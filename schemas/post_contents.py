from datetime import datetime
from typing import List, Optional
from fastapi import UploadFile
from pydantic import BaseModel


class CreateProduct(BaseModel):
    sku: str
    category_id: int
    model: str
    name: str
    seo_title: str
    short_description: str
    seo_description: Optional[str] = None
    no_price_no_stock: bool
    price: int
    sort_priority: Optional[int] = 0
    content: str
    disabled_by_vendoer: Optional[bool] = None
    disabled_by_admin: Optional[bool] = None
    require_user_login: Optional[bool] = None
    # vendor_member_id: int
    # vendor_company_id: int
    created_at: datetime
    content_updated_at: datetime 
    popularity: int

class UploadImages(BaseModel):
    image: UploadFile

class UpdateProduct(BaseModel):
    sku: str
    category_id: int
    model: str
    name: str
    seo_title: str
    short_description: str
    seo_description: Optional[str] = None
    no_price_no_stock: bool
    price: int
    sort_priority: Optional[int] = 0
    content: str
    disabled_by_vendoer: Optional[bool] = None
    disabled_by_admin: Optional[bool] = None
    require_user_login: Optional[bool] = None
    # vendor_member_id: int
    # vendor_company_id: int
    created_at: datetime
    content_updated_at: datetime 
    popularity: int
    # image: UploadImages

class CreateCategory(BaseModel):
    name: str

class ShowCategory(BaseModel):
    name: str

    class Config:
        orm_mode = True

class UpdateCategory(BaseModel):
    name: Optional[str] = None

class CreateCategoryAttribute(BaseModel):
    category_id: int
    title: str
    description: str
    sort: int = 0
    option1: str
    option2: str
    option3: Optional[str] = None
    option4: Optional[str] = None
    option5: Optional[str] = None
    option6: Optional[str] = None
    option7: Optional[str] = None
    option8: Optional[str] = None
    option9: Optional[str] = None
    option10: Optional[str] = None

class ShowCategoryAttribute(BaseModel):
    # category_id: int
    title: str
    description: str
    sort: int = 0
    option1: str
    option2: str
    option3: Optional[str] = None
    option4: Optional[str] = None
    option5: Optional[str] = None
    option6: Optional[str] = None
    option7: Optional[str] = None
    option8: Optional[str] = None
    option9: Optional[str] = None
    option10: Optional[str] = None

    class Config:
        orm_mode = True

class UpdateCategoryAttribute(BaseModel):
    # category_id: int
    title: Optional[str] = None
    description: Optional[str] = None
    sort: Optional[int] = 0
    option1: Optional[str] = None
    option2: Optional[str] = None
    option3: Optional[str] = None
    option4: Optional[str] = None
    option5: Optional[str] = None
    option6: Optional[str] = None
    option7: Optional[str] = None
    option8: Optional[str] = None
    option9: Optional[str] = None
    option10: Optional[str] = None
