import unittest
import json
from app import create_app


class AmenityEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up before each test:
        - Create the Flask app instance.
        - Create a test client to interact with the app.
        """
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        """
        Test creating an Amenity via API endpoint.
        """
        response = self.client.post(
            "/api/v1/amenities/",
            data=json.dumps({"name": "WiFi"}),
            content_type="application/json",
        )
        self.assertEqual(
            response.status_code, 201
        )  # Assert HTTP status code 201 (Created)
        self.assertIn(
            "id", response.get_json()
        )  # Assert response JSON contains 'id' field

    def test_get_amenity(self):
        """
        Test retrieving an Amenity via API endpoint.
        """
        response = self.client.post(
            "/api/v1/amenities/",
            data=json.dumps({"name": "WiFi"}),
            content_type="application/json",
        )
        self.assertEqual(
            response.status_code, 201
        )  # Assert HTTP status code 201 (Created)
        amenity_id = response.get_json()["id"]
        response = self.client.get(f"/api/v1/amenities/{amenity_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["name"], "WiFi"
        )  # Assert Amenity name is 'WiFi'

    def test_update_amenity(self):
        """
        Test updating an Amenity via API endpoint.
        """
        response = self.client.post(
            "/api/v1/amenities/",
            data=json.dumps({"name": "WiFi"}),
            content_type="application/json",
        )
        self.assertEqual(
            response.status_code, 201
        )  # Assert HTTP status code 201 (Created)
        amenity_id = response.get_json()["id"]
        response = self.client.put(
            f"/api/v1/amenities/{amenity_id}",
            data=json.dumps({"name": "Updated Amenity"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["name"], "Updated Amenity"
        )  # Assert updated name

    def test_delete_amenity(self):
        """
        Test deleting an Amenity via API endpoint.
        """
        response = self.client.post(
            "/api/v1/amenities/",
            data=json.dumps({"name": "WiFi"}),
            content_type="application/json",
        )
        self.assertEqual(
            response.status_code, 201
        )  # Assert HTTP status code 201 (Created)
        amenity_id = response.get_json()["id"]
        response = self.client.delete(f"/api/v1/amenities/{amenity_id}")
        self.assertEqual(response.status_code, 204)
