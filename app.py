import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ---------------- DATA ----------------
data = [
   data = [
    {"question":"What is your name?","answer":"My name is Ilyas Bham."},
    {"question":"Who are you?","answer":"I am Ilyas Bham, a Computer Engineering student and aspiring software engineer."},
    {"question":"Where are you from?","answer":"I am originally from Myanmar and currently studying in Turkey."},
    {"question":"Which university do you study at?","answer":"I study at Karabuk University in Turkey."},
    {"question":"What is your major?","answer":"My major is Computer Engineering."},
    {"question":"What year are you in?","answer":"I am in my final year of Computer Engineering."},
    {"question":"What is your GPA?","answer":"My GPA is approximately 2.7."},
    {"question":"What programming languages do you know?","answer":"I know Java, Python, JavaScript, SQL, HTML, CSS, and Kotlin."},
    {"question":"Which language are you strongest in?","answer":"Java is one of my strongest programming languages."},
    {"question":"Do you know Python?","answer":"Yes, I use Python for machine learning, scripting, and automation."},
    {"question":"Do you know Java?","answer":"Yes, I use Java extensively for backend development and software engineering projects."},
    {"question":"Do you know JavaScript?","answer":"Yes, I use JavaScript for frontend web development with React."},
    {"question":"Do you know Kotlin?","answer":"Yes, I use Kotlin for Android development with Jetpack Compose."},
    {"question":"What frontend technologies do you know?","answer":"I know React, JavaScript, HTML, CSS, Tailwind CSS, and Vite."},
    {"question":"What backend technologies do you know?","answer":"I know Spring Boot, REST APIs, Firebase, and Java backend development."},
    {"question":"What databases do you know?","answer":"I have experience with MySQL, MongoDB, and Firebase Firestore."},
    {"question":"What version control system do you use?","answer":"I use Git and GitHub for version control and collaboration."},
    {"question":"What frameworks do you know?","answer":"I know Spring Boot, React, Jetpack Compose, Firebase, and Tailwind CSS."},
    {"question":"Do you know Spring Boot?","answer":"Yes, Spring Boot is my preferred backend framework."},
    {"question":"Do you know React?","answer":"Yes, React is my preferred frontend framework."},
    {"question":"Do you know Firebase?","answer":"Yes, I have worked with Firebase Authentication, Firestore, and Hosting."},
    {"question":"Do you know MongoDB?","answer":"Yes, I have experience building applications using MongoDB."},
    {"question":"What IDEs do you use?","answer":"I use IntelliJ IDEA, Visual Studio Code, Android Studio, and PyCharm."},
    {"question":"What operating systems do you use?","answer":"I mainly use Windows and have some Linux experience."},

    {"question":"What languages can you speak?","answer":"I can speak Burmese, English, and Turkish."},
    {"question":"Do you speak English?","answer":"Yes, I communicate comfortably in English."},
    {"question":"Do you speak Turkish?","answer":"Yes, I have experience communicating and studying in Turkish."},

    {"question":"What are your career goals?","answer":"I want to become a professional software engineer and work internationally."},
    {"question":"What field interests you the most?","answer":"Backend development, full-stack development, artificial intelligence, and machine learning."},
    {"question":"Are you interested in AI?","answer":"Yes, I am highly interested in Artificial Intelligence and Machine Learning."},
    {"question":"Are you interested in machine learning?","answer":"Yes, I enjoy learning and experimenting with machine learning algorithms."},

    {"question":"What machine learning algorithms do you know?","answer":"I have studied KNN, SVM, Logistic Regression, Decision Trees, Random Forest, CNN, and LSTM."},
    {"question":"Do you know CNN?","answer":"Yes, CNN stands for Convolutional Neural Network and is used in image processing."},
    {"question":"Do you know LSTM?","answer":"Yes, LSTM is a recurrent neural network architecture used for sequential data."},
    {"question":"Do you know Random Forest?","answer":"Yes, Random Forest is an ensemble machine learning algorithm."},
    {"question":"Do you know KNN?","answer":"Yes, KNN is a supervised machine learning algorithm used for classification and regression."},

    {"question":"What projects have you built?","answer":"I have built Employee Management Systems, Restaurant Management Systems, Student Registration Systems, Resume Builders, Portfolio Websites, and Book Store applications."},
    {"question":"Tell me about your Employee Management System.","answer":"It is a full-stack application built with Spring Boot and React including authentication, CRUD operations, search, pagination, image upload, and responsive UI."},
    {"question":"Tell me about your Restaurant Management System.","answer":"It is a software project designed to manage restaurant operations efficiently."},
    {"question":"Tell me about your Portfolio Website.","answer":"My portfolio website showcases my projects, skills, experience, and contact information."},
    {"question":"Tell me about your Resume Builder project.","answer":"The Resume Builder helps users generate professional resumes dynamically."},
    {"question":"Tell me about your Book Store project.","answer":"The Book Store project uses Spring Boot, MongoDB, React, DTOs, services, repositories, and REST APIs."},

    {"question":"Have you worked in a team?","answer":"Yes, I have collaborated on large software projects using GitHub and Git workflows."},
    {"question":"What is Git Flow?","answer":"Git Flow is a branching strategy used for collaborative software development."},
    {"question":"Have you used GitHub?","answer":"Yes, I use GitHub for source control, project management, and collaboration."},

    {"question":"What software engineering concepts do you know?","answer":"I know Object-Oriented Programming, Design Patterns, Data Structures, Algorithms, Database Design, and REST API development."},
    {"question":"What algorithms have you studied?","answer":"I have studied BFS, DFS, Dijkstra, Bellman-Ford, Prim's Algorithm, and Dynamic Programming."},
    {"question":"What networking concepts have you studied?","answer":"I have studied IP, NAT, Routing, Router Architecture, SDN, and Network Layer concepts."},
    {"question":"What database concepts have you studied?","answer":"I have studied ER Diagrams, Normalization, SQL, ARC Structures, and Database Design."},

    {"question":"Can you build REST APIs?","answer":"Yes, I can design and develop RESTful APIs using Spring Boot."},
    {"question":"Can you build full-stack applications?","answer":"Yes, I can build full-stack applications using Spring Boot and React."},
    {"question":"Can you build Android applications?","answer":"Yes, I can build Android applications using Kotlin and Jetpack Compose."},
    {"question":"Can you create responsive websites?","answer":"Yes, I can create responsive websites using React, CSS, and Tailwind CSS."},
    {"question":"Can you work with databases?","answer":"Yes, I can design, query, and manage relational and NoSQL databases."},

    {"question":"What are your strengths?","answer":"Quick learning, problem solving, backend development, teamwork, and adaptability."},
    {"question":"Why should someone hire you?","answer":"I have strong foundations in software engineering, experience with full-stack development, and a passion for continuous learning."},
    {"question":"What kind of jobs are you looking for?","answer":"Software Engineer, Backend Developer, Full Stack Developer, or Machine Learning Engineer roles."},
    {"question":"Do you have experience with APIs?","answer":"Yes, I have built and consumed REST APIs in multiple projects."},
    {"question":"What is your favorite backend technology?","answer":"Spring Boot is my favorite backend technology."},
    {"question":"What is your favorite frontend technology?","answer":"React is my favorite frontend technology."},
    {"question":"What is your favorite database?","answer":"I enjoy working with MongoDB and MySQL."},
    {"question":"What is your dream career?","answer":"My dream is to become a successful software engineer working on impactful global projects."},
    {"question":"Do you create content?","answer":"I plan to create educational programming content and Python tutorials on YouTube."},
    {"question":"What kind of software can you build?","answer":"Web applications, REST APIs, Android apps, management systems, AI chatbots, and database-driven applications."}
]
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