import unittest
from unittest.mock import MagicMock
from uuid import uuid4
from DataManager import DataManager


class DataManagerDeleteTestCase(unittest.TestCase):
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
    def test_delete_place(self):
        place_id = str(uuid4())
        self.data_manager.place_repository.delete.return_value = None

        result = self.data_manager.delete_place(place_id)
        self.data_manager.place_repository.delete.assert_called_once_with(place_id)
        self.assertIsNone(result)

    # Tests for User
    def test_delete_user(self):
        user_id = str(uuid4())
        self.data_manager.user_repository.delete.return_value = None

        result = self.data_manager.delete_user(user_id)
        self.data_manager.user_repository.delete.assert_called_once_with(user_id)
        self.assertIsNone(result)

    # Tests for Review
    def test_delete_review(self):
        review_id = str(uuid4())
        self.data_manager.review_repository.delete.return_value = None

        result = self.data_manager.delete_review(review_id)
        self.data_manager.review_repository.delete.assert_called_once_with(review_id)
        self.assertIsNone(result)

    # Tests for Amenity
    def test_delete_amenity(self):
        amenity_id = str(uuid4())
        self.data_manager.amenity_repository.delete.return_value = None

        result = self.data_manager.delete_amenity(amenity_id)
        self.data_manager.amenity_repository.delete.assert_called_once_with(amenity_id)
        self.assertIsNone(result)

    # Tests for Country
    def test_delete_country(self):
        country_id = str(uuid4())
        self.data_manager.country_repository.delete.return_value = None

        result = self.data_manager.delete_country(country_id)
        self.data_manager.country_repository.delete.assert_called_once_with(country_id)
        self.assertIsNone(result)

    # Tests for City
    def test_delete_city(self):
        city_id = str(uuid4())
        self.data_manager.city_repository.delete.return_value = None

        result = self.data_manager.delete_city(city_id)
        self.data_manager.city_repository.delete.assert_called_once_with(city_id)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
