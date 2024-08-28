# app/crud/project.py

from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate

def get_project(db: Session, project_id: str):
    return db.query(Project).filter(Project.id == project_id).first()

def get_projects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Project).offset(skip).limit(limit).all()

def create_project(db: Session, project: ProjectCreate):
    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def update_project(db: Session, project_id: str, project: ProjectUpdate):
    db_project = get_project(db, project_id)
    if not db_project:
        return None
    for key, value in project.dict(exclude_unset=True).items():
        setattr(db_project, key, value)
    db.commit()
    db.refresh(db_project)
    return db_project

def delete_project(db: Session, project_id: str):
    db_project = get_project(db, project_id)
    if db_project:
        db.delete(db_project)
        db.commit()
    return db_project

# Related operations: Get all sprints related to a project
def get_project_sprints(db: Session, project_id: str):
    project = get_project(db, project_id)
    if project:
        return project.sprints
    return []