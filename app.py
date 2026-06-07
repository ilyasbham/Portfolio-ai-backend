import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ---------------- DATA ----------------
data = [
    {"question": "What is your name?", "answer": "My name is Ilyas Bham."},
    {"question": "What is your major?", "answer": "Computer Engineering."},
    {"question": "What projects have you built?", "answer": "Portfolio, Employee System, Book Store."},
    {"question": "Where do you study?", "answer": "I study at Karabuk University in Turkey."},
    {"question": "What programming languages do you know?", "answer": "Java, Python, JavaScript, SQL, HTML, CSS, Kotlin."}
]

# ---------------- SIMPLE AI LOGIC (NO ML MODEL) ----------------
def simple_similarity(user_q, stored_q):
    user_words = set(user_q.lower().split())
    stored_words = set(stored_q.lower().split())
    return len(user_words.intersection(stored_words))


def get_top_k(user_question, k=3):
    scores = []

    for item in data:
        score = simple_similarity(user_question, item["question"])
        scores.append({
            "question": item["question"],
            "answer": item["answer"],
            "score": score
        })

    scores = sorted(scores, key=lambda x: x["score"], reverse=True)
    return scores[:k]


def query_ai(user_question):
    top3 = get_top_k(user_question, 3)
    best = top3[0]

    # threshold (tweak if needed)
    if best["score"] == 0:
        return {
            "answer": "Sorry, I don't have enough information about that.",
            "confidence": 0,
            "alternatives": [x["answer"] for x in top3[1:]]
        }

    return {
        "answer": best["answer"],
        "confidence": best["score"],
        "alternatives": [x["answer"] for x in top3[1:]]
    }

# ---------------- ROUTES ----------------
@app.route("/", methods=["GET"])
def home():
    return "AI Backend Running 🚀"


@app.route("/chat", methods=["POST"])
def chat():
    data_req = request.get_json()
    message = data_req.get("message", "")

    result = query_ai(message)

    return jsonify(result)

# ---------------- RENDER FIX ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)