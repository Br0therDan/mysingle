# app/schemas/profile.py

from pydantic import BaseModel, UUID4, EmailStr
from datetime import datetime
from typing import Optional

class ProfileBase(BaseModel):
    username: Optional[str]
    full_name: Optional[str]
    avatar_url: Optional[str]
    website: Optional[str]
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    job_role: Optional[str]
    work_email: Optional[EmailStr]
    is_verified: bool = False
    org_id: Optional[UUID4]

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class ProfileInDBBase(ProfileBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Profile(ProfileInDBBase):
    pass