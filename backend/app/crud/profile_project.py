# app/crud/profile_project.py

from sqlalchemy.orm import Session
from app.models.profile_project import ProfileProject
from app.schemas.profile_project import ProfileProjectCreate, ProfileProjectUpdate

def get_profile_project(db: Session, profile_id: str, project_id: str):
    return db.query(ProfileProject).filter(ProfileProject.profile_id == profile_id, ProfileProject.project_id == project_id).first()

def get_profile_projects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ProfileProject).offset(skip).limit(limit).all()

def create_profile_project(db: Session, profile_project: ProfileProjectCreate):
    # 중복 확인 로직 추가
    existing_profile_project = get_profile_project(db, profile_project.profile_id, profile_project.project_id)
    if existing_profile_project:
        raise ValueError("This profile-project relationship already exists.")
    
    db_profile_project = ProfileProject(**profile_project.dict())
    db.add(db_profile_project)
    db.commit()
    db.refresh(db_profile_project)
    return db_profile_project

def update_profile_project(db: Session, profile_id: str, project_id: str, profile_project: ProfileProjectUpdate):
    db_profile_project = get_profile_project(db, profile_id, project_id)
    if not db_profile_project:
        return None
    for key, value in profile_project.dict(exclude_unset=True).items():
        setattr(db_profile_project, key, value)
    db.commit()
    db.refresh(db_profile_project)
    return db_profile_project

def delete_profile_project(db: Session, profile_id: str, project_id: str):
    db_profile_project = get_profile_project(db, profile_id, project_id)
    if db_profile_project:
        db.delete(db_profile_project)
        db.commit()
    return db_profile_project

# 특정 프로필과 연관된 모든 프로젝트 삭제
def delete_projects_by_profile(db: Session, profile_id: str):
    db.query(ProfileProject).filter(ProfileProject.profile_id == profile_id).delete(synchronize_session=False)
    db.commit()

# 특정 프로젝트와 연관된 모든 프로필 삭제
def delete_profiles_by_project(db: Session, project_id: str):
    db.query(ProfileProject).filter(ProfileProject.project_id == project_id).delete(synchronize_session=False)
    db.commit()

# 특정 프로필과 관련된 모든 프로젝트 가져오기
def get_projects_by_profile(db: Session, profile_id: str):
    return db.query(ProfileProject).filter(ProfileProject.profile_id == profile_id).all()

# 특정 프로젝트와 관련된 모든 프로필 가져오기
def get_profiles_by_project(db: Session, project_id: str):
    return db.query(ProfileProject).filter(ProfileProject.project_id == project_id).all()

# 대량의 프로필-프로젝트 관계 생성
def bulk_create_profile_projects(db: Session, profile_projects: list[ProfileProjectCreate]):
    db_profile_projects = [ProfileProject(**profile_project.dict()) for profile_project in profile_projects]
    db.bulk_save_objects(db_profile_projects)
    db.commit()
    return db_profile_projects

# 특정 프로필과 관련된 모든 프로젝트 관계 대량 삭제
def bulk_delete_profile_projects(db: Session, profile_id: str):
    db.query(ProfileProject).filter(ProfileProject.profile_id == profile_id).delete(synchronize_session=False)
    db.commit()