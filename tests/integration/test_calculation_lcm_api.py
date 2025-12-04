import pytest
from fastapi.testclient import TestClient
from uuid import uuid4
from app.main import app

client = TestClient(app)

@pytest.fixture
def auth_headers():
    username = f"user_{uuid4().hex[:8]}"
    password = "TestPassword123!"

    client.post(
        "/auth/register",
        json={
            "username": username,
            "password": password,
            "confirm_password": password,
            "email": f"{username}@example.com",
            "first_name": "Test",
            "last_name": "User"
        }
    )

    login = client.post(
        "/auth/login",
        json={"username": username, "password": password}
    )

    token = login.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_create_lcm_calculation(auth_headers):
    response = client.post(
        "/calculations",
        json={"type": "lcm", "inputs": [4, 6]},
        headers=auth_headers
    )

    assert response.status_code == 201
    data = response.json()
    assert data["type"] == "lcm"
    assert data["inputs"] == [4, 6]
    assert data["result"] == 12


def test_lcm_invalid_inputs(auth_headers):
    response = client.post(
        "/calculations",
        json={"type": "lcm", "inputs": [5]},
        headers=auth_headers
    )

    assert response.status_code == 422
    assert "at least 2 items" in response.text
