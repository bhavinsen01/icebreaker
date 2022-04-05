from typing import Optional
from pydantic import BaseModel
from pydantic import EmailStr


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    mobile: str
    username: str
    email: EmailStr
    password: str
    organization: str


class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    organization: str
    first_name: str
    last_name: str
    mobile: str

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    mobile: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    organization: Optional[str] = None