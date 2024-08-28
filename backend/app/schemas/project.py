# app/schemas/project.py

from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional

class ProjectBase(BaseModel):
    project_name: str
    account_id: UUID4
    opportunity_id: Optional[UUID4]
    profile_id: UUID4
    description: Optional[str]

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass

class ProjectInDBBase(ProjectBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Project(ProjectInDBBase):
    pass