import unittest
import json
from app import create_app


class APITestCase(unittest.TestCase):
    """
    Test cases for API endpoints related to reviews.
    """

    def setUp(self):
        """
        Set up test environment:
        - Create Flask app instance using create_app().
        - Set up test client for making requests.
        """
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_review(self):
        """
        Test case for creating a new review via POST request.
        """
        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(
                {
                    "user_id": "user_1",
                    "place_id": "place_1",
                    "rating": 5,
                    "text": "Great place!",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(
            response.status_code, 201
        )  # Assert HTTP status code 201 (Created)
        self.assertIn(
            "id", response.get_json()
        )  # Assert response JSON contains 'id' field

    def test_update_review(self):
        """
        Test case for updating a review via PUT request.
        """
        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(
                {
                    "user_id": "user_1",
                    "place_id": "place_1",
                    "rating": 5,
                    "text": "Great place!",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(
            response.status_code, 201
        )  # Assert HTTP status code 201 (Created)
        review_id = response.get_json()["id"]
        response = self.client.put(
            f"/api/v1/reviews/{review_id}",
            data=json.dumps(
                {
                    "user_id": "user_1",
                    "place_id": "place_1",
                    "rating": 4,
                    "text": "Updated review",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["text"], "Updated review"
        )  # Assert updated review text

    def test_delete_review(self):
        """
        Test case for deleting a review via DELETE request.
        """
        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(
                {
                    "user_id": "user_1",
                    "place_id": "place_1",
                    "rating": 5,
                    "text": "Great place!",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(
            response.status_code, 201
        )  # Assert HTTP status code 201 (Created)
        review_id = response.get_json()["id"]
        response = self.client.delete(f"/api/v1/reviews/{review_id}")
        self.assertEqual(
            response.status_code, 204
        )  # Assert HTTP status code 204 (No Content)

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
        self.assertEqual(
            response.status_code, 201
        )  # Assert HTTP status code 201 (Created)
        self.assertIn(
            "id", response.get_json()
        )  # Assert response JSON contains 'id' field

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
        self.assertEqual(
            response.status_code, 201
        )  # Assert HTTP status code 201 (Created)
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
        self.assertEqual(
            response.get_json()["name"], "Updated City"
        )  # Assert updated city name

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
        self.assertEqual(
            response.status_code, 201
        )  # Assert HTTP status code 201 (Created)
        city_id = response.get_json()["id"]
        response = self.client.delete(f"/api/v1/cities/{city_id}")
        self.assertEqual(
            response.status_code, 204
        )  # Assert HTTP status code 204 (No Content)

        # Verify that the city has been deleted
        get_response = self.client.get(f"/api/v1/cities/{city_id}")
        self.assertEqual(
            get_response.status_code, 404
        )  # Assert HTTP status code 404 (Not Found)


if __name__ == "__main__":
    unittest.main()
