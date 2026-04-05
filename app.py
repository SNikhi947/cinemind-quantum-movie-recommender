import os
from flask import Flask, render_template, request, jsonify
from ml.recommender import CineMindEngine
import google.generativeai as genai

app = Flask(__name__)

# Initialize Recommender Engine
recommender = CineMindEngine()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/results")
def results():
    return render_template("results.html")


@app.route("/api/recommend", methods=["POST"])
def recommend_movies():
    data = request.json

    prompt = data.get("query", "")
    genre = data.get("genre", "All")
    language = data.get("language", "All")
    mood = data.get("mood", 50)
    quantum_mode = data.get("quantum", False)

    recommendations = recommender.get_recommendations(
        prompt=prompt,
        genre_filter=genre,
        language_filter=language,
        mood_score=mood,
        quantum_mode=quantum_mode
    )

    return jsonify(recommendations)


@app.route("/api/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    user_msg = data.get("message", "")

    context = """
    You are CineMind AI Assistant.
    You explain movie recommendations,
    user preferences, genres, languages,
    and moods in a friendly way.
    Do not directly recommend movies.
    Keep answers simple and engaging.
    """

    response = model.generate_content(context + user_msg)
    return jsonify({"reply": response.text})


if __name__ == "__main__":
    app.run(debug=True)
