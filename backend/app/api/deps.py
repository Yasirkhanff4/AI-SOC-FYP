from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_dashboard_summary():
    response = client.get("/api/dashboard/summary")
    assert response.status_code == 200
    data = response.json()
    assert "total_alerts" in data
    assert data["total_alerts"] >= 1


def test_login():
    response = client.post("/api/auth/login", json={"username": "admin", "password": "StrongPass123!"})
    assert response.status_code == 200
    body = response.json()
    assert "access_token" in body
