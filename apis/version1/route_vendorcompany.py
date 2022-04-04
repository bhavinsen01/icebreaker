from db.repository.vendor import create_vendor_company
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from schemas.vendor import ShowVendorCompany, VendorCompanyCreate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ShowVendorCompany)
def create_new_vendor_company(vendor_company: VendorCompanyCreate, db: Session = Depends(get_db)):
    vendor_company = create_vendor_company(vendor_company=vendor_company, db=db)
    return vendor_company