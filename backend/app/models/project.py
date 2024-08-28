# app/models/project.py

from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.base import Base
import uuid
from datetime import datetime

class Project(Base):
    __tablename__ = 'projects'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_name = Column(String(100), nullable=False)
    account_id = Column(UUID(as_uuid=True), ForeignKey('accounts.id'), nullable=False)
    opportunity_id = Column(UUID(as_uuid=True), nullable=True)
    profile_id = Column(UUID(as_uuid=True), ForeignKey('profiles.id'), nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)

    account = relationship("Account", back_populates="projects")
    profile = relationship("Profile", back_populates="projects")
    sprints = relationship("Sprint", back_populates="project")
    daily_scrums = relationship("DailyScrum", back_populates="project")