# app/tests/test_auth.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login():
    login_data = {"username": "testuser", "password": "testpassword"}
    response = client.post("/login/", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_protected_route_without_token():
    response = client.get("/protected-route/")
    assert response.status_code == 401

def test_protected_route_with_token():
    login_data = {"username": "testuser", "password": "testpassword"}
    login_response = client.post("/login/", data=login_data)
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/protected-route/", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "This is a protected route"}
