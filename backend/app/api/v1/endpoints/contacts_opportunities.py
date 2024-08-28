# app/api/v1/endpoints/contacts_opportunities.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.contacts_opportunities import ContactsOpportunities, ContactsOpportunitiesCreate
from app.crud.contacts_opportunities import (
    get_contacts_opportunity,
    get_contacts_opportunities,
    create_contacts_opportunity,
    delete_contacts_opportunity,
    get_opportunities_by_contact,
    get_contacts_by_opportunity,
)
from app.db.session import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.get("/", response_model=list[ContactsOpportunities])
def read_contacts_opportunities(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_contacts_opportunities(db, skip=skip, limit=limit)

@router.post("/", response_model=ContactsOpportunities)
def create_new_contacts_opportunity(contacts_opportunity: ContactsOpportunitiesCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return create_contacts_opportunity(db, contacts_opportunity)

@router.delete("/{opportunity_id}/{contact_id}", response_model=ContactsOpportunities)
def delete_existing_contacts_opportunity(opportunity_id: str, contact_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_contacts_opportunity = delete_contacts_opportunity(db, opportunity_id, contact_id)
    if not db_contacts_opportunity:
        raise HTTPException(status_code=404, detail="ContactsOpportunity not found")
    return db_contacts_opportunity

@router.get("/contact/{contact_id}/opportunities", response_model=list)
def read_opportunities_by_contact(contact_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_opportunities_by_contact(db, contact_id)

@router.get("/opportunity/{opportunity_id}/contacts", response_model=list)
def read_contacts_by_opportunity(opportunity_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_contacts_by_opportunity(db, opportunity_id)