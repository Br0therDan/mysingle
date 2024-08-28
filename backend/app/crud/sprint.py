# app/crud/sprint.py

from sqlalchemy.orm import Session
from app.models.sprint import Sprint
from app.schemas.sprint import SprintCreate, SprintUpdate

def get_sprint(db: Session, sprint_id: str):
    return db.query(Sprint).filter(Sprint.id == sprint_id).first()

def get_sprints(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Sprint).offset(skip).limit(limit).all()

def create_sprint(db: Session, sprint: SprintCreate):
    db_sprint = Sprint(**sprint.dict())
    db.add(db_sprint)
    db.commit()
    db.refresh(db_sprint)
    return db_sprint

def update_sprint(db: Session, sprint_id: str, sprint: SprintUpdate):
    db_sprint = get_sprint(db, sprint_id)
    if not db_sprint:
        return None
    for key, value in sprint.dict(exclude_unset=True).items():
        setattr(db_sprint, key, value)
    db.commit()
    db.refresh(db_sprint)
    return db_sprint

def delete_sprint(db: Session, sprint_id: str):
    db_sprint = get_sprint(db, sprint_id)
    if db_sprint:
        db.delete(db_sprint)
        db.commit()
    return db_sprint

# Related operations: Get all tasks related to a sprint
def get_sprint_tasks(db: Session, sprint_id: str):
    sprint = get_sprint(db, sprint_id)
    if sprint:
        return sprint.tasks
    return []