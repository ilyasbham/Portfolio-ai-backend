import os
from flask import Flask, request, jsonify
from flask_cors import CORS

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)
CORS(app)

# ---------------- MODEL (LIGHTWEIGHT) ----------------
# IMPORTANT: smaller model = prevents Render 512MB crash
model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------------- DATA ----------------
data = [
    {"question":"What is your name?","answer":"My name is Ilyas Bham."},
    {"question":"What is your major?","answer":"Computer Engineering."},
    {"question":"What projects have you built?","answer":"Portfolio, Employee System, Book Store."},
    {"question":"Where do you study?","answer":"I study at Karabuk University in Turkey."},
    {"question":"What programming languages do you know?","answer":"Java, Python, JavaScript, SQL, HTML, CSS, Kotlin."}
]

# ---------------- PRE-COMPUTE EMBEDDINGS (IMPORTANT FIX) ----------------
questions = [d["question"] for d in data]
embeddings = model.encode(questions)

# ---------------- AI LOGIC ----------------
def get_top_k(user_question, k=3):
    user_emb = model.encode([user_question])

    scores = cosine_similarity(user_emb, embeddings)[0]
    top_k_idx = np.argsort(scores)[::-1][:k]

    results = []
    for i in top_k_idx:
        results.append({
            "question": data[i]["question"],
            "answer": data[i]["answer"],
            "score": float(scores[i])
        })

    return results


def query_ai(user_question):
    top3 = get_top_k(user_question, 3)
    best = top3[0]

    if best["score"] < 0.45:
        return {
            "answer": "Sorry, I don't have enough information about that.",
            "confidence": float(best["score"]),
            "alternatives": [x["answer"] for x in top3[1:]]
        }

    return {
        "answer": best["answer"],
        "confidence": float(best["score"]),
        "alternatives": [x["answer"] for x in top3[1:]]
    }

# ---------------- ROUTES ----------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    result = query_ai(message)

    return jsonify(result)


@app.route("/", methods=["GET"])
def home():
    return "AI Backend Running 🚀"


# ---------------- RENDER FIX ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)