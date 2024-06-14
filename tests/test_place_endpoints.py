import unittest
import json
from app import create_app


class PlaceEndpointsTestCase(unittest.TestCase):
    """
    Unit tests for the place endpoints of the API.
    """

    def setUp(self):
        """
        Set up test environment:
        - Create an instance of the Flask application.
        - Set up a test client for making requests.
        """
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_place(self):
        """
        Test case for creating a new place via POST request.
        """
        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps({"name": "New Place",
                             "description": "A nice place"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.get_json())

    def test_get_place(self):
        """
        Test case for retrieving a place via GET request.
        """
        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps({"name": "New Place",
                             "description": "A nice place"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        place_id = response.get_json()["id"]
        response = self.client.get(f"/api/v1/places/{place_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "New Place")

    def test_update_place(self):
        """
        Test case for updating a place via PUT request.
        """
        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps({"name": "New Place",
                             "description": "A nice place"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        place_id = response.get_json()["id"]
        response = self.client.put(
            f"/api/v1/places/{place_id}",
            data=json.dumps(
                {"name": "Updated Place",
                 "description": "An updated description"}
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "Updated Place")

    def test_delete_place(self):
        """
        Test case for deleting a place via DELETE request.
        """
        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps({"name": "New Place",
                             "description": "A nice place"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        place_id = response.get_json()["id"]
        response = self.client.delete(f"/api/v1/places/{place_id}")
        self.assertEqual(response.status_code, 204)


if __name__ == "__main__":
    unittest.main()
