from db.models.users import User
from sqlalchemy.orm import Session


def get_user(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    return user

def get_user_by_id(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()