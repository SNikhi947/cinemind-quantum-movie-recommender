# 🎬 CineMind – Quantum Movie Recommendation System

CineMind is an advanced AI-powered movie recommendation system that combines **Machine Learning (ML), Natural Language Processing (NLP), and Quantum Machine Learning (QML)** to provide highly personalized movie suggestions.

This project demonstrates how **quantum computing concepts** can enhance modern recommendation systems.

---

## 🚀 Features

- 🔐 User Authentication (Login & Register)
- 🎤 Voice-Based Movie Search (Speech-to-Text)
- 🧠 NLP Prompt-Based Recommendations  
  _Example: "Suggest emotional romantic movies like Sita Ramam"_
- 🎯 Personalized Movie Recommendations
- ⚛️ Quantum Machine Learning Integration (Qiskit)
- 📊 Explainable AI (Shows why a movie is recommended)
- 🎞️ Movie Cards with Poster, Rating, and Trailer
- 📺 OTT Platform Filtering
- ❤️ Watchlist & History Tracking
- 📈 Trending & Smart Playlist Generation

---

## 🧠 Technologies Used

### Frontend
- HTML5
- CSS3 (Glassmorphism + Animations)
- JavaScript (Vanilla JS)

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- K-Nearest Neighbors (KNN)

### Quantum Machine Learning
- Qiskit
- Quantum Support Vector Classifier (QSVC)
- Variational Quantum Circuits (QNN)

### Database
- SQLite

---

## ⚙️ How It Works

1. User inputs preferences:
   - Genres
   - Favorite Movies
   - Text Prompt
   - Voice Input

2. Data Processing:
   - Text is converted using TF-IDF
   - Features are extracted and normalized

3. Classical ML Model:
   - Finds similarity using cosine similarity

4. Quantum ML Model:
   - Uses Qiskit to refine predictions

5. Final Output:
   - Personalized movie recommendations
   - Explanation for each recommendation

---

## ⚛️ Quantum Advantage

This project integrates **Quantum Machine Learning (QML)** to:

- Handle complex feature relationships
- Improve pattern recognition
- Demonstrate future AI + Quantum applications

> Note: Uses Qiskit simulator (no physical quantum hardware required)

---

## 📂 Project Structure
cinemind/
│── frontend/
│── backend/
│── ml/
│── data/
│── app.py
│── requirements.txt
│── README.md


---

## ▶️ Run Locally

### 1. Clone Repository
```bash
git clone https://github.com/your-username/cinemind-quantum-movie-recommender.git
cd cinemind-quantum-movie-recommender
. Install Dependencies
pip install -r requirements.txt
3. Run Application
python app.py
4. Open in Browser
http://localhost:5000
📊 Dataset
Movie dataset (custom / MovieLens / TMDB style)
Contains:
Title
Genre
Overview
Rating
Tags
📈 Evaluation Metrics
Accuracy
Precision
Recall
F1 Score
Cosine Similarity Score
💡 Future Enhancements
Real Quantum Hardware Integration
Deep Learning Models
Multi-language Support
OTT Platform API Integration
Reinforcement Learning for better recommendations
👨‍💻 Author

Nikhil Kumar
B.Tech CSE Student

⭐ Support

If you like this project, give it a ⭐ on GitHub.
