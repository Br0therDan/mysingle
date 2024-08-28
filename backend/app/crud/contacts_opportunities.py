# app/crud/contacts_opportunities.py

from sqlalchemy.orm import Session
from app.models.contacts_opportunities import ContactsOpportunities
from app.schemas.contacts_opportunities import ContactsOpportunitiesCreate

def get_contacts_opportunity(db: Session, opportunity_id: str, contact_id: str):
    return db.query(ContactsOpportunities).filter(ContactsOpportunities.opportunity_id == opportunity_id, ContactsOpportunities.contact_id == contact_id).first()

def get_contacts_opportunities(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ContactsOpportunities).offset(skip).limit(limit).all()

def create_contacts_opportunity(db: Session, contacts_opportunity: ContactsOpportunitiesCreate):
    existing_relationship = get_contacts_opportunity(db, contacts_opportunity.opportunity_id, contacts_opportunity.contact_id)
    if existing_relationship:
        raise ValueError("This contact-opportunity relationship already exists.")
    
    db_contacts_opportunity = ContactsOpportunities(**contacts_opportunity.dict())
    db.add(db_contacts_opportunity)
    db.commit()
    db.refresh(db_contacts_opportunity)
    return db_contacts_opportunity

def delete_contacts_opportunity(db: Session, opportunity_id: str, contact_id: str):
    db_contacts_opportunity = get_contacts_opportunity(db, opportunity_id, contact_id)
    if db_contacts_opportunity:
        db.delete(db_contacts_opportunity)
        db.commit()
    return db_contacts_opportunity

# 특정 기회와 연관된 모든 연락처 삭제
def delete_contacts_by_opportunity(db: Session, opportunity_id: str):
    relationships = db.query(ContactsOpportunities).filter(ContactsOpportunities.opportunity_id == opportunity_id).all()
    for relationship in relationships:
        db.delete(relationship)
    db.commit()

# 특정 연락처와 연관된 모든 기회 삭제
def delete_opportunities_by_contact(db: Session, contact_id: str):
    relationships = db.query(ContactsOpportunities).filter(ContactsOpportunities.contact_id == contact_id).all()
    for relationship in relationships:
        db.delete(relationship)
    db.commit()

# 특정 연락처와 관련된 모든 기회 가져오기
def get_opportunities_by_contact(db: Session, contact_id: str):
    return db.query(ContactsOpportunities).filter(ContactsOpportunities.contact_id == contact_id).all()

# 특정 기회와 관련된 모든 연락처 가져오기
def get_contacts_by_opportunity(db: Session, opportunity_id: str):
    return db.query(ContactsOpportunities).filter(ContactsOpportunities.opportunity_id == opportunity_id).all()

# 대량의 연락처-기회 관계 생성
def bulk_create_contacts_opportunities(db: Session, contacts_opportunities: list[ContactsOpportunitiesCreate]):
    db_contacts_opportunities = [ContactsOpportunities(**contacts_opportunity.dict()) for contacts_opportunity in contacts_opportunities]
    db.bulk_save_objects(db_contacts_opportunities)
    db.commit()
    return db_contacts_opportunities

# 특정 연락처와 관련된 모든 기회 관계 대량 삭제
def bulk_delete_contacts_opportunities(db: Session, contact_id: str):
    db.query(ContactsOpportunities).filter(ContactsOpportunities.contact_id == contact_id).delete(synchronize_session=False)
    db.commit()