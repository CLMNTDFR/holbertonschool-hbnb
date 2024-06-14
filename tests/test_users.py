import requests

BASE_URL = "http://localhost:5000/users"


def test_create_user():
    """Test case for creating a new user via POST request."""
    response = requests.post(
        BASE_URL,
        json={
            "email": "test@example.com",
            "password": "password",
            "first_name": "Test",
            "last_name": "User",
        },
    )
    assert response.status_code == 201
    assert "id" in response.json()


def test_get_users():
    """Test case for retrieving all users via GET request."""
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
