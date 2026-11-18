from fastapi import APIRouter
import requests

router = APIRouter(prefix="/ai")

API_KEY = "YOUR_OMDB_API_KEY"

# 🧠 Smart AI mood mapping
def get_keywords(mood: str):
    mood = mood.lower()

    if "sad" in mood:
        return ["drama", "emotional", "life"]
    elif "romantic" in mood or "love" in mood:
        return ["romance", "love", "relationship"]
    elif "bored" in mood:
        return ["action", "thriller", "adventure"]
    elif "happy" in mood:
        return ["comedy", "fun", "family"]
    elif "scared" in mood or "horror" in mood:
        return ["horror", "ghost", "dark"]
    else:
        return ["popular"]

@router.get("/mood/{mood}")
def mood_search(mood: str):
    keywords = get_keywords(mood)

    results = []

    for word in keywords:
        url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={word}"
        res = requests.get(url).json()

        if res.get("Response") == "True":
            results.extend(res["Search"])

    # remove duplicates
    unique = {movie["imdbID"]: movie for movie in results}.values()

    return list(unique)[:10]