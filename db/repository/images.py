from db.models.upload_image import UploadImage
from schemas.upload_images import UploadImages
from fastapi import UploadFile
from sqlalchemy.orm import Session

def upload_images(files: UploadImages, db: Session):
    file = UploadImage(
        file_title = files
    )
    db.add(file)
    db.commit()
    db.refresh(file)
    return file