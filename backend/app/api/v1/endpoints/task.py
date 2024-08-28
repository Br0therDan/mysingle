# app/api/v1/endpoints/task.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.crud.task import (get_task, get_tasks, create_task, update_task, delete_task, get_tasks_by_sprint, get_tasks_by_assignee)
from app.db.session import get_db
from app.core.security import get_current_user
from typing import Optional

router = APIRouter()

@router.get("/", response_model=list[Task])
def read_tasks(skip: int = 0, limit: int = 10, sprint_id: Optional[str] = None, assigned_to: Optional[str] = None, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    query = db.query(Task)
    if sprint_id:
        query = query.filter(Task.sprint_id == sprint_id)
    if assigned_to:
        query = query.filter(Task.assigned_to == assigned_to)
    return query.offset(skip).limit(limit).all()

@router.get("/{task_id}", response_model=Task)
def read_task(task_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_task = get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.post("/", response_model=Task)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return create_task(db, task)

@router.put("/{task_id}", response_model=Task)
def update_existing_task(task_id: str, task: TaskUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_task = update_task(db, task_id, task)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.delete("/{task_id}", response_model=Task)
def delete_existing_task(task_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_task = delete_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.get("/sprint/{sprint_id}/tasks", response_model=list[Task])
def read_tasks_by_sprint(sprint_id: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_tasks_by_sprint(db, sprint_id)

@router.get("/assignee/{assigned_to}/tasks", response_model=list[Task])
def read_tasks_by_assignee(assigned_to: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return