from typing import Optional
from pydantic import BaseModel
from pydantic import EmailStr

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    mobile: str = "0123456789"
    username: str
    email: Optional[EmailStr] = None
    password: str
    organization: Optional[str] = None
    postal: Optional[str] = None
    pref: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    # interested_category_id_1: Optional[int] = None
    # interested_category_id_2: Optional[int] = None
    # sort_option_id: Optional[int] = 0
    device: Optional[int] = None
    # last_accessed: Optional[datetime] = None
    # line_access_token: Optional[str] = None
    # line_refresh_token: Optional[str] = None
    line_id: Optional[str] = None
    line_pic_url: Optional[str] = None
    line_name: Optional[str] = None
    # created_at: datetime


class ShowUser(BaseModel):
    username: str
    email: EmailStr
    organization: str
    first_name: str
    last_name: str
    mobile: str
    postal: str
    pref: str
    city: str
    address: str
    # interested_category_id_1: int
    # interested_category_id_2: int
    # sort_option_id: int
    device: int
    # last_accessed: datetime
    # line_access_token: str
    # line_refresh_token: str
    line_id: str
    line_pic_url: str
    line_name: str
    # created_at: datetime
    # is_active: bool

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    mobile: Optional[str] = "0123456789"
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    organization: Optional[str] = None
    postal: Optional[str] = None
    pref: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    # interested_category_id_1: Optional[int] = None
    # interested_category_id_2: Optional[int] = None
    # sort_option_id: Optional[int] = None
    device: Optional[int] = None
    # last_accessed: Optional[datetime] = None
    # line_access_token: Optional[str] = None
    # line_refresh_token: Optional[str] = None
    line_id: Optional[str] = None
    line_pic_url: Optional[str] = None
    line_name: Optional[str] = None

class CreataSortOption(BaseModel):
    sort_type: str

class ShowSortOption(BaseModel):
    sort_type: str

    class Config:
        orm_mode = True

class UpdateSortOption(BaseModel):
    sort_type: Optional[str] = None