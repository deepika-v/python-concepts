"""
FastAPI Production Tests

This module provides:
- Comprehensive testing with pytest
- FastAPI TestClient usage
- Authentication testing
- API endpoint testing
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from fastapi_production.main import app, get_db

# Test database
TEST_DATABASE_URL = "sqlite+aiosqlite:///./test.db"
test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=test_engine, class_=AsyncSession
)

# Override the dependency
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Setup test database."""
    from fastapi_production.main import Base
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)

def test_health_check():
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "timestamp": response.json()["timestamp"]}

def test_create_user():
    """Test user creation."""
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123",
        "role": "user"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert data["role"] == "user"

def test_login():
    """Test user login and token generation."""
    login_data = {
        "username": "testuser",
        "password": "testpass123"
    }
    response = client.post("/token", data=login_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

    # Store token for other tests
    global test_token
    test_token = data["access_token"]

def test_get_current_user():
    """Test getting current user info."""
    headers = {"Authorization": f"Bearer {test_token}"}
    response = client.get("/users/me/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"

def test_rate_limiting():
    """Test rate limiting middleware."""
    # Make multiple requests quickly
    for i in range(65):  # Exceed the 60 requests per minute limit
        response = client.get("/health")
        if i < 60:
            assert response.status_code == 200
        else:
            assert response.status_code == 429

def test_metrics_endpoint():
    """Test Prometheus metrics endpoint."""
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "http_requests_total" in response.text

def test_mongo_items():
    """Test MongoDB integration."""
    item_data = {"name": "test item", "value": 42}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "test item"
    assert data["value"] == 42

    # Test getting items
    response = client.get("/items/")
    assert response.status_code == 200
    items = response.json()
    assert len(items) >= 1

if __name__ == "__main__":
    pytest.main([__file__])