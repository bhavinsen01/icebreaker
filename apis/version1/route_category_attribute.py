from fastapi import APIRouter
from db.repository.post import create_category_attribute, creata_category, get_categoryattr_by_id, get_categoryattrs, get_category_by_id, get_categories
from db.session import get_db, engine
from fastapi import Depends, HTTPException
from schemas.post_contents import CreateCategoryAttribute, ShowCategory, ShowCategoryAttribute, CreateCategory, UpdateCategoryAttribute, UpdateCategory
from sqlalchemy.orm import Session
from db.models.post_content import CategoryAttribute, Category
from typing import List

router = APIRouter()

@router.post("/categoryattr", response_model=ShowCategoryAttribute)
def category_attribut(categoryattr: CreateCategoryAttribute, db: Session = Depends(get_db)):
    category_attribute = create_category_attribute(categoryattr=categoryattr, db=db)
    return category_attribute

@router.get("/{categoryattr_id}", response_model=ShowCategoryAttribute)
def read_category_attribute(categoryattr_id: int, db: Session = Depends(get_db)):
    db_categoryattr = get_categoryattr_by_id(categoryattr_id=categoryattr_id, db=db)
    if db_categoryattr is None:
        raise HTTPException(status_code=404, detail="Category Attribute not found")
    return db_categoryattr

@router.get("/allcategoryattr/", response_model=List[ShowCategoryAttribute])
def read_categoryattrs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categoryattr = get_categoryattrs(db, skip=skip, limit=limit)
    return categoryattr

@router.patch("/{categoryattr_id}", response_model=ShowCategoryAttribute)
def update_categoryattr(categoryattr_id: int, categoryattr: UpdateCategoryAttribute):
    with Session(engine) as session:
        db_categoryattr = session.get(CategoryAttribute, categoryattr_id)
        if not db_categoryattr:
            raise HTTPException(status_code=404, detail="Category Attribute not found")
        categoryattr_update = categoryattr.dict(exclude_unset=True)
        for key, value in categoryattr_update.items():
            setattr(db_categoryattr, key, value)
        session.add(db_categoryattr)
        session.commit()
        session.refresh(db_categoryattr)
        return db_categoryattr

@router.delete("/delete/{categoryattr_id}")
def delete_categoryattr(categoryattr_id: int):
    with Session(engine) as session:
        categoryattr = session.get(CategoryAttribute, categoryattr_id)
        if not categoryattr:
            raise HTTPException(status_code=404, detail="Category Attribute not found")
        session.delete(categoryattr)
        session.commit()
        return {"Category Attribute": "Category Attribute Deleted Successfully"}