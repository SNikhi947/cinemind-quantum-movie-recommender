import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

from ml.quantum_engine import QuantumRecommender


class CineMindEngine:
    def __init__(self):
        self.movies = []

        if os.path.exists("data/movies.json"):
            with open("data/movies.json", "r", encoding="utf-8") as f:
                self.movies = json.load(f)
        else:
            print("❌ Data missing. Run seed_data.py")
            self.movies = []
            return

        self.soup = []
        for m in self.movies:
            combined_text = (
                f"{m['language']} {m['language']} "
                f"{' '.join(m['genres'])} {' '.join(m['genres'])} "
                f"{m['overview']}"
            )
            self.soup.append(combined_text)

        self.tfidf = TfidfVectorizer(stop_words="english")
        self.matrix = self.tfidf.fit_transform(self.soup)

        # REAL QUANTUM ENGINE
        self.quantum_engine = QuantumRecommender()
        dense_vectors = self.matrix.toarray()
        self.quantum_vectors = self.quantum_engine.fit_transform_data(dense_vectors)

    def get_recommendations(
        self,
        prompt,
        genre_filter,
        language_filter,
        mood_score,
        quantum_mode=False,
    ):
        user_vec = self.tfidf.transform([prompt])
        sim_scores = cosine_similarity(user_vec, self.matrix).flatten()

        # Filters
        for idx, movie in enumerate(self.movies):
            if genre_filter != "All" and genre_filter not in movie["genres"]:
                sim_scores[idx] = 0

            if language_filter != "All" and movie["language"] != language_filter:
                sim_scores[idx] = 0

        # REAL QUANTUM HYBRID
        if quantum_mode:
            user_dense = user_vec.toarray()
            q_input = self.quantum_engine.transform_single(user_dense)

            quantum_scores = []
            for i in range(len(self.quantum_vectors)):
                q_score = self.quantum_engine.compute_quantum_similarity(
                    q_input.flatten(), self.quantum_vectors[i]
                )
                quantum_scores.append(q_score)

            quantum_scores = np.array(quantum_scores)

            sim_scores = (0.7 * sim_scores) + (0.3 * quantum_scores)

        top_indices = sim_scores.argsort()[-8:][::-1]

        results = []
        for idx in top_indices:
            if sim_scores[idx] > 0.0:
                results.append(
                    {
                        "movie": self.movies[idx],
                        "score": round(sim_scores[idx] * 100, 1),
                        "reason": f"Matched {self.movies[idx]['language']} {self.movies[idx]['genres'][0]}",
                    }
                )

        if not results:
            fallback = []
            for m in self.movies:
                if (
                    (genre_filter == "All" or genre_filter in m["genres"])
                    and (language_filter == "All" or m["language"] == language_filter)
                ):
                    fallback.append(m)

            return [
                {"movie": m, "score": 85, "reason": "Popular Choice"}
                for m in fallback[:5]
            ]

        return results[:5]
