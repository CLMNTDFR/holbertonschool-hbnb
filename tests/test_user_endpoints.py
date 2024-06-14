import unittest
import json
from app import create_app


class UserEndpointsTestCase(unittest.TestCase):
    """
    Unit tests for the user endpoints of the API.
    """

    def setUp(self):
        """
        Set up test environment:
        - Create an instance of the Flask application.
        - Set up a test client for making requests.
        """
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        """Test case for creating a new user via POST request."""
        response = self.client.post(
            "/api/v1/users/",
            data=json.dumps(
                {"email": "test@example.com", "first_name": "John",
                 "last_name": "Doe"}
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.get_json())

    def test_get_user(self):
        """Test case for retrieving a user via GET request."""
        response = self.client.post(
            "/api/v1/users/",
            data=json.dumps(
                {"email": "test@example.com", "first_name": "John",
                 "last_name": "Doe"}
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        user_id = response.get_json()["id"]
        response = self.client.get(f"/api/v1/users/{user_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["email"], "test@example.com")

    def test_update_user(self):
        """Test case for updating a user via PUT request."""
        response = self.client.post(
            "/api/v1/users/",
            data=json.dumps(
                {"email": "test@example.com", "first_name": "John",
                 "last_name": "Doe"}
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        user_id = response.get_json()["id"]
        response = self.client.put(
            f"/api/v1/users/{user_id}",
            data=json.dumps(
                {
                    "email": "updated@example.com",
                    "first_name": "Jane",
                    "last_name": "Doe",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["email"], "updated@example.com")

    def test_delete_user(self):
        """Test case for deleting a user via DELETE request."""
        response = self.client.post(
            "/api/v1/users/",
            data=json.dumps(
                {"email": "test@example.com", "first_name": "John",
                 "last_name": "Doe"}
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        user_id = response.get_json()["id"]
        response = self.client.delete(f"/api/v1/users/{user_id}")
        self.assertEqual(response.status_code, 204)


if __name__ == "__main__":
    unittest.main()
