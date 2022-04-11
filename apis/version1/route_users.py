from db.repository.login import get_user_by_email
from db.repository.users import create_new_user
from db.session import get_db
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from schemas.users import ShowUser
from schemas.users import UserCreate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = create_new_user(user=user, db=db)
    return user
