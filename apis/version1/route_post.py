from fastapi import APIRouter
from db.repository.post import create_new_post,create_sub_category
from db.session import get_db
from fastapi import Depends
from schemas.post_contents import PostCreate,SubCategories
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/")
def create_post_contents(posts: PostCreate, db: Session = Depends(get_db)):
    post_contents = create_new_post(post=posts, db=db)
    return post_contents

@router.post("/subcategory")
def create_sub_category_type(categories: SubCategories, db: Session = Depends(get_db)):
    sub_categories = create_sub_category(sub_category_types=categories, db=db)
    return sub_categories
