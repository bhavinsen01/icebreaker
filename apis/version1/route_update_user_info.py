from db.models.users import User
from fastapi import APIRouter
from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.users import ShowUser, UpdateUser 
from db.session import engine


router = APIRouter()


@router.put("/{user_id}", response_model=ShowUser)
def update_user(user_id: int, user: UpdateUser):
    with Session(engine) as session:
        db_user = session.get(User, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        user_update = user.dict(exclude_unset=True)
        for key, value in user_update.items():
            setattr(db_user, key, value)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
