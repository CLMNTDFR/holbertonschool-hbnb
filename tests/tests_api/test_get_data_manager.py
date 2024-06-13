import unittest
import sys
import os
from unittest.mock import MagicMock
from uuid import uuid4

# Ajouter le répertoire parent de `tests_api` au `sys.path`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Ajouter le répertoire `tests_api` au `sys.path`
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from DataManager import DataManager
from model.place import Place
from model.user import User
from model.review import Review
from model.amenity import Amenity
from model.country import Country
from model.city import City


class DataManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()

        # Mock repositories
        self.data_manager.place_repository = MagicMock()
        self.data_manager.user_repository = MagicMock()
        self.data_manager.review_repository = MagicMock()
        self.data_manager.amenity_repository = MagicMock()
        self.data_manager.country_repository = MagicMock()
        self.data_manager.city_repository = MagicMock()

    # Tests for Place
    def test_get_place(self):
        place_id = str(uuid4())
        place_data = {
            "name": "Test Place",
            "description": "A nice place",
            "address": "123 Main St",
            "city_id": "city_123",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "host_id": "host_123",
            "number_of_rooms": 3,
            "number_of_bathrooms": 2,
            "price_per_night": 150,
            "max_guests": 4,
            "amenity_ids": ["amenity_1", "amenity_2"],
        }
        place = Place(**place_data)
        place.place_id = place_id
        self.data_manager.place_repository.get.return_value = place

        result = self.data_manager.get_place(place_id)
        self.data_manager.place_repository.get.assert_called_once_with(place_id)
        self.assertEqual(result.place_id, place_id)

    # Tests for User
    def test_get_user(self):
        user_id = str(uuid4())
        user_data = {
            "username": "john_doe",
            "email": "john.doe@example.com",
            "password": "password123",
        }
        user = User(**user_data)
        user.user_id = user_id
        self.data_manager.user_repository.get.return_value = user

        result = self.data_manager.get_user(user_id)
        self.data_manager.user_repository.get.assert_called_once_with(user_id)
        self.assertEqual(result.user_id, user_id)

    # Tests for Review
    def test_get_review(self):
        review_id = str(uuid4())
        review_data = {
            "comment": "Great place!",
            "user_id": "user_123",
            "place_id": "place_123",
            "rating": 5,
        }
        review = Review(**review_data)
        review.review_id = review_id
        self.data_manager.review_repository.get.return_value = review

        result = self.data_manager.get_review(review_id)
        self.data_manager.review_repository.get.assert_called_once_with(review_id)
        self.assertEqual(result.review_id, review_id)

    # Tests for Amenity
    def test_get_amenity(self):
        amenity_id = str(uuid4())
        amenity_data = {"name": "Test Amenity"}
        amenity = Amenity(**amenity_data)
        amenity.amenity_id = amenity_id
        self.data_manager.amenity_repository.get.return_value = amenity

        result = self.data_manager.get_amenity(amenity_id)
        self.data_manager.amenity_repository.get.assert_called_once_with(amenity_id)
        self.assertEqual(result.amenity_id, amenity_id)

    # Tests for Country
    def test_get_country(self):
        country_id = str(uuid4())
        country_data = {"name": "Test Country"}
        country = Country(**country_data)
        country.country_id = country_id
        self.data_manager.country_repository.get.return_value = country

        result = self.data_manager.get_country(country_id)
        self.data_manager.country_repository.get.assert_called_once_with(country_id)
        self.assertEqual(result.country_id, country_id)

    # Tests for City
    def test_get_city(self):
        city_id = str(uuid4())
        city_data = {"name": "Test City", "country_id": "country_123"}
        city = City(**city_data)
        city.city_id = city_id
        self.data_manager.city_repository.get.return_value = city

        result = self.data_manager.get_city(city_id)
        self.data_manager.city_repository.get.assert_called_once_with(city_id)
        self.assertEqual(result.city_id, city_id)


if __name__ == "__main__":
    unittest.main()
