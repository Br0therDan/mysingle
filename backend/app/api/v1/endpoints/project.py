# app/api/v1/endpoints/project.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.project import Project, ProjectCreate, ProjectUpdate
from app.crud.project import (get_project, get_projects, create_project, update_project, delete_project, get_project_sprints)
from app.db.session import get_db
from app.core.security import get_current_user
from typing import Optional

router = APIRouter()

@router.get("/", response_model=list[Project])
def read_projects(skip: int = 0, limit: int = 10, account_id: Optional[str] = None, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    query = db.query(Project)
    if account_id:
        query = query.filter(Project.account_id == account_id)
    return query.offset(skip).limit(limit).all()

@router.get("/{project_id}", response_model=Project)
def read_project(project_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_project = get_project(db, project_id)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.post("/", response_model=Project)
def create_new_project(project: ProjectCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return create_project(db, project)

@router.put("/{project_id}", response_model=Project)
def update_existing_project(project_id: str, project: ProjectUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_project = update_project(db, project_id, project)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.delete("/{project_id}", response_model=Project)
def delete_existing_project(project_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_project = delete_project(db, project_id)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.get("/{project_id}/sprints", response_model=list)
def read_project_sprints(project_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_project_sprints(db, project_id)