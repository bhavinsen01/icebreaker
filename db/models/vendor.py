from db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class Vendor(Base):
    __tablename__ = 'vendor'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey("vendorcompany.id"))
    roll = Column(Integer)
    is_active = Column(Boolean(), default=True)

    vendor = relationship("VendorCompany", back_populates="vendor_comapny")

class VendorCompany(Base):
    __tablename__ = 'vendorcompany'
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    tel = Column(Integer, nullable=False)
    email = Column(String, nullable=False, unique=True)
    postal = Column(Integer, nullable=False)
    pref = Column(String, nullable=False)
    city = Column(String, nullable=False)
    address = Column(String)
    contact1 = Column(String)
    contact2 = Column(String)
    contact3 = Column(String)
    classification1 = Column(Integer)

    vendor_comapny = relationship("Vendor", back_populates="vendor")
