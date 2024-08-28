# app/models/organization.py

from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.base import Base
from enum import Enum as PyEnum
import uuid
from datetime import datetime

class OrgType(PyEnum):
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"

class Organization(Base):
    __tablename__ = 'organizations'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_name = Column(String(100), nullable=True)
    org_type = Column(Enum(OrgType), nullable=False)
    created_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)

    profiles = relationship("Profile", back_populates="organization")