# app/schemas/opportunity.py

from pydantic import BaseModel, UUID4
from datetime import datetime, date
from typing import Optional
from enum import Enum

class OpportunityStage(str, Enum):
    _1_OPPORTUNITY = "1 _OPPORTUNITY"
    _2_DISCOVERY = "2_DISCOVERY"
    _3_OBJECTIVES = "3_OBJECTIVES"
    _4_PRESENT_SOLUTION = "4_PRESENT_SOLUTION"
    _4_ECONOMIC_BUYER_IDNETIFIED = "4_ECONOMIC_BUYER_IDNETIFIED"
    _5_ECONOMIC_BUYER_VALIDATION = "5_ECONOMIC_BUYER_VALIDATION"
    _6_VALIDATION_COMPLETED = "6_VALIDATION_COMPLETED"
    _7_DEAL_IMMINENT = "7_DEAL_IMMINENT"
    _8_CLOSED_LOST = "8_CLOSED_LOST"
    _8_CLOSED_NO_DECISION = "8_CLOSED_NO_DECISION"
    _9_CLOSED_WON = "9_CLOSED_WON"

class ForecastCategory(str, Enum):
    PIPELINE = "PIPELINE"
    UPSIDE = "UPSIDE"
    EXPECT = "EXPECT"
    COMMIT = "COMMIT"
    CLOSED = "CLOSED"

class OpportunityType(str, Enum):
    NEW_BUSINESS = "NEW_BUSINESS"
    UPSELL = "UPSELL"
    RENEWAL = "RENEWAL"

class OpportunityBase(BaseModel):
    opportunity_name: str
    close_date: date
    net_new_acv: float
    account_id: UUID4
    stage: OpportunityStage = OpportunityStage._1_OPPORTUNITY
    forecast_category: ForecastCategory = ForecastCategory.PIPELINE
    opportunity_summary: Optional[str]
    currency_code: str
    profile_id: UUID4
    opportunity_type: Optional[OpportunityType] = OpportunityType.NEW_BUSINESS
    opportunity_contact: Optional[str]
    partner: Optional[str]

class OpportunityCreate(OpportunityBase):
    pass

class OpportunityUpdate(OpportunityBase):
    pass

class OpportunityInDBBase(OpportunityBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Opportunity(OpportunityInDBBase):
    pass