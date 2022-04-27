from db.models.admin import AdminMember, AdminNotification
from schemas.admin import CreateAdminMember, CreateAdminNotification
from sqlalchemy.orm import Session

def create_adamin_member(admin: CreateAdminMember, db:Session):
    admin = AdminMember(
        first_name = admin.first_name,
        last_name = admin.last_name,
        role = admin.role
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin

def get_admin_by_id(admin_member_id: int, db: Session):
    return db.query(AdminMember).filter(AdminMember.id == admin_member_id).first()

def get_admin_members(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AdminMember).offset(skip).limit(limit).all()


def create_admin_notification(admin_notification: CreateAdminNotification, db: Session):
    admin_notification = AdminNotification(
        admin_id= admin_notification.admin_id,
        title = admin_notification.title,
        notification = admin_notification.notification,
        checked = admin_notification.checked,
        created_at = admin_notification.created_at,
        checked_at = admin_notification.checked_at
    )
    db.add(admin_notification)
    db.commit()
    db.refresh(admin_notification)
    return admin_notification

def get_admin_notification_by_id(admin_notification_id: int, db:Session):
    return db.query(AdminNotification).filter(AdminNotification.id == admin_notification_id).first()

def get_admin_notifications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AdminNotification).offset(skip).limit(limit).all()