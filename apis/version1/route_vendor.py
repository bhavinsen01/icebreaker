from db.repository.vendor import create_new_vendor, get_vendor_by_email
from db.session import get_db
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from schemas.vendor import VendorCreate, ShowVendor
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ShowVendor)
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    db_user = get_vendor_by_email(db=db, email=vendor.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    vendor = create_new_vendor(vendor=vendor, db=db)
    return vendor
