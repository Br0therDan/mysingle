# app/schemas/sprint.py

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

class SprintBase(BaseModel):
    sprint_name: str
    project_id: UUID4
    goal: Optional[str]
    start_date: date
    end_date: date
    status: Status = Status.IN_REVIEW
    velocity: Optional[int]
    capacity: Optional[int]
    retrospective: Optional[str]

class SprintCreate(SprintBase):
    pass

class SprintUpdate(SprintBase):
    pass

class SprintInDBBase(SprintBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Sprint(SprintInDBBase):
    pass