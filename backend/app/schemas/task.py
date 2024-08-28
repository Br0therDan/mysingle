# app/schemas/task.py

from pydantic import BaseModel, UUID4
from datetime import datetime, date
from typing import Optional
from enum import Enum

class Status(str, Enum):
    IN_REVIEW = "IN_REVIEW"
    PLANNED = "PLANNED"
    SCHEDULED = "SCHEDULED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    BLOCKED = "BLOCKED"
    ON_HOLD = "ON_HOLD"

class TaskBase(BaseModel):
    task_name: str
    description: Optional[str]
    priority: str = 'Low'
    status: Status
    assigned_to: UUID4
    sprint_id: UUID4
    due_date: date
    estimated_time: Optional[int]
    actual_time: Optional[int]
    related_task_id: Optional[UUID4]

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskInDBBase(TaskBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Task(TaskInDBBase):
    pass