from sqlalchemy import Column, Integer, String, Text
from db.base_class import Base

class UploadImage(Base):
    __tablename__ = 'uploadimage'
    id = Column(Integer, primary_key= True, index=True)
    file_title = Column(String)