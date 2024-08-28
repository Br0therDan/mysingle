import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas import TaskCreate

client = TestClient(app)

def test_create_task():
    task_data = {
        "task_name": "Design Homepage",
        "description": "Create initial design for the homepage",
        "priority": "High",
        "status": "Open",
        "assigned_to": "some-profile-uuid",
        "sprint_id": "some-sprint-uuid"
    }
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 201
    assert response.json()["task_name"] == "Design Homepage"

def test_read_task():
    task_id = "some-task-uuid"
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["task_id"] == task_id

def test_update_task():
    task_id = "some-task-uuid"
    update_data = {
        "status": "In Progress"
    }
    response = client.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["status"] == "In Progress"

def test_delete_task():
    task_id = "some-task-uuid"
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204
