# app/models/opportunity.py

from sqlalchemy import Column, String, Text, ForeignKey, Enum, Float, Date
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.base import Base
from enum import Enum as PyEnum
import uuid
from datetime import datetime

class OpportunityStage(PyEnum):
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

class ForecastCategory(PyEnum):
    PIPELINE = "PIPELINE"
    UPSIDE = "UPSIDE"
    EXPECT = "EXPECT"
    COMMIT = "COMMIT"
    CLOSED = "CLOSED"

class OpportunityType(PyEnum):
    NEW_BUSINESS = "NEW_BUSINESS"
    UPSELL = "UPSELL"
    RENEWAL = "RENEWAL"

class Opportunity(Base):
    __tablename__ = 'opportunities'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    opportunity_name = Column(String(100), nullable=False)
    close_date = Column(Date, nullable=False)
    net_new_acv = Column(Float, nullable=False)
    account_id = Column(UUID(as_uuid=True), ForeignKey('accounts.id'), nullable=False)
    stage = Column(Enum(OpportunityStage), default=OpportunityStage._1_OPPORTUNITY, nullable=False)
    forecast_category = Column(Enum(ForecastCategory), default=ForecastCategory.PIPELINE, nullable=False)
    opportunity_summary = Column(Text, nullable=True)
    currency_code = Column(String(3), nullable=False)
    created_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow, nullable=False)
    profile_id = Column(UUID(as_uuid=True), ForeignKey('profiles.id'), nullable=False)
    opportunity_type = Column(Enum(OpportunityType), default=OpportunityType.NEW_BUSINESS, nullable=True)
    opportunity_contact = Column(Text, nullable=True)
    partner = Column(Text, nullable=True)

    account = relationship("Account", back_populates="opportunities")
    profile = relationship("Profile", back_populates="opportunities")