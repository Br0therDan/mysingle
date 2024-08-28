import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas import SprintCreate

client = TestClient(app)

def test_create_sprint():
    sprint_data = {
        "sprint_name": "Sprint 1",
        "project_id": "some-project-uuid",
        "goal": "Complete initial design",
        "start_date": "2024-08-01",
        "end_date": "2024-08-15",
        "status": "Active"
    }
    response = client.post("/sprints/", json=sprint_data)
    assert response.status_code == 201
    assert response.json()["sprint_name"] == "Sprint 1"

def test_read_sprint():
    sprint_id = "some-sprint-uuid"
    response = client.get(f"/sprints/{sprint_id}")
    assert response.status_code == 200
    assert response.json()["sprint_id"] == sprint_id

def test_update_sprint():
    sprint_id = "some-sprint-uuid"
    update_data = {
        "status": "Completed"
    }
    response = client.put(f"/sprints/{sprint_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["status"] == "Completed"

def test_delete_sprint():
    sprint_id = "some-sprint-uuid"
    response = client.delete(f"/sprints/{sprint_id}")
    assert response.status_code == 204
