# app/crud/organization.py

from sqlalchemy.orm import Session
from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate, OrganizationUpdate

def get_organization(db: Session, organization_id: str):
    return db.query(Organization).filter(Organization.id == organization_id).first()

def get_organizations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Organization).offset(skip).limit(limit).all()

def create_organization(db: Session, organization: OrganizationCreate):
    db_organization = Organization(**organization.dict())
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization

def update_organization(db: Session, organization_id: str, organization: OrganizationUpdate):
    db_organization = get_organization(db, organization_id)
    if not db_organization:
        return None
    for key, value in organization.dict(exclude_unset=True).items():
        setattr(db_organization, key, value)
    db.commit()
    db.refresh(db_organization)
    return db_organization

def delete_organization(db: Session, organization_id: str):
    db_organization = get_organization(db, organization_id)
    if db_organization:
        db.delete(db_organization)
        db.commit()
    return db_organization

def get_organization_profiles(db: Session, organization_id: str):
    organization = get_organization(db, organization_id)
    if not organization:
        return []
    return organization.profiles