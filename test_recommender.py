from ml.recommender import CineMindEngine

engine = CineMindEngine()
res = engine.get_recommendations(
    "action movie",
    "Action",
    "Telugu",
    70,
    quantum_mode=True
)

for r in res:
    print(r["movie"]["title"], r["score"])
