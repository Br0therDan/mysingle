# app/tests/test_main.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API"}

def test_not_found():
    response = client.get("/nonexistent-url")
    assert response.status_code == 404
