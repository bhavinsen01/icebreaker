from fastapi import APIRouter, UploadFile, File
from db.repository.images import upload_images
from db.session import get_db
from fastapi import Depends
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/")
async def upload_image(files: UploadFile=File(...), db: Session = Depends(get_db)):
    upload_image = upload_images(files=files.filename, db=db)
    return {"upload_image": upload_image}