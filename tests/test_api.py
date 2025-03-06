import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import get_db
from tests.conftest import db as test_db

# Override dependency to use test DB
app.dependency_overrides[get_db] = lambda: test_db

client = TestClient(app)

def test_process_query():
    response = client.post("/query", json={"customer_id": 1, "query": "Where is my order?"})
    assert response.status_code == 200
    data = response.json()
    assert data["customer_id"] == 1
    assert data["query"] == "Where is my order?"
    assert data["query_type"] == "order_status"
    assert "response" in data
