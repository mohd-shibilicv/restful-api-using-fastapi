from fastapi import FastAPI, HTTPException
from typing import List

from models import UserRequestModel, UserResponseModel


app = FastAPI()

users_db = []


@app.post("/users/", response_model=UserResponseModel, status_code=201)
async def create_user(user: UserRequestModel):
    new_user_id = len(users_db) + 1
    new_user = UserResponseModel(
        id=new_user_id,
        username=user.username,
        email=user.email,
        age=user.age
    )
    users_db.append(new_user)
    return new_user


@app.get("/users/{user_id}", response_model=UserResponseModel)
async def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
        raise HTTPException(status_code=404, detail="User not found")


@app.get("/users/", response_model=List[UserResponseModel])
async def list_users():
    return users_db
