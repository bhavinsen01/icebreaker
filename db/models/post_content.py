from db.base_class import Base
from sqlalchemy import Integer, DateTime, Boolean, ForeignKey, Column, String
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, nullable=False)
    category_id = Column(Integer, nullable=False)
    model = Column(String, nullable=False)
    name = Column(String, nullable=False)
    seo_title = Column(String, nullable=False)
    short_description = Column(String, nullable=False)
    seo_description = Column(String)
    no_price_no_stock = Column(Boolean, nullable=False)
    price = Column(Integer, nullable=False)
    sort_priority = Column(Integer, default=0)
    image = Column(String)
    content = Column(String, nullable=False)
    disabled_by_vendoer = Column(Boolean)
    disabled_by_admin = Column(Boolean)
    require_user_login = Column(Boolean)
    # vendor_member_id = Column(Integer)
    # vendor_company_id = Column(Integer)
    created_at = Column(DateTime)
    content_updated_at = Column(DateTime)
    popularity = Column(Integer)


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


class CategoryAttribute(Base):
    __tablename__ = "categoryattribute"
    id = Column(Integer, primary_key=True, index=True)
    # category_id = Column(Integer)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    sort = Column(Integer, default=0)
    option1 = Column(String, nullable=False)
    option2 = Column(String, nullable=False)
    option3 = Column(String)
    option4 = Column(String)
    option5 = Column(String)
    option6 = Column(String)
    option7 = Column(String)
    option8 = Column(String)
    option9 = Column(String)
    option10 = Column(String)
