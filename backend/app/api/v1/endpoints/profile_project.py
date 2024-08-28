# app/api/v1/endpoints/profile_project.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.profile_project import ProfileProject, ProfileProjectCreate, ProfileProjectUpdate
from app.crud.profile_project import (
    get_profile_project,
    get_profile_projects,
    create_profile_project,
    update_profile_project,
    delete_profile_project,
    get_projects_by_profile,
    get_profiles_by_project,
)
from app.db.session import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.get("/", response_model=list[ProfileProject])
def read_profile_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_profile_projects(db, skip=skip, limit=limit)

@router.post("/", response_model=ProfileProject)
def create_new_profile_project(profile_project: ProfileProjectCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return create_profile_project(db, profile_project)

@router.put("/{profile_id}/{project_id}", response_model=ProfileProject)
def update_existing_profile_project(profile_id: str, project_id: str, profile_project: ProfileProjectUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_profile_project = update_profile_project(db, profile_id, project_id, profile_project)
    if not db_profile_project:
        raise HTTPException(status_code=404, detail="ProfileProject not found")
    return db_profile_project

@router.delete("/{profile_id}/{project_id}", response_model=ProfileProject)
def delete_existing_profile_project(profile_id: str, project_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_profile_project = delete_profile_project(db, profile_id, project_id)
    if not db_profile_project:
        raise HTTPException(status_code=404, detail="ProfileProject not found")
    return db_profile_project

@router.get("/profile/{profile_id}/projects", response_model=list)
def read_projects_by_profile(profile_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_projects_by_profile(db, profile_id)

@router.get("/project/{project_id}/profiles", response_model=list)
def read_profiles_by_project(project_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_profiles_by_project(db, project_id)