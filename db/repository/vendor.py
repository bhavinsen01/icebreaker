from core.hashing import Hasher
from db.models.vendor import Vendor, VendorCompany
from schemas.vendor import VendorCreate, VendorCompanyCreate
from sqlalchemy.orm import Session


def create_new_vendor(vendor: VendorCreate, db: Session):
    vendor = Vendor(
        first_name = vendor.first_name,
        last_name = vendor.last_name,
        email = vendor.email,
        username = vendor.username,
        hashed_password=Hasher.get_password_hash(vendor.password),
        vendor_company_id = vendor.vendor_company_id,
        roll = vendor.roll,
        created_at= vendor.created_at,
        is_active = True
    )
    db.add(vendor)
    db.commit()
    db.refresh(vendor)
    return vendor

def get_vendor_by_email(db: Session, email: str):
    return db.query(Vendor).filter(Vendor.email == email).first()

def get_vendor_by_id(vendor_id: int, db: Session):
    return db.query(Vendor).filter(Vendor.id == vendor_id).first()

def get_vendors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Vendor).offset(skip).limit(limit).all()

def create_vendor_company(vendor_company: VendorCompanyCreate, db:Session):
    vendor_company = VendorCompany(
        name = vendor_company.name,
        tel = vendor_company.tel,
        email = vendor_company.email,
        postal = vendor_company.postal,
        pref = vendor_company.pref,
        city = vendor_company.city,
        address = vendor_company.address,
        line_url = vendor_company.line_url,
        rating = vendor_company.rating,
        disabled = vendor_company.disabled,
        business_hours_from = vendor_company.business_hours_from,
        business_hours_to = vendor_company.business_hours_to,
        business_title = vendor_company.business_title,
        busienss_description = vendor_company.busienss_description,
        last_accessed = vendor_company.last_accessed,
        created_at = vendor_company.created_at
    )
    db.add(vendor_company)
    db.commit()
    db.refresh(vendor_company)
    return vendor_company

def get_vendor_company_by_email(db: Session, email: str):
    return db.query(VendorCompany).filter(VendorCompany.email == email).first() 

def get_vendor(username: str, db: Session):
    user = db.query(Vendor).filter(Vendor.username == username).first()
    return user

def get_vendor_company_by_id(vendor_company_id: int, db: Session):
    return db.query(VendorCompany).filter(VendorCompany.id == vendor_company_id).first()

def get_vendor_companies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(VendorCompany).offset(skip).limit(limit).all()