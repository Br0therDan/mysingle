# app/crud/daily_scrum.py

from sqlalchemy.orm import Session
from app.models.daily_scrum import DailyScrum
from app.schemas.daily_scrum import DailyScrumCreate, DailyScrumUpdate

def get_daily_scrum(db: Session, daily_scrum_id: str):
    return db.query(DailyScrum).filter(DailyScrum.id == daily_scrum_id).first()

def get_daily_scrums(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DailyScrum).offset(skip).limit(limit).all()

def create_daily_scrum(db: Session, daily_scrum: DailyScrumCreate):
    db_daily_scrum = DailyScrum(**daily_scrum.dict())
    db.add(db_daily_scrum)
    db.commit()
    db.refresh(db_daily_scrum)
    return db_daily_scrum

def update_daily_scrum(db: Session, daily_scrum_id: str, daily_scrum: DailyScrumUpdate):
    db_daily_scrum = get_daily_scrum(db, daily_scrum_id)
    if not db_daily_scrum:
        return None
    for key, value in daily_scrum.dict(exclude_unset=True).items():
        setattr(db_daily_scrum, key, value)
    db.commit()
    db.refresh(db_daily_scrum)
    return db_daily_scrum

def delete_daily_scrum(db: Session, daily_scrum_id: str):
    db_daily_scrum = get_daily_scrum(db, daily_scrum_id)
    if db_daily_scrum:
        db.delete(db_daily_scrum)
        db.commit()
    return db_daily_scrum

# Related operations: Get all daily scrums associated with a sprint
def get_daily_scrums_by_sprint(db: Session, sprint_id: str):
    return db.query(DailyScrum).filter(DailyScrum.sprint_id == sprint_id).all()

# Related operations: Get all daily scrums associated with a project
def get_daily_scrums_by_project(db: Session, project_id: str):
    return db.query(DailyScrum).filter(DailyScrum.project_id == project_id).all()