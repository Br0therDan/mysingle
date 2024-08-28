import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas import ProjectCreate

client = TestClient(app)

def test_create_project():
    project_data = {
        "project_name": "Website Redesign",
        "account_id": "some-account-uuid",
        "profile_id": "some-profile-uuid",
        "description": "Redesigning the corporate website"
    }
    response = client.post("/projects/", json=project_data)
    assert response.status_code == 201
    assert response.json()["project_name"] == "Website Redesign"

def test_read_project():
    project_id = "some-project-uuid"
    response = client.get(f"/projects/{project_id}")
    assert response.status_code == 200
    assert response.json()["project_id"] == project_id

def test_update_project():
    project_id = "some-project-uuid"
    update_data = {
        "project_name": "Updated Project Name"
    }
    response = client.put(f"/projects/{project_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["project_name"] == "Updated Project Name"

def test_delete_project():
    project_id = "some-project-uuid"
    response = client.delete(f"/projects/{project_id}")
    assert response.status_code == 204
