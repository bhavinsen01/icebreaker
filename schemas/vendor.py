from typing import Optional
from pydantic import BaseModel
from pydantic import EmailStr
from datetime import datetime

class VendorCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    username: str
    password: str
    vendor_company_id: int
    roll:int
    created_at: datetime


class ShowVendor(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    username: str
    is_active: bool
    vendor_company_id: int
    roll:int
    created_at: datetime


    class Config:
        orm_mode = True


class UpdateVendor(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None
    vendor_company_id: Optional[int] = None
    roll: Optional[int] = None


class VendorCompanyCreate(BaseModel):
    name: str
    tel: int
    email: EmailStr
    postal: str
    pref: str
    city: str
    address: str
    line_url: str
    rating: str
    disabled: bool
    business_hours_from: str
    business_hours_to: str
    business_title: str
    busienss_description: str
    last_accessed: datetime
    created_at: datetime

class ShowVendorCompany(BaseModel):
    name: str
    tel: int
    email: EmailStr
    postal: str
    pref: str
    city: str
    address: str
    line_url: str
    rating: str
    disabled: bool
    business_hours_from: str
    business_hours_to: str
    business_title: str
    busienss_description: str
    last_accessed: datetime
    created_at: datetime

    class Config:
        orm_mode = True


class VendorCompanyUpdate(BaseModel):
    name: Optional[str] = None
    tel: Optional[int] = None
    email: Optional[EmailStr] = None
    postal: Optional[str] = None
    pref: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    line_url: Optional[str] = None
    rating: Optional[str] = None
    disabled: Optional[bool] = False
    business_hours_from: Optional[str] = None
    business_hours_to: Optional[str] = None
    business_title: Optional[str] = None
    busienss_description: Optional[str] = None
    last_accessed: Optional[datetime] = None


class CreateVendorNotification(BaseModel):
    vendor_id: int
    title: str
    notification: str
    checked: bool
    created_at: datetime
    checked_at: datetime

class ShowVendorNotification(BaseModel):
    vendor_id: int
    title: str
    notification: str
    checked: bool
    created_at: datetime
    checked_at: datetime

    class Config:
        orm_mode = True

class UpdateVendorNotification(BaseModel):
    vendor_id: Optional[int] = None
    title: Optional[str] = None
    notification: Optional[str] = None
    checked: Optional[bool] = None
    created_at: Optional[datetime] = None
    checked_at: Optional[datetime] = None