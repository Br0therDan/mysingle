# app/api/v1/endpoints/profile.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.profile import Profile, ProfileCreate, ProfileUpdate
from app.crud.profile import (get_profile, get_profiles, create_profile, update_profile, delete_profile, get_profile_accounts)
from app.db.session import get_db
from app.core.security import get_current_user
from typing import Optional

router = APIRouter()

@router.get("/", response_model=list[Profile])
def read_profiles(skip: int = 0, limit: int = 10, job_role: Optional[str] = None, is_verified: Optional[bool] = None, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    query = db.query(Profile)
    if job_role:
        query = query.filter(Profile.job_role == job_role)
    if is_verified is not None:
        query = query.filter(Profile.is_verified == is_verified)
    return query.offset(skip).limit(limit).all()

@router.get("/{profile_id}", response_model=Profile)
def read_profile(profile_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_profile = get_profile(db, profile_id)
    if not db_profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile

@router.post("/", response_model=Profile)
def create_new_profile(profile: ProfileCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return create_profile(db, profile)

@router.put("/{profile_id}", response_model=Profile)
def update_existing_profile(profile_id: str, profile: ProfileUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_profile = update_profile(db, profile_id, profile)
    if not db_profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile

@router.delete("/{profile_id}", response_model=Profile)
def delete_existing_profile(profile_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_profile = delete_profile(db, profile_id)
    if not db_profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile

@router.get("/{profile_id}/accounts", response_model=list)
def read_profile_accounts(profile_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_profile_accounts(db, profile_id)