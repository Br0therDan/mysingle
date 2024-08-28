# app/tests/test_crud.py

from fastapi.testclient import TestClient
from app.main import app
from app.schemas import AccountCreate, Account
from app.crud import create_account, get_account

client = TestClient(app)

def test_create_account():
    account_data = {"account_name": "Test Account", "account_type": "Customer"}
    response = client.post("/accounts/", json=account_data)
    assert response.status_code == 200
    assert response.json()["account_name"] == "Test Account"

def test_read_account():
    response = client.get("/accounts/1")
    assert response.status_code == 200
    assert response.json()["account_name"] == "Test Account"
