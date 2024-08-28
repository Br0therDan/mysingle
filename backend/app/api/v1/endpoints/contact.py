# app/api/v1/endpoints/contact.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.contact import Contact, ContactCreate, ContactUpdate
from app.crud.contact import (get_contact, get_contacts, create_contact, update_contact, delete_contact, get_contact_opportunities)
from app.db.session import get_db
from app.core.security import get_current_user
from typing import Optional

router = APIRouter()

@router.get("/", response_model=list[Contact])
def read_contacts(skip: int = 0, limit: int = 10, account_id: Optional[str] = None, job_role: Optional[str] = None, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    query = db.query(Contact)
    if account_id:
        query = query.filter(Contact.account_id == account_id)
    if job_role:
        query = query.filter(Contact.job_role == job_role)
    return query.offset(skip).limit(limit).all()

@router.get("/{contact_id}", response_model=Contact)
def read_contact(contact_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_contact = get_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@router.post("/", response_model=Contact)
def create_new_contact(contact: ContactCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return create_contact(db, contact)

@router.put("/{contact_id}", response_model=Contact)
def update_existing_contact(contact_id: str, contact: ContactUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_contact = update_contact(db, contact_id, contact)
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@router.delete("/{contact_id}", response_model=Contact)
def delete_existing_contact(contact_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_contact = delete_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@router.get("/{contact_id}/opportunities", response_model=list)
def read_contact_opportunities(contact_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_contact_opportunities(db, contact_id)