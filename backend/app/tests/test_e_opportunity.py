import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas import OpportunityCreate

client = TestClient(app)

def test_create_opportunity():
    opportunity_data = {
        "opportunity_name": "New Business Deal",
        "close_date": "2024-12-31",
        "ACV": 100000.00,
        "account_id": "some-account-uuid",
        "stage": "Negotiation",
        "forecast_category": "Best Case",
        "description": "A new business deal worth pursuing",
        "currency_code": "USD",
        "profile_id": "some-profile-uuid"
    }
    response = client.post("/opportunities/", json=opportunity_data)
    assert response.status_code == 201
    assert response.json()["opportunity_name"] == "New Business Deal"

def test_read_opportunity():
    opportunity_id = "some-opportunity-uuid"
    response = client.get(f"/opportunities/{opportunity_id}")
    assert response.status_code == 200
    assert response.json()["opportunity_id"] == opportunity_id

def test_update_opportunity():
    opportunity_id = "some-opportunity-uuid"
    update_data = {
        "stage": "Closed Won"
    }
    response = client.put(f"/opportunities/{opportunity_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["stage"] == "Closed Won"

def test_delete_opportunity():
    opportunity_id = "some-opportunity-uuid"
    response = client.delete(f"/opportunities/{opportunity_id}")
    assert response.status_code == 204
