# app/crud/profile.py

from sqlalchemy.orm import Session
from app.models.profile import Profile
from app.schemas.profile import ProfileCreate, ProfileUpdate

def get_profile(db: Session, profile_id: str):
    return db.query(Profile).filter(Profile.id == profile_id).first()

def get_profiles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Profile).offset(skip).limit(limit).all()

def create_profile(db: Session, profile: ProfileCreate):
    db_profile = Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def update_profile(db: Session, profile_id: str, profile: ProfileUpdate):
    db_profile = get_profile(db, profile_id)
    if not db_profile:
        return None
    for key, value in profile.dict(exclude_unset=True).items():
        setattr(db_profile, key, value)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def delete_profile(db: Session, profile_id: str):
    db_profile = get_profile(db, profile_id)
    if db_profile:
        db.delete(db_profile)
        db.commit()
    return db_profile

# Related operations: Get all accounts related to a profile
def get_profile_accounts(db: Session, profile_id: str):
    profile = get_profile(db, profile_id)
    if profile:
        return profile.accounts
    return []