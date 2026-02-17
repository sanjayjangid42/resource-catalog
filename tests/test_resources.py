from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_list_resources():
    r = client.get("/catalog/v1/resources")
    assert r.status_code == 200
    assert "page" in r.json()
    assert "items" in r.json()


def test_create_resource():
    r = client.post(
        "/catalog/v1/resources",
        json={"name": "new-resource", "resource_type": "compute"},
    )
    assert r.status_code == 201
    assert "data" in r.json()


def test_get_not_found():
    r = client.get("/catalog/v1/resources/invalid-id")
    assert r.status_code == 404
    assert "error" in r.json()
