# app/models/sprint.py

from sqlalchemy import Column, String, Text, Date, Integer, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.base import Base
from enum import Enum as PyEnum
import uuid
from datetime import datetime

class Status(PyEnum):
    IN_REVIEW = "IN_REVIEW"
    PLANNED = "PLANNED"
    SCHEDULED = "SCHEDULED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    BLOCKED = "BLOCKED"
    ON_HOLD = "ON_HOLD"

class Sprint(Base):
    __tablename__ = 'sprints'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sprint_name = Column(String(100), nullable=False)
    project_id = Column(UUID(as_uuid=True), ForeignKey('projects.id'), nullable=False)
    goal = Column(String(150), nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status = Column(Enum(Status), default=Status.IN_REVIEW, nullable=False)
    created_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)
    velocity = Column(Integer, nullable=True)
    capacity = Column(Integer, nullable=True)
    retrospective = Column(Text, nullable=True)

    project = relationship("Project", back_populates="sprints")
    daily_scrums = relationship("DailyScrum", back_populates="sprint")