import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas import AccountCreate

client = TestClient(app)

def test_create_account():
    account_data = {
        "account_name": "Test Account",
        "profile_id": "some-profile-uuid",
        "account_type": "Customer"
    }
    response = client.post("/accounts/", json=account_data)
    assert response.status_code == 201
    assert response.json()["account_name"] == "Test Account"

def test_read_account():
    account_id = "some-account-uuid"
    response = client.get(f"/accounts/{account_id}")
    assert response.status_code == 200
    assert response.json()["account_id"] == account_id

def test_update_account():
    account_id = "some-account-uuid"
    update_data = {
        "account_name": "Updated Account Name"
    }
    response = client.put(f"/accounts/{account_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["account_name"] == "Updated Account Name"

def test_delete_account():
    account_id = "some-account-uuid"
    response = client.delete(f"/accounts/{account_id}")
    assert response.status_code == 204
