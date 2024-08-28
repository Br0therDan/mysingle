# app/schemas/account.py

from pydantic import BaseModel, UUID4, Field
from datetime import datetime
from typing import Optional
from enum import Enum

class AccountType(str, Enum):
    PROSPECT = "PROSPECT"
    CUSTOMER = "CUSTOMER"
    PARTNER = "PARTNER"
    INACTIVE = "INACTIVE"

class AccountSegment(str, Enum):
    ENTERPRISE = "ENTERPRISE"
    CORPORATE = "CORPORATE"
    SMB = "SMB"
    STARTUP = "STARTUP"
    GOVERNMENT = "GOVERNMENT"
    NON_PROFIT = "NON PROFIT"

class AccountBase(BaseModel):
    account_name: str
    profile_id: Optional[UUID4]
    account_type: AccountType = AccountType.PROSPECT
    total_acv: int = 0
    number_of_employee: Optional[int]
    segment: Optional[AccountSegment] = AccountSegment.ENTERPRISE
    parent_account_id: Optional[UUID4]
    country_id: Optional[int]

class AccountCreate(AccountBase):
    pass

class AccountUpdate(AccountBase):
    pass

class AccountInDBBase(AccountBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Account(AccountInDBBase):
    pass