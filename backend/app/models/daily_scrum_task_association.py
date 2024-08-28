from sqlmodel import SQLModel, Field
import uuid

class DailyScrumTaskAssociation(SQLModel, table=True):
    __tablename__ = "daily_scrum_task_associations"
    task_id: uuid.UUID = Field(foreign_key="tasks.task_id", primary_key=True)
    daily_scrum_id: uuid.UUID = Field(foreign_key="daily_scrums.daily_scrum_id", primary_key=True)
