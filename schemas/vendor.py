from typing import Optional
from pydantic import BaseModel
from pydantic import EmailStr


class VendorCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    company_id: int
    roll:int


class ShowVendor(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    is_active: bool
    company_id: int
    roll:int


    class Config:
        orm_mode = True


class UpdateVendor(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    company_id: Optional[int] = None
    roll: Optional[int] = None


class VendorCompanyCreate(BaseModel):
    company_name: str
    tel: int
    email: EmailStr
    postal: int
    pref: str
    city: str
    address: str
    contact1: str
    contact2: str
    contact3: str
    classification1: int

class ShowVendorCompany(BaseModel):
    company_name: str
    tel: int
    email: EmailStr
    postal: int
    pref: str
    city: str
    address: str
    contact1: str
    contact2: str
    contact3: str
    classification1: int

    class Config:
        orm_mode = True


class VendorCompanyUpdate(BaseModel):
    company_name: Optional[str] = None
    tel: Optional[int] = None
    email: Optional[EmailStr] = None
    postal: Optional[int] = None
    pref: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    contact1: Optional[str] = None
    contact2: Optional[str] = None
    contact3: Optional[str] = None
    classification1: Optional[int] = None