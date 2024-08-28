# app/schemas/contact.py

from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional

class ContactBase(BaseModel):
    full_name: Optional[str]
    mobile_phone: Optional[str]
    email: Optional[str]
    account_id: Optional[UUID4]
    profile_id: Optional[UUID4]
    address: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    job_level: Optional[str]
    job_type: Optional[str]
    job_role: Optional[str]
    reporting_manager: Optional[UUID4]
    relationship_strength: Optional[str]
    business_phone: Optional[str]

class ContactCreate(ContactBase):
    pass

class ContactUpdate(ContactBase):
    pass

class ContactInDBBase(ContactBase):
    id: UUID4
    created_at: datetime

    class Config:
        orm_mode = True

class Contact(ContactInDBBase):
    pass