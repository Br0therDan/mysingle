# app/api/v1/endpoints/daily_scrum.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.daily_scrum import DailyScrum, DailyScrumCreate, DailyScrumUpdate
from app.crud.daily_scrum import (get_daily_scrum, get_daily_scrums, create_daily_scrum, update_daily_scrum, delete_daily_scrum, get_daily_scrums_by_sprint, get_daily_scrums_by_project)
from app.db.session import get_db
from app.core.security import get_current_user
from typing import Optional

router = APIRouter()

@router.get("/", response_model=list[DailyScrum])
def read_daily_scrums(skip: int = 0, limit: int = 10, sprint_id: Optional[str] = None, project_id: Optional[str] = None, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    query = db.query(DailyScrum)
    if sprint_id:
        query = query.filter(DailyScrum.sprint_id == sprint_id)
    if project_id:
        query = query.filter(DailyScrum.project_id == project_id)
    return query.offset(skip).limit(limit).all()

@router.get("/{daily_scrum_id}", response_model=DailyScrum)
def read_daily_scrum(daily_scrum_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_daily_scrum = get_daily_scrum(db, daily_scrum_id)
    if not db_daily_scrum:
        raise HTTPException(status_code=404, detail="Daily Scrum not found")
    return db_daily_scrum

@router.post("/", response_model=DailyScrum)
def create_new_daily_scrum(daily_scrum: DailyScrumCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return create_daily_scrum(db, daily_scrum)

@router.put("/{daily_scrum_id}", response_model=DailyScrum)
def update_existing_daily_scrum(daily_scrum_id: str, daily_scrum: DailyScrumUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_daily_scrum = update_daily_scrum(db, daily_scrum_id, daily_scrum)
    if not db_daily_scrum:
        raise HTTPException(status_code=404, detail="Daily Scrum not found")
    return db_daily_scrum

@router.delete("/{daily_scrum_id}", response_model=DailyScrum)
def delete_existing_daily_scrum(daily_scrum_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_daily_scrum = delete_daily_scrum(db, daily_scrum_id)
    if not db_daily_scrum:
        raise HTTPException(status_code=404, detail="Daily Scrum not found")
    return db_daily_scrum

@router.get("/sprint/{sprint_id}/daily_scrums", response_model=list[DailyScrum])
def read_daily_scrums_by_sprint(sprint_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_daily_scrums_by_sprint(db, sprint_id)

@router.get("/project/{project_id}/daily_scrums", response_model=list[DailyScrum])
def read_daily_scrums_by_project(project_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_daily_scrums_by_project(db, project_id)