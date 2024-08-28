from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date
import uuid

class DailyScrum(SQLModel, table=True):
    __tablename__ = "daily_scrums"
    daily_scrum_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    scrum_date: date
    summary: Optional[str]
    sprint_id: uuid.UUID = Field(foreign_key="sprints.sprint_id")
    project_id: uuid.UUID = Field(foreign_key="projects.project_id")
