from db.repository.vendor import create_new_vendor, get_vendor_by_email, get_vendor_by_id, get_vendors
from db.session import get_db
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from schemas.vendor import VendorCreate, ShowVendor
from sqlalchemy.orm import Session
from typing import List

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