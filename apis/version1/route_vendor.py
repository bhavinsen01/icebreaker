from db.repository.vendor import create_new_vendor, get_vendor_by_company_id, get_vendor_by_email, get_vendor_by_id, get_vendors, create_vendor_notification, get_vendor_notification_by_id, get_vendor_notifications, get_vendor_by_username
from db.session import get_db, engine
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from schemas.vendor import VendorCreate, ShowVendor, UpdateVendor, CreateVendorNotification, ShowVendorNotification, UpdateVendorNotification
from sqlalchemy.orm import Session
from typing import List
from db.models.vendor import Vendor, VendorNotification

router = APIRouter()


# <-----------------------------VENDOR MEMBER----------------------------->

@router.post("/", response_model=ShowVendor)
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    db_vendor = get_vendor_by_email(db=db, email=vendor.email)
    if db_vendor:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_vendor_username = get_vendor_by_username(db=db, username=vendor.username)
    if db_vendor_username:
        raise HTTPException(status_code=400, detail="Username already registered")
    # db_vendor_company_id = get_vendor_by_company_id(db=db, vendor_company_id=vendor.vendor_company_id)
    # if db_vendor_company_id:
    #     raise HTTPException(status_code=400, detail="Comapny ID already registered")
    # else:
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
def update_vendor(vendor_id: int, vendor: UpdateVendor, db: Session = Depends(get_db)):
    with Session(engine) as session:
        db_vendor = get_vendor_by_email(db=db, email=vendor.email)
        if db_vendor:
            raise HTTPException(status_code=400, detail="Email already registered")
        db_vendor_username = get_vendor_by_username(db=db, username=vendor.username)
        if db_vendor_username:
            raise HTTPException(status_code=400, detail="Username already registered")
        else:
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


# <-----------------------------VENDOR NOTIFICATION----------------------------->

@router.post("/notification", response_model=ShowVendorNotification)
def create_vendor_notifications(vendor_notification: CreateVendorNotification, db: Session = Depends(get_db)):
    db_vendor_notification = create_vendor_notification(vendor_notification=vendor_notification, db=db)
    return db_vendor_notification

@router.get("/notification/{vendor_notification_id}", response_model=ShowVendorNotification)
def read_vendor_notification(vendor_notification_id: int, db: Session = Depends(get_db)):
    db_vendor_notification = get_vendor_notification_by_id(vendor_notification_id=vendor_notification_id, db=db)
    if db_vendor_notification is None:
        raise HTTPException(status_code=404, detail="Vendor Notification not found")
    return db_vendor_notification

@router.get("/notification/allnotifications/", response_model=List[ShowVendorNotification])
def read_vendor_notifications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vendor_notifications = get_vendor_notifications(db, skip=skip, limit=limit)
    return vendor_notifications

@router.patch("/notification/{vendor_notification_id}", response_model=ShowVendorNotification)
def update_vendor_notification(vendor_notification_id: int, vendor_notification: UpdateVendorNotification):
    with Session(engine) as session:
        db_vendor_notification = session.get(VendorNotification, vendor_notification_id)
        if not db_vendor_notification:
            raise HTTPException(status_code=404, detail="Vendor Notification not found")
        vendor_notification_update = vendor_notification.dict(exclude_unset=True)
        for key, value in vendor_notification_update.items():
            setattr(db_vendor_notification, key, value)
        session.add(db_vendor_notification)
        session.commit()
        session.refresh(db_vendor_notification)
        return db_vendor_notification

@router.delete("/notification/delete/{vendor_notification_id}")
def delete_vendor_notification(vendor_notification_id: int):
    with Session(engine) as session:
        vendor_notification = session.get(VendorNotification, vendor_notification_id)
        if not vendor_notification:
            raise HTTPException(status_code=404, detail="Vendor Notification not found")
        session.delete(vendor_notification)
        session.commit()
        return {"Vendor Member": "Vendor Notification Deleted Successfully"}