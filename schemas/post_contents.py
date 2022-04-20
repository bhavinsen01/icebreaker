from datetime import datetime
from fastapi import UploadFile
from pydantic import BaseModel


class CreateProduct(BaseModel):
    sku: str
    category_id: int
    model: str
    name: str
    seo_title: str
    short_description: str
    seo_description: str
    no_price_no_stock: bool
    price: int
    sort_priority: int = 0
    content: str
    disabled_by_vendoer: bool
    disabled_by_admin: bool
    require_user_login: bool
    # vendor_member_id: int
    # vendor_company_id: int
    created_at: datetime
    content_updated_at: datetime
    popularity: int

# class UploadImages(BaseModel):
#     image: UploadFile
