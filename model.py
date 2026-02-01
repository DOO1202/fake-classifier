import torch.nn as nn
from transformers import RobertaModel
class FakeDetection(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        #roberta
        self.roberta = RobertaModel.from_pretrained('roberta-base', add_pooling_layer = False)
        for param in self.roberta.parameters():
            param.requires_grad=False
        hidden_dim = 512
        #classification head
        self.head = nn.Sequential(
            nn.Dropout(0.3),
            nn.Linear(self.roberta.config.hidden_size, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_classes),
        )
    def forward(self, input_ids, attention_mask):
        outputs = self.roberta(
            input_ids=input_ids,
            attention_mask=attention_mask,
        )
        #classification vector
        first_vecs = outputs.last_hidden_state[:, 0, :]
        logits = self.head(first_vecs)
        return logits