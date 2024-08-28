# app/api/v1/endpoints/sprint.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.sprint import Sprint, SprintCreate, SprintUpdate
from app.crud.sprint import (get_sprint, get_sprints, create_sprint, update_sprint, delete_sprint, get_sprint_tasks)
from app.db.session import get_db
from app.core.security import get_current_user
from typing import Optional

router = APIRouter()

@router.get("/", response_model=list[Sprint])
def read_sprints(skip: int = 0, limit: int = 10, project_id: Optional[str] = None, status: Optional[str] = None, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    query = db.query(Sprint)
    if project_id:
        query = query.filter(Sprint.project_id == project_id)
    if status:
        query = query.filter(Sprint.status == status)
    return query.offset(skip).limit(limit).all()

@router.get("/{sprint_id}", response_model=Sprint)
def read_sprint(sprint_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_sprint = get_sprint(db, sprint_id)
    if not db_sprint:
        raise HTTPException(status_code=404, detail="Sprint not found")
    return db_sprint

@router.post("/", response_model=Sprint)
def create_new_sprint(sprint: SprintCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return create_sprint(db, sprint)

@router.put("/{sprint_id}", response_model=Sprint)
def update_existing_sprint(sprint_id: str, sprint: SprintUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_sprint = update_sprint(db, sprint_id, sprint)
    if not db_sprint:
        raise HTTPException(status_code=404, detail="Sprint not found")
    return db_sprint

@router.delete("/{sprint_id}", response_model=Sprint)
def delete_existing_sprint(sprint_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_sprint = delete_sprint(db, sprint_id)
    if not db_sprint:
        raise HTTPException(status_code=404, detail="Sprint not found")
    return db_sprint

@router.get("/{sprint_id}/tasks", response_model=list)
def read_sprint_tasks(sprint_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_sprint_tasks(db, sprint_id)