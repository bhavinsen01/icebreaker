from db.repository.vendor import create_new_vendor, get_vendor_by_email, get_vendor_by_id, get_vendors
from db.session import get_db, engine
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from schemas.vendor import VendorCreate, ShowVendor, UpdateVendor
from sqlalchemy.orm import Session
from typing import List
from db.models.vendor import Vendor

router = APIRouter()


@router.post("/", response_model=ShowVendor)
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    db_user = get_vendor_by_email(db=db, email=vendor.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    vendor = create_new_vendor(vendor=vendor, db=db)
    return vendor


@router.get("/{vendor_id}", response_model=ShowVendor)
def read_vendor(vendor_id: int, db: Session = Depends(get_db)):
    db_vendor = get_vendor_by_id(vendor_id=vendor_id, db=db)
    if db_vendor is None:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return db_vendor

@router.get("/allvendor/", response_model=List[ShowVendor])
def read_vendors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vendors = get_vendors(db, skip=skip, limit=limit)
    return vendors

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

@router.delete("/delete/{vendor_id}")
def delete_vendor(vendor_id: int):
    with Session(engine) as session:
        vendor = session.get(Vendor, vendor_id)
        if not vendor:
            raise HTTPException(status_code=404, detail="Vendor not found")
        session.delete(vendor)
        session.commit()
        return {"Vendor": "Vendor Deleted Successfully"}