# app/crud/task.py

from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def get_task(db: Session, task_id: str):
    return db.query(Task).filter(Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: str, task: TaskUpdate):
    db_task = get_task(db, task_id)
    if not db_task:
        return None
    for key, value in task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: str):
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task

# Related operations: Get all tasks related to a sprint
def get_tasks_by_sprint(db: Session, sprint_id: str):
    return db.query(Task).filter(Task.sprint_id == sprint_id).all()

# Related operations: Get tasks assigned to a specific user
def get_tasks_by_assignee(db: Session, assignee_id: str):
    return db.query(Task).filter(Task.assigned_to == assignee_id).all()