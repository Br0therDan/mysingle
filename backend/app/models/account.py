# app/models/account.py

from sqlalchemy import Column, String, BigInteger, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.base import Base
from enum import Enum as PyEnum
import uuid
from datetime import datetime

class AccountType(PyEnum):
    PROSPECT = "PROSPECT"
    CUSTOMER = "CUSTOMER"
    PARTNER = "PARTNER"
    INACTIVE = "INACTIVE"

class AccountSegment(PyEnum):
    ENTERPRISE = "ENTERPRISE"
    CORPORATE = "CORPORATE"
    SMB = "SMB"
    STARTUP = "STARTUP"
    GOVERNMENT = "GOVERNMENT"
    NON_PROFIT = "NON PROFIT"

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    account_name = Column(String(100), nullable=False)
    profile_id = Column(UUID(as_uuid=True), ForeignKey('profiles.id'), nullable=True)
    created_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)
    account_type = Column(Enum(AccountType), default=AccountType.PROSPECT, nullable=False)
    total_acv = Column(BigInteger, default=0)
    number_of_employee = Column(BigInteger, nullable=True)
    segment = Column(Enum(AccountSegment), default=AccountSegment.ENTERPRISE, nullable=True)
    parent_account_id = Column(UUID(as_uuid=True), nullable=True)
    country_id = Column(BigInteger, nullable=True)
    
    profile = relationship("Profile", back_populates="accounts")
    opportunities = relationship("Opportunity", back_populates="account")
    projects = relationship("Project", back_populates="account")