from fastapi import APIRouter
from db.repository.post import create_category_attribute, creata_category
from db.session import get_db
from fastapi import Depends
from schemas.post_contents import CreateCategoryAttribute, ShowCategory, ShowCategoryAttribute, CreateCategory
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/", response_model=ShowCategory)
def category(category: CreateCategory, db: Session = Depends(get_db)):
    category = creata_category(category=category, db=db)
    return category

@router.post("/categoryattr", response_model=ShowCategoryAttribute)
def category_attribut(categoryattr: CreateCategoryAttribute, db: Session = Depends(get_db)):
    category_attribute = create_category_attribute(categoryattr=categoryattr, db=db)
    return category_attribute

