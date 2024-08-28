
# app/api/deps.py

from typing import Generator
from sqlalchemy.orm import Session
from app.db.session import get_session

# Dependency that provides a SQLAlchemy session
def get_db() -> Generator[Session, None, None]:
    session = get_session()
    try:
        yield session
    finally:
        session.close()