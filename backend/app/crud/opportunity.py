# app/crud/opportunity.py

from sqlalchemy.orm import Session
from app.models.opportunity import Opportunity
from app.schemas.opportunity import OpportunityCreate, OpportunityUpdate

def get_opportunity(db: Session, opportunity_id: str):
    return db.query(Opportunity).filter(Opportunity.id == opportunity_id).first()

def get_opportunities(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Opportunity).offset(skip).limit(limit).all()

def create_opportunity(db: Session, opportunity: OpportunityCreate):
    db_opportunity = Opportunity(**opportunity.dict())
    db.add(db_opportunity)
    db.commit()
    db.refresh(db_opportunity)
    return db_opportunity

def update_opportunity(db: Session, opportunity_id: str, opportunity: OpportunityUpdate):
    db_opportunity = get_opportunity(db, opportunity_id)
    if not db_opportunity:
        return None
    for key, value in opportunity.dict(exclude_unset=True).items():
        setattr(db_opportunity, key, value)
    db.commit()
    db.refresh(db_opportunity)
    return db_opportunity

def delete_opportunity(db: Session, opportunity_id: str):
    db_opportunity = get_opportunity(db, opportunity_id)
    if db_opportunity:
        db.delete(db_opportunity)
        db.commit()
    return db_opportunity

# Related operations: Get all contacts related to an opportunity
def get_opportunity_contacts(db: Session, opportunity_id: str):
    opportunity = get_opportunity(db, opportunity_id)
    if opportunity:
        return opportunity.contacts
    return []