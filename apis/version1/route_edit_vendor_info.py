from db.models.vendor import Vendor, VendorCompany
from fastapi import APIRouter
from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.vendor import ShowVendor, ShowVendorCompany, VendorCompanyUpdate, UpdateVendor
from db.session import engine


router = APIRouter()


@router.patch("/{vendor_id}", response_model=ShowVendor)
def update_vendor(vendor_id: int, vendor: UpdateVendor):
    with Session(engine) as session:
        db_vendor = session.get(Vendor, vendor_id)
        if not db_vendor:
            raise HTTPException(status_code=404, detail="Vendor not found")
        vendor_update = vendor.dict(exclude_unset=True)
        for key, value in vendor_update.items():
            setattr(db_vendor, key, value)
        session.add(db_vendor)
        session.commit()
        session.refresh(db_vendor)
        return db_vendor


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