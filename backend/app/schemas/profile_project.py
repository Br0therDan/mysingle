# app/schemas/profile_project.py

from pydantic import BaseModel, UUID4
from datetime import datetime

class ProfileProjectBase(BaseModel):
    profile_id: UUID4
    project_id: UUID4
    role: Optional[str]

class ProfileProjectCreate(ProfileProjectBase):
    pass

class ProfileProjectUpdate(ProfileProjectBase):
    pass

class ProfileProjectInDBBase(ProfileProjectBase):
    joined_at: datetime

    class Config:
        orm_mode = True

class ProfileProject(ProfileProjectInDBBase):
    pass