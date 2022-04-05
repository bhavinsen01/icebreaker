from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.users import ShowUser
from db.repository.login import get_user_by_id, get_users
from typing import List

router = APIRouter()


@router.get("/{user_id}", response_model=ShowUser)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_id(user_id=user_id, db=db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/alluser/", response_model=List[ShowUser])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users