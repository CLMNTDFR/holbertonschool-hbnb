import unittest
import json
from app import create_app


class CountryEndpointsTestCase(unittest.TestCase):
    """
    Unit tests for the Country API endpoints.
    """

    def setUp(self):
        """
        Set up test environment:
        - Create Flask app instance.
        - Set up test client for making requests.
        """
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_country(self):
        """
        Test case for creating a new country via POST request.
        """
        response = self.client.post(
            "/api/v1/countries/",
            data=json.dumps({"name": "France"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)  # Check creation
        self.assertIn(
            "id", response.get_json()
        )  # Check if response contains the ID of the created country

    def test_get_countries(self):
        """
        Test case for retrieving all countries via GET request.
        """
        response = self.client.post(
            "/api/v1/countries/",
            data=json.dumps({"name": "France"}),
            content_type="application/json",
        )
        self.assertEqual(
            response.status_code, 201
        )  # Create a country first for testing retrieval
        response = self.client.get("/api/v1/countries/")
        self.assertEqual(response.status_code, 200)  # Check if retrieval
        self.assertGreaterEqual(
            len(response.get_json()), 1
        )  # Check if at least one country is returned

    def test_get_country(self):
        """
        Test case for retrieving a specific country via GET request.
        """
        response = self.client.post(
            "/api/v1/countries/",
            data=json.dumps({"name": "France"}),
            content_type="application/json",
        )
        self.assertEqual(
            response.status_code, 201
        )  # Create a country first for testing retrieval
        country_id = response.get_json()["id"]
        response = self.client.get(f"/api/v1/countries/{country_id}")
        self.assertEqual(response.status_code, 200)  # Check if retrieval
        self.assertEqual(
            response.get_json()["name"], "France"
        )  # Check if correct country data is returned

    def test_update_country(self):
        """
        Test case for updating a specific country via PUT request.
        """
        response = self.client.post(
            "/api/v1/countries/",
            data=json.dumps({"name": "France"}),
            content_type="application/json",
        )
        self.assertEqual(
            response.status_code, 201
        )  # Create a country first for testing update
        country_id = response.get_json()["id"]
        response = self.client.put(
            f"/api/v1/countries/{country_id}",
            data=json.dumps({"name": "Germany"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)  # Check update
        self.assertEqual(
            response.get_json()["name"], "Germany"
        )  # Check if country name is updated correctly

    def test_delete_country(self):
        """
        Test case for deleting a specific country via DELETE request.
        """
        response = self.client.post(
            "/api/v1/countries/",
            data=json.dumps({"name": "France"}),
            content_type="application/json",
        )
        self.assertEqual(
            response.status_code, 201
        )  # Create a country first for testing deletion
        country_id = response.get_json()["id"]
        response = self.client.delete(f"/api/v1/countries/{country_id}")
        self.assertEqual(response.status_code, 204)  # Check deletion


if __name__ == "__main__":
    unittest.main()
