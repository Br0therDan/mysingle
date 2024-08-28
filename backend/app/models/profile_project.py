# app/models/daily_scrum.py

from sqlalchemy import Column, String, Text, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.base import Base
import uuid
from datetime import datetime

class DailyScrum(Base):
    __tablename__ = 'daily_scrums'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    scrum_date = Column(Date, nullable=False)
    summary = Column(String, nullable=True)
    sprint_id = Column(UUID(as_uuid=True), ForeignKey('sprints.id'), nullable=False)
    project_id = Column(UUID(as_uuid=True), ForeignKey('projects.id'), nullable=False)

    created_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)

    sprint = relationship("Sprint", back_populates="daily_scrums")
    project = relationship("Project", back_populates="daily_scrums")