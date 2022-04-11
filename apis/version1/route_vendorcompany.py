from db.repository.vendor import create_vendor_company, get_vendor_company_by_email
from db.session import get_db
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from schemas.vendor import ShowVendorCompany, VendorCompanyCreate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ShowVendorCompany)
def create_new_vendor_company(vendor_company: VendorCompanyCreate, db: Session = Depends(get_db)):
    db_user = get_vendor_company_by_email(db=db, email=vendor_company.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    vendor_company = create_vendor_company(vendor_company=vendor_company, db=db)
    return vendor_company