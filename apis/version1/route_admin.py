from typing import List
from fastapi import APIRouter, HTTPException, Depends
from db.repository.admin import create_adamin_member, create_admin_notification, get_admin_by_id, get_admin_members, get_admin_notification_by_id, get_admin_notifications
from db.session import get_db, engine
from db.models.admin import AdminMember, AdminNotification
from sqlalchemy.orm import Session
from schemas.admin import CreateAdminMember, ShowAdminMember, UpdateAdminMember, CreateAdminNotification, ShowAdminNotification, UpdateAdminNotification


router = APIRouter()


# <-----------------------------ADMIN MEMBER----------------------------->

@router.post("/", response_model=ShowAdminMember)
def create_admin(admin: CreateAdminMember, db: Session = Depends(get_db)):
    db_admin = create_adamin_member(admin=admin, db=db)
    return db_admin

@router.get("/{admin_member_id}", response_model=ShowAdminMember)
def read_admin_member(admin_member_id: int, db: Session = Depends(get_db)):
    db_admin_member = get_admin_by_id(admin_member_id=admin_member_id, db=db)
    if db_admin_member is None:
        raise HTTPException(status_code=404, detail="Admin Member not found")
    return db_admin_member

@router.get("/allmembers/", response_model=List[ShowAdminMember])
def read_admin_members(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    admin_members = get_admin_members(db, skip=skip, limit=limit)
    return admin_members

@router.patch("/{admin_member_id}", response_model=ShowAdminMember)
def update_admin_member(admin_member_id: int, admin: UpdateAdminMember):
    with Session(engine) as session:
        db_admin = session.get(AdminMember, admin_member_id)
        if not db_admin:
            raise HTTPException(status_code=404, detail="Admin Member not found")
        admin_member_update = admin.dict(exclude_unset=True)
        for key, value in admin_member_update.items():
            setattr(db_admin, key, value)
        session.add(db_admin)
        session.commit()
        session.refresh(db_admin)
        return db_admin

@router.delete("/delete/{admin_member_id}")
def delete_admin_member(admin_member_id: int):
    with Session(engine) as session:
        admin_member = session.get(AdminMember, admin_member_id)
        if not admin_member:
            raise HTTPException(status_code=404, detail="Admin Member not found")
        session.delete(admin_member)
        session.commit()
        return {"Admin Member": "Admin Member Deleted Successfully"}


# <-----------------------------ADMIN NOTIFICATION----------------------------->

@router.post("/notification", response_model=ShowAdminNotification)
def create_notification(admin_notification: CreateAdminNotification, db: Session = Depends(get_db)):
    db_admin_notification = create_admin_notification(admin_notification=admin_notification, db=db)
    return db_admin_notification

@router.get("/notification/{admin_notification_id}", response_model=ShowAdminNotification)
def read_admin_notification(admin_notification_id: int, db: Session = Depends(get_db)):
    db_admin_notification = get_admin_notification_by_id(admin_notification_id=admin_notification_id, db=db)
    if db_admin_notification is None:
        raise HTTPException(status_code=404, detail="Admin Notification not found")
    return db_admin_notification

@router.get("/notification/allnotifications/", response_model=List[ShowAdminNotification])
def read_admin_notifications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    admin_notifications = get_admin_notifications(db, skip=skip, limit=limit)
    return admin_notifications

@router.patch("/notification/{admin_notification_id}", response_model=ShowAdminNotification)
def update_admin_notification(admin_notification_id: int, admin_notification: UpdateAdminNotification):
    with Session(engine) as session:
        db_admin_notification = session.get(AdminNotification, admin_notification_id)
        if not db_admin_notification:
            raise HTTPException(status_code=404, detail="Admin Notification not found")
        admin_notification_update = admin_notification.dict(exclude_unset=True)
        for key, value in admin_notification_update.items():
            setattr(db_admin_notification, key, value)
        session.add(db_admin_notification)
        session.commit()
        session.refresh(db_admin_notification)
        return db_admin_notification

@router.delete("/notification/delete/{admin_notification_id}")
def delete_admin_notification(admin_notification_id: int):
    with Session(engine) as session:
        admin_notification = session.get(AdminNotification, admin_notification_id)
        if not admin_notification:
            raise HTTPException(status_code=404, detail="Admin Notification not found")
        session.delete(admin_notification)
        session.commit()
        return {"Admin Notification": "Admin Notification Deleted Successfully"}