import datetime
from db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship


class Vendor(Base):
    __tablename__ = 'vendor'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    vendor_company_id = Column(Integer, ForeignKey("vendorcompany.id"))
    roll = Column(Integer)
    created_at = Column(DateTime)
    is_active = Column(Boolean(), default=True)

    vendor = relationship("VendorCompany", back_populates="vendor_comapny")

class VendorCompany(Base):
    __tablename__ = 'vendorcompany'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    tel = Column(Integer, nullable=False)
    email = Column(String, nullable=False, unique=True)
    postal = Column(String, nullable=False)
    pref = Column(String, nullable=False)
    city = Column(String, nullable=False)
    address = Column(String)
    line_url = Column(String)
    rating = Column(String)
    disabled = Column(Boolean(), default=False)
    business_hours_from = Column(String, nullable=False)
    business_hours_to = Column(String, nullable=False)
    business_title = Column(String, nullable=False)
    busienss_description = Column(String, nullable=False)
    last_accessed = Column(DateTime, default=datetime.datetime)
    created_at = Column(DateTime)

    vendor_comapny = relationship("Vendor", back_populates="vendor")
