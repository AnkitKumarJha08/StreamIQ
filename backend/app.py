from fastapi import FastAPI
from routes import auth, movies, ai, analytics

app = FastAPI(title="StreamIQ AI")

app.include_router(auth.router)
app.include_router(movies.router)
app.include_router(ai.router)
app.include_router(analytics.router)

@app.get("/")
def home():
    return {"message": "StreamIQ Backend Running 🚀"}