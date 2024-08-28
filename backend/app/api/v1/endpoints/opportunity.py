# app/api/v1/endpoints/opportunity.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.opportunity import Opportunity, OpportunityCreate, OpportunityUpdate
from app.crud.opportunity import (get_opportunity, get_opportunities, create_opportunity, update_opportunity, delete_opportunity, get_opportunity_contacts)
from app.db.session import get_db
from app.core.security import get_current_user
from typing import Optional

router = APIRouter()

@router.get("/", response_model=list[Opportunity])
def read_opportunities(skip: int = 0, limit: int = 10, stage: Optional[str] = None, forecast_category: Optional[str] = None, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    query = db.query(Opportunity)
    if stage:
        query = query.filter(Opportunity.stage == stage)
    if forecast_category:
        query = query.filter(Opportunity.forecast_category == forecast_category)
    return query.offset(skip).limit(limit).all()

@router.get("/{opportunity_id}", response_model=Opportunity)
def read_opportunity(opportunity_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_opportunity = get_opportunity(db, opportunity_id)
    if not db_opportunity:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return db_opportunity

@router.post("/", response_model=Opportunity)
def create_new_opportunity(opportunity: OpportunityCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return create_opportunity(db, opportunity)

@router.put("/{opportunity_id}", response_model=Opportunity)
def update_existing_opportunity(opportunity_id: str, opportunity: OpportunityUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_opportunity = update_opportunity(db, opportunity_id, opportunity)
    if not db_opportunity:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return db_opportunity

@router.delete("/{opportunity_id}", response_model=Opportunity)
def delete_existing_opportunity(opportunity_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_opportunity = delete_opportunity(db, opportunity_id)
    if not db_opportunity:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return db_opportunity

@router.get("/{opportunity_id}/contacts", response_model=list)
def read_opportunity_contacts(opportunity_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_opportunity_contacts(db, opportunity_id)