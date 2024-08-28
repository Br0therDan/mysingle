# app/models/contact.py

from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.base import Base
import uuid
from datetime import datetime

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow, nullable=False)
    full_name = Column(String, nullable=True)
    mobile_phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    account_id = Column(UUID(as_uuid=True), ForeignKey('accounts.id'), nullable=True)
    profile_id = Column(UUID(as_uuid=True), ForeignKey('profiles.id'), nullable=True)
    address = Column(Text, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    job_level = Column(Text, nullable=True)
    job_type = Column(Text, nullable=True)
    job_role = Column(Text, nullable=True)
    reporting_manager = Column(UUID(as_uuid=True), nullable=True)
    relationship_strength = Column(Text, nullable=True)
    business_phone = Column(String, nullable=True)

    account = relationship("Account", back_populates="contacts")
    profile = relationship("Profile", back_populates="contacts")