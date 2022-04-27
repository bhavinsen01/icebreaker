from core.hashing import Hasher
from db.models.users import User, SortOption
from schemas.users import UserCreate, CreataSortOption
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
        postal= user.postal,
        pref= user.pref,
        city= user.city,
        address= user.address,
        # interested_category_id_1= user.interested_category_id_1,
        # interested_category_id_2= user.interested_category_id_2,
        # sort_option_id= user.sort_option_id,
        device= user.device,
        # last_accessed= user.last_accessed,
        # line_access_token= user.line_access_token,
        # line_refresh_token= user.line_refresh_token,
        # line_id= user.line_id,
        # line_pic_url= user.line_pic_url,
        # line_name= user.line_name,
        # created_at= user.created_at,
        # is_active=True,
        # is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user

def create_sort_option(sortoption: CreataSortOption, db: Session):
    sortoption = SortOption(
        sort_type = sortoption.sort_type
    )
    db.add(sortoption)
    db.commit()
    db.refresh(sortoption)
    return sortoption

def get_sort_option_by_id(sort_option_id: int, db: Session):
    return db.query(SortOption).filter(SortOption.id == sort_option_id).first()

def get_sort_options(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SortOption).offset(skip).limit(limit).all()