# app/schemas/daily_scrum.py

from pydantic import BaseModel, UUID4
from datetime import datetime, date
from typing import Optional

class DailyScrumBase(BaseModel):
    scrum_date: date
    summary: Optional[str]
    sprint_id: UUID4
    project_id: UUID4

class DailyScrumCreate(DailyScrumBase):
    pass

class DailyScrumUpdate(DailyScrumBase):
    pass

class DailyScrumInDBBase(DailyScrumBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class DailyScrum(DailyScrumInDBBase):
    pass