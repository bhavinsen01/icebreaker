from fastapi import APIRouter
from db.repository.post import create_new_post
from db.session import get_db
from fastapi import Depends, UploadFile, File
from schemas.post_contents import CreateProduct
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/")
async def create_post_contents(posts: CreateProduct = Depends(), data: UploadFile = File(...), db: Session = Depends(get_db)):
    post_contents = create_new_post(post=posts, files=data.filename, db=db)
    return post_contents

