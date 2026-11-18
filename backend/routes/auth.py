from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/auth")

users = {}

class User(BaseModel):
    username: str
    password: str

@router.post("/signup")
def signup(user: User):
    users[user.username] = user.password
    return {"msg": "User created"}

@router.post("/login")
def login(user: User):
    if users.get(user.username) == user.password:
        return {"msg": "Login success"}
    return {"msg": "Invalid credentials"}