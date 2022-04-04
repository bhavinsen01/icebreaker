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
