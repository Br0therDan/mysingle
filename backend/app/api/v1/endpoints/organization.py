# app/api/v1/endpoints/organization.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.organization import Organization, OrganizationCreate, OrganizationUpdate
from app.crud.organization import (get_organization, get_organizations, create_organization, update_organization, delete_organization, get_organization_profiles)
from app.db.session import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.get("/", response_model=list[Organization])
def read_organizations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_organizations(db, skip=skip, limit=limit)

@router.get("/{organization_id}", response_model=Organization)
def read_organization(organization_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_organization = get_organization(db, organization_id)
    if not db_organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_organization

@router.post("/", response_model=Organization)
def create_new_organization(organization: OrganizationCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return create_organization(db, organization)

@router.put("/{organization_id}", response_model=Organization)
def update_existing_organization(organization_id: str, organization: OrganizationUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_organization = update_organization(db, organization_id, organization)
    if not db_organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_organization

@router.delete("/{organization_id}", response_model=Organization)
def delete_existing_organization(organization_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_organization = delete_organization(db, organization_id)
    if not db_organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_organization

@router.get("/{organization_id}/profiles", response_model=list)
def read_organization_profiles(organization_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_organization_profiles(db, organization_id)