from fastapi import UploadFile
from pydantic import BaseModel

class UploadImages(BaseModel):
    file_name: UploadFile