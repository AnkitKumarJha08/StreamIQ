from fastapi import APIRouter

router = APIRouter(prefix="/analytics")

data = {
    "hours_watched": 120,
    "favorite_genre": "Thriller",
    "peak_time": "10 PM"
}

@router.get("/")
def get_analytics():
    return data