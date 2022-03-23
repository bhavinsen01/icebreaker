from core.hashing import Hasher
from db.models.users import User
from schemas.users import UserCreate
from sqlalchemy.orm import Session


def create_new_user(user: UserCreate, db: Session):
    user = User(
        first_name = user.first_name,
        last_name = user.last_name,
        mobile = user.mobile,
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        organization = user.organization,
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user
