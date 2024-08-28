# app/models/profile.py

from sqlalchemy import Column, String, Text, Boolean, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.base import Base
import uuid
from datetime import datetime

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(UUID(as_uuid=True), primary_key=True)
    username = Column(Text, nullable=True, unique=True)
    full_name = Column(Text, nullable=True)
    avatar_url = Column(Text, nullable=True)
    website = Column(Text, nullable=True)
    email = Column(String(50), nullable=False)
    first_name = Column(String(30), nullable=True)
    last_name = Column(String(30), nullable=True)
    job_role = Column(String(30), nullable=True)
    work_email = Column(String(50), nullable=True)
    is_verified = Column(Boolean, default=False, nullable=False)
    created_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)
    org_id = Column(UUID(as_uuid=True), nullable=True)

    accounts = relationship("Account", back_populates="profile")
    contacts = relationship("Contact", back_populates="profile")
    opportunities = relationship("Opportunity", back_populates="profile")