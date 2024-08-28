# app/crud/contact.py

from sqlalchemy.orm import Session
from app.models.contact import Contact
from app.schemas.contact import ContactCreate, ContactUpdate

def get_contact(db: Session, contact_id: str):
    return db.query(Contact).filter(Contact.id == contact_id).first()

def get_contacts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Contact).offset(skip).limit(limit).all()

def create_contact(db: Session, contact: ContactCreate):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def update_contact(db: Session, contact_id: str, contact: ContactUpdate):
    db_contact = get_contact(db, contact_id)
    if not db_contact:
        return None
    for key, value in contact.dict(exclude_unset=True).items():
        setattr(db_contact, key, value)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def delete_contact(db: Session, contact_id: str):
    db_contact = get_contact(db, contact_id)
    if db_contact:
        db.delete(db_contact)
        db.commit()
    return db_contact

# Related operations: Get all opportunities related to a contact
def get_contact_opportunities(db: Session, contact_id: str):
    contact = get_contact(db, contact_id)
    if contact:
        return contact.opportunities
    return []