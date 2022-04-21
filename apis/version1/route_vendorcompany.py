from db.repository.vendor import create_vendor_company, get_vendor_company_by_email, get_vendor_company_by_id, get_vendor_companies
from db.session import get_db
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from schemas.vendor import ShowVendorCompany, VendorCompanyCreate
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()


@router.post("/", response_model=ShowVendorCompany)
def create_new_vendor_company(vendor_company: VendorCompanyCreate, db: Session = Depends(get_db)):
    db_user = get_vendor_company_by_email(db=db, email=vendor_company.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    vendor_company = create_vendor_company(vendor_company=vendor_company, db=db)
    return vendor_company

@router.get("/{vendor_company_id}", response_model=ShowVendorCompany)
def read_vendor_comapny(vendor_company_id: int, db: Session = Depends(get_db)):
    db_vendor_company = get_vendor_company_by_id(vendor_company_id=vendor_company_id, db=db)
    if db_vendor_company is None:
        raise HTTPException(status_code=404, detail="Vendor Company not found")
    return db_vendor_company

@router.get("/allvendorcompany/", response_model=List[ShowVendorCompany])
def read_vendor_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    company = get_vendor_companies(db, skip=skip, limit=limit)
    return company