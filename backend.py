import torch
import torch.nn.functional as F
from transformers import RobertaTokenizer
from model import FakeDetection

device = torch.device("cpu")

# Load tokenizer & model
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")

model = FakeDetection(num_classes=2)
model.load_state_dict(
    torch.load("model_weights.pth", map_location=device),
    strict=False
)
model.to(device)
model.eval()

def analyze_review(text, category, rating):
    combined_text = f"Category: {category}. Rating: {rating}. Review: {text}"

    encoded = tokenizer.encode_plus(
        combined_text,
        max_length=256,
        padding="max_length",
        truncation=True,
        return_tensors="pt"
    )

    input_ids = encoded["input_ids"].to(device)
    attention_mask = encoded["attention_mask"].to(device)

    with torch.no_grad():
        logits = model(input_ids, attention_mask)
        probs = F.softmax(logits, dim=1)

    real_prob = probs[0][0].item() * 100
    fake_prob = probs[0][1].item() * 100

    label = "REAL (Genuine)" if fake_prob > real_prob else "FAKE (Fraudulent)"

    return {
        "label": label,
        "fake_prob": round(fake_prob, 2),
        "real_prob": round(real_prob, 2)
    }