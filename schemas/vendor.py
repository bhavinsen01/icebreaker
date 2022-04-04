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


class VendorCompanyCreate(BaseModel):
    company_name: str
    tel: int
    email: str
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
    email: str
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