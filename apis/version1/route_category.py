from fastapi import APIRouter
from db.repository.post import creata_category, get_category_by_id, get_categories
from db.session import get_db, engine
from fastapi import Depends, HTTPException
from schemas.post_contents import ShowCategory, CreateCategory, UpdateCategory
from sqlalchemy.orm import Session
from db.models.post_content import Category
from typing import List

router = APIRouter()

@router.post("/", response_model=ShowCategory)
def category(category: CreateCategory, db: Session = Depends(get_db)):
    category = creata_category(category=category, db=db)
    return category

@router.get("/{category_id}", response_model=ShowCategory)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = get_category_by_id(category_id=category_id, db=db)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category Not Found")
    return db_category

@router.get("/allcategory/", response_model=List[ShowCategory])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    category = get_categories(db, skip=skip, limit=limit)
    return category

@router.patch("/{category_id}", response_model=ShowCategory)
def update_category(category_id: int, category: UpdateCategory):
    with Session(engine) as session:
        db_category = session.get(Category, category_id)
        if not db_category:
            raise HTTPException(status_code=404, detail="Category not found")
        category_update = category.dict(exclude_unset=True)
        for key, value in category_update.items():
            setattr(db_category, key, value)
        session.add(db_category)
        session.commit()
        session.refresh(db_category)
        return db_category

@router.delete("/delete/{category_id}")
def delete_category(category_id: int):
    with Session(engine) as session:
        category = session.get(Category, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        session.delete(category)
        session.commit()
        return {"Category": "Category Deleted Successfully"}