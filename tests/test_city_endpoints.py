import unittest
import json
from app import create_app


class CityEndpointsTestCase(unittest.TestCase):
    """
    Unit tests for City endpoints in the API.
    """

    def setUp(self):
        """
        Set up test environment:
        - Create Flask app instance using create_app().
        - Set up test client for making requests.
        """
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_city(self):
        """
        Test case for creating a new city via POST request.
        """
        response = self.client.post(
            "/api/v1/cities/",
            data=json.dumps(
                {"name": "New York",
                 "description": "The city that never sleeps"}
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.get_json())

    def test_get_city(self):
        """
        Test case for retrieving a city via GET request.
        """
        response = self.client.post(
            "/api/v1/cities/",
            data=json.dumps(
                {"name": "New York",
                 "description": "The city that never sleeps"}
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        city_id = response.get_json()["id"]
        response = self.client.get(f"/api/v1/cities/{city_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "New York")

    def test_update_city(self):
        """
        Test case for updating a city via PUT request.
        """
        response = self.client.post(
            "/api/v1/cities/",
            data=json.dumps(
                {"name": "New York",
                 "description": "The city that never sleeps"}
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        city_id = response.get_json()["id"]
        response = self.client.put(
            f"/api/v1/cities/{city_id}",
            data=json.dumps(
                {"name": "Updated City",
                 "description": "An updated description"}
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "Updated City")

    def test_delete_city(self):
        """
        Test case for deleting a city via DELETE request.
        """
        response = self.client.post(
            "/api/v1/cities/",
            data=json.dumps(
                {"name": "New York",
                 "description": "The city that never sleeps"}
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        city_id = response.get_json()["id"]
        response = self.client.delete(f"/api/v1/cities/{city_id}")
        self.assertEqual(response.status_code, 204)

        # Verify that the city has been deleted
        get_response = self.client.get(f"/api/v1/cities/{city_id}")
        self.assertEqual(get_response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
