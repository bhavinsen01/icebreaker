from db.repository.vendor import create_new_vendor
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from schemas.vendor import VendorCreate, ShowVendor
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ShowVendor)
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    vendor = create_new_vendor(vendor=vendor, db=db)
    return vendor
