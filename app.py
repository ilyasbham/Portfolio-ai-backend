import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)
CORS(app)

# ---------------- MODEL (FIXED) ----------------
model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

data = [
    {"question":"What is your name?","answer":"My name is Ilyas Bham."},
    {"question":"Who are you?","answer":"I am Ilyas Bham, a Computer Engineering student and aspiring software engineer."},
    {"question":"Where are you from?","answer":"I am originally from Myanmar and currently studying in Turkey."},
    {"question":"Which university do you study at?","answer":"I study at Karabuk University in Turkey."},
    {"question":"What is your major?","answer":"My major is Computer Engineering."},
    {"question":"What year are you in?","answer":"I am in my final year of Computer Engineering."},
    {"question":"What is your GPA?","answer":"My GPA is approximately 2.7."},
    {"question":"What programming languages do you know?","answer":"I know Java, Python, JavaScript, SQL, HTML, CSS, and Kotlin."},
    {"question":"What projects have you built?","answer":"Portfolio, Employee System, Book Store, Resume Builder."},
]

# ---------------- EMBEDDINGS ----------------
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

# ---------------- API ----------------
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    return jsonify(query_ai(user_message))


@app.route("/", methods=["GET"])
def home():
    return "AI Backend is running"

# ---------------- RUN (RENDER SAFE) ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)