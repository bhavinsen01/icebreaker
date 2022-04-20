from fastapi import APIRouter
from db.repository.post import create_new_post
from db.session import get_db
from fastapi import Depends
from schemas.post_contents import CreateProduct
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/")
def create_post_contents(posts: CreateProduct, db: Session = Depends(get_db)):
    post_contents = create_new_post(post=posts, db=db)
    return post_contents

