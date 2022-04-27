from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class CreateAdminMember(BaseModel):
    first_name: str
    last_name: str
    role: int

class ShowAdminMember(BaseModel):
    first_name: str
    last_name: str
    role: int

    class Config:
        orm_mode = True 

class UpdateAdminMember(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[int] = None


class CreateAdminNotification(BaseModel):
    admin_id: int
    title: str
    notification: str
    checked: bool
    created_at: datetime
    checked_at: datetime

class ShowAdminNotification(BaseModel):
    admin_id: int
    title: str
    notification: str
    checked: bool
    created_at: datetime
    checked_at: datetime

    class Config:
        orm_mode = True

class UpdateAdminNotification(BaseModel):
    admin_id: Optional[int] = None
    title: Optional[str] = None
    notification: Optional[str] = None
    checked: Optional[bool] = None
    created_at: Optional[datetime] = None
    checked_at: Optional[datetime] = None