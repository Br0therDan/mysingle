import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas import DailyScrumCreate

client = TestClient(app)

def test_create_daily_scrum():
    scrum_data = {
        "scrum_date": "2024-08-01",
        "summary": "Daily Scrum Meeting",
        "sprint_id": "some-sprint-uuid",
        "project_id": "some-project-uuid"
    }
    response = client.post("/daily_scrums/", json=scrum_data)
    assert response.status_code == 201
    assert response.json()["summary"] == "Daily Scrum Meeting"

def test_read_daily_scrum():
    scrum_id = "some-daily-scrum-uuid"
    response = client.get(f"/daily_scrums/{scrum_id}")
    assert response.status_code == 200
    assert response.json()["daily_scrum_id"] == scrum_id

def test_update_daily_scrum():
    scrum_id = "some-daily-scrum-uuid"
    update_data = {
        "summary": "Updated Scrum Meeting"
    }
    response = client.put(f"/daily_scrums/{scrum_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["summary"] == "Updated Scrum Meeting"

def test_delete_daily_scrum():
    scrum_id = "some-daily-scrum-uuid"
    response = client.delete(f"/daily_scrums/{scrum_id}")
    assert response.status_code == 204
