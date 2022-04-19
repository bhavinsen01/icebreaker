from db.base_class import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

class PostContents(Base):
    __tablename__ = 'postcontents'
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String)
    url = Column(String)
    service_name = Column(String)
    service_short_description = Column(String)
    price = Column(Integer)
    availibility = Column(String)
    post_category = Column(String, ForeignKey("subcategory.id"))

    post = relationship("SubCategory", back_populates="sub_category_relation")


class SubCategory(Base):
    __tablename__ = 'subcategory'
    id = Column(Integer, primary_key=True, index=True)
    sub_category_name = Column(String)

    sub_category_relation = relationship("PostContents", back_populates="post")
