from pydantic import BaseModel, HttpUrl


class PostCreate(BaseModel):
    sku: str
    url: HttpUrl
    service_name: str
    service_short_description: str
    price: int
    availibility: str
    post_category: str

class SubCategories(BaseModel):
    sub_category_title: str