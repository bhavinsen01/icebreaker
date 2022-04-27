from db.base_class import Base
from sqlalchemy import Integer, DateTime, Boolean, ForeignKey, Column, String
from sqlalchemy.orm import relationship

class AdminMember(Base):
    __tablename__ = "adminmember"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    role = Column(Integer, nullable=False)


class AdminNotification(Base):
    __tablename__ = "adminnotification"
    id = Column(Integer, primary_key=True, index=True)
    admin_id = Column(Integer)
    title = Column(String, nullable=False)
    notification = Column(String, nullable=False)
    checked = Column(Boolean)
    created_at = Column(DateTime)
    checked_at = Column(DateTime)