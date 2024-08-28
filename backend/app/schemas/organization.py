# app/schemas/organization.py

from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional
from enum import Enum

class OrgType(str, Enum):
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"

class OrganizationBase(BaseModel):
    org_name: Optional[str]
    org_type: OrgType

class OrganizationCreate(OrganizationBase):
    pass

class OrganizationUpdate(OrganizationBase):
    pass

class OrganizationInDBBase(OrganizationBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Organization(OrganizationInDBBase):
    pass