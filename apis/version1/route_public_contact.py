from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, Text
from fastapi.encoders import jsonable_encoder


router = APIRouter()

postdb = []

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    mobile: Optional[str]

@router.get("/get/{detail_id}")
def get_user(user_id: int):
    user = user_id - 1
    return postdb[user]

@router.post("/post")
def add_user(user: User):
    postdb.append(user.dict())
    return postdb[-1]

@router.put("/update/{user_id}", response_model=User)
async def update_user(user_id: int, item: User):
    update_user_encoded = jsonable_encoder(item)
    postdb[user_id - 1] = update_user_encoded
    return update_user_encoded

@router.delete("/delete/{post_id}")
def delete_user(user_id: int):
    postdb.pop(user_id-1)
    return {"message": "User has been deleted succesfully"}