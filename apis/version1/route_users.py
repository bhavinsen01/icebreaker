from db.repository.login import get_user_by_email, get_user_by_id, get_users
from db.repository.users import create_new_user, create_sort_option, get_sort_option_by_id, get_sort_options
from db.session import get_db, engine
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from schemas.users import ShowUser, UpdateUser, UserCreate, CreataSortOption, ShowSortOption, UpdateSortOption
from sqlalchemy.orm import Session
from db.models.users import SortOption, User
from typing import List

router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = create_new_user(user=user, db=db)
    return user

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

@router.patch("/{user_id}", response_model=ShowUser)
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

@router.delete("/delete/{user_id}")
def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        session.delete(user)
        session.commit()
        return {"User": "User Deleted Successfully"}

    
@router.post("/sortoption")
def create_sortoption(sort_option: CreataSortOption, db: Session = Depends(get_db)):
    sort_option = create_sort_option(sortoption=sort_option, db=db)
    return sort_option

@router.get("/sortoption/{sort_option_id}", response_model=ShowSortOption)
def read_sort_type(sort_option_id: int, db: Session = Depends(get_db)):
    db_sort_option = get_sort_option_by_id(sort_option_id=sort_option_id, db=db)
    if db_sort_option is None:
        raise HTTPException(status_code=404, detail="Sort option not found")
    return db_sort_option

@router.get("/sortoption/allsortoption/", response_model=List[ShowSortOption])
def read_sort_options(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sort_option = get_sort_options(db, skip=skip, limit=limit)
    return sort_option

@router.patch("/sortoption/{sort_option_id}", response_model=ShowSortOption)
def update_sort_option(sort_option_id: int, sort_option: UpdateSortOption):
    with Session(engine) as session:
        db_sort_option = session.get(SortOption, sort_option_id)
        if not db_sort_option:
            raise HTTPException(status_code=404, detail="Sort Option not found")
        sort_option_update = sort_option.dict(exclude_unset=True)
        for key, value in sort_option_update.items():
            setattr(db_sort_option, key, value)
        session.add(db_sort_option)
        session.commit()
        session.refresh(db_sort_option)
        return db_sort_option

@router.delete("/sortoption/delete/{sort_option_id}")
def delete_sort_option(sort_option_id: int):
    with Session(engine) as session:
        sort_option = session.get(SortOption, sort_option_id)
        if not sort_option:
            raise HTTPException(status_code=404, detail="Sort Option not found")
        session.delete(sort_option)
        session.commit()
        return {"Sort Option": "Sort Option Deleted Successfully"}