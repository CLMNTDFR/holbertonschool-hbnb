import unittest
import sys
import os
from flask import Flask, json
from flask_restx import Api
from unittest.mock import MagicMock

# Add the parent directory of `tests_api` to `sys.path`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Add the `tests_api` directory to `sys.path`
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Importing from city_api in the same directory
from api.city_api import api, data_manager


class CityApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(api, path="/cities")
        self.client = self.app.test_client()

        # Mocking the DataManager methods
        data_manager.get_all_cities = MagicMock(
            return_value=[
                {"name": "Paris", "country_id": "1"},
                {"name": "New York", "country_id": "2"},
            ]
        )
        data_manager.save_city = MagicMock(return_value="city_123")
        data_manager.get_city = MagicMock(
            side_effect=lambda id: (
                {"name": "Paris", "country_id": "1"} if id == "city_123" else None
            )
        )
        data_manager.delete_city = MagicMock(side_effect=lambda id: id == "city_123")
        data_manager.update_city = MagicMock(
            side_effect=lambda id, data: id == "city_123"
        )

    def test_get_all_cities(self):
        response = self.client.get("/cities/")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["name"], "Paris")
        self.assertEqual(data[1]["name"], "New York")

    def test_create_city(self):
        response = self.client.post(
            "/cities/",
            data=json.dumps({"name": "London", "country_id": "3"}),
            content_type="application/json",
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["message"], "City successfully created")
        self.assertEqual(data["city_id"], "city_123")

    def test_get_city(self):
        response = self.client.get("/cities/city_123")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "Paris")

        response = self.client.get("/cities/nonexistent_id")
        self.assertEqual(response.status_code, 404)

    def test_delete_city(self):
        response = self.client.delete("/cities/city_123")
        self.assertEqual(response.status_code, 204)

        response = self.client.delete("/cities/nonexistent_id")
        self.assertEqual(response.status_code, 404)

    def test_update_city(self):
        response = self.client.put(
            "/cities/city_123",
            data=json.dumps({"name": "Updated City", "country_id": "1"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 204)

        response = self.client.put(
            "/cities/nonexistent_id",
            data=json.dumps({"name": "Updated City", "country_id": "1"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
