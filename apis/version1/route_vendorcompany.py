from db.repository.vendor import create_vendor_company, get_vendor_company_by_email, get_vendor_company_by_id, get_vendor_companies
from db.session import get_db, engine
from db.models.vendor import VendorCompany
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from schemas.vendor import ShowVendorCompany, VendorCompanyCreate, VendorCompanyUpdate
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

@router.patch("/company/{vendor_company_id}", response_model=ShowVendorCompany)
def update_vendor(vendor_company_id: int, vendor_company: VendorCompanyUpdate):
    with Session(engine) as session:
        db_company = session.get(VendorCompany, vendor_company_id)
        if not db_company:
            raise HTTPException(status_code=404, detail="Vendor not found")
        company_update = vendor_company.dict(exclude_unset=True)
        for key, value in company_update.items():
            setattr(db_company, key, value)
        session.add(db_company)
        session.commit()
        session.refresh(db_company)
        return db_company

@router.delete("/delete/{vendor_company_id}")
def delete_vendor_comapny(vendor_company_id: int):
    with Session(engine) as session:
        vendor_company = session.get(VendorCompany, vendor_company_id)
        if not vendor_company:
            raise HTTPException(status_code=404, detail="Vendor Company not found")
        session.delete(vendor_company)
        session.commit()
        return {"Vendor": "Vendor Company Deleted Successfully"}