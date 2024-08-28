# app/models/task.py

from sqlalchemy import Column, String, Integer, Date, ForeignKey, Enum
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

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task_name = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    priority = Column(String(50), default='Low', nullable=False)
    status = Column(Enum(Status), nullable=False)
    assigned_to = Column(UUID(as_uuid=True), ForeignKey('profiles.id'), nullable=False)
    sprint_id = Column(UUID(as_uuid=True), ForeignKey('sprints.id'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)
    due_date = Column(Date, nullable=False)
    estimated_time = Column(Integer, nullable=True)
    actual_time = Column(Integer, nullable=True)
    related_task_id = Column(UUID(as_uuid=True), nullable=True)

    sprint = relationship("Sprint", back_populates="tasks")
    profile = relationship("Profile", back_populates="tasks")