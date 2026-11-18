from fastapi import APIRouter
import requests

router = APIRouter(prefix="/movies")

API_KEY = "d4b37b6e-fe4e-46cb-879f-27a19967c7ca"

@router.get("/search/{query}")
def search_movie(query: str):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={query}"
    res = requests.get(url).json()

    if res.get("Response") == "True":
        return res["Search"]
    return []