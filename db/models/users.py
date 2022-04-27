from db.base_class import Base
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    mobile = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True)
    hashed_password = Column(String, nullable=False)
    organization = Column(String)
    postal = Column(String)
    pref = Column(String)
    city = Column(String)
    address = Column(String)
    # interested_category_id_1 = Column(Integer)
    # interested_category_id_2 = Column(Integer)
    # sort_option_id = Column(Integer, default=0)
    device = Column(Integer)
    # last_accessed = Column(DateTime, default=datetime.datetime)
    # line_access_token = Column(String)
    # line_refresh_token = Column(String)
    line_id = Column(String)
    line_pic_url = Column(String)
    line_name = Column(String)
    # created_at = Column(DateTime)
    # is_active = Column(Boolean(), default=True)
    # is_superuser = Column(Boolean(), default=False)
    

class SortOption(Base):
    id = Column(Integer, primary_key=True, index=True)
    sort_type = Column(String, nullable=False)