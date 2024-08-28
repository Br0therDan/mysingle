# app/api/api_v1.py

from fastapi import APIRouter
from app.api.v1.endpoints import account, contact, opportunity, profile, project, sprint, task, organization, daily_scrum

api_router = APIRouter()

api_router.include_router(account.router, prefix="/accounts", tags=["accounts"])
api_router.include_router(contact.router, prefix="/contacts", tags=["contacts"])
api_router.include_router(opportunity.router, prefix="/opportunities", tags=["opportunities"])
api_router.include_router(profile.router, prefix="/profiles", tags=["profiles"])
api_router.include_router(project.router, prefix="/projects", tags=["projects"])
api_router.include_router(sprint.router, prefix="/sprints", tags=["sprints"])
api_router.include_router(task.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(organization.router, prefix="/organizations", tags=["organizations"])
api_router.include_router(daily_scrum.router, prefix="/daily_scrums", tags=["daily_scrums"])