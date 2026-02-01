from flask import Flask, render_template, request, jsonify
from backend import analyze_review

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    # Phải trả về đúng file index.html trong thư mục templates
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        text = data.get("text", "").strip()
        category = data.get("category", "").strip()
        rating = data.get("rating", "5")
        
        # Gọi backend xử lý
        result = analyze_review(text, category, rating)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, threaded=True)