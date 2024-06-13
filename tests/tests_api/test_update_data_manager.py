import unittest
from unittest.mock import MagicMock
from uuid import uuid4
from DataManager import DataManager


class DataManagerUpdateTestCase(unittest.TestCase):
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
    def test_update_place(self):
        place_id = str(uuid4())
        new_data = {"name": "Updated Place"}
        self.data_manager.place_repository.update.return_value = new_data

        result = self.data_manager.update_place(place_id, new_data)
        self.data_manager.place_repository.update.assert_called_once_with(
            place_id, new_data
        )
        self.assertEqual(result, new_data)

    # Tests for User
    def test_update_user(self):
        user_id = str(uuid4())
        new_data = {"first_name": "Jane"}
        self.data_manager.user_repository.update.return_value = new_data

        result = self.data_manager.update_user(user_id, new_data)
        self.data_manager.user_repository.update.assert_called_once_with(
            user_id, new_data
        )
        self.assertEqual(result, new_data)

    # Tests for Review
    def test_update_review(self):
        review_id = str(uuid4())
        new_data = {"comment": "Updated review"}
        self.data_manager.review_repository.update.return_value = new_data

        result = self.data_manager.update_review(review_id, new_data)
        self.data_manager.review_repository.update.assert_called_once_with(
            review_id, new_data
        )
        self.assertEqual(result, new_data)

    # Tests for Amenity
    def test_update_amenity(self):
        amenity_id = str(uuid4())
        new_data = {"name": "Updated Amenity"}
        self.data_manager.amenity_repository.update.return_value = new_data

        result = self.data_manager.update_amenity(amenity_id, new_data)
        self.data_manager.amenity_repository.update.assert_called_once_with(
            amenity_id, new_data
        )
        self.assertEqual(result, new_data)

    # Tests for Country
    def test_update_country(self):
        country_id = str(uuid4())
        new_data = {"name": "Updated Country"}
        self.data_manager.country_repository.update.return_value = new_data

        result = self.data_manager.update_country(country_id, new_data)
        self.data_manager.country_repository.update.assert_called_once_with(
            country_id, new_data
        )
        self.assertEqual(result, new_data)

    # Tests for City
    def test_update_city(self):
        city_id = str(uuid4())
        new_data = {"name": "Updated City"}
        self.data_manager.city_repository.update.return_value = new_data

        result = self.data_manager.update_city(city_id, new_data)
        self.data_manager.city_repository.update.assert_called_once_with(
            city_id, new_data
        )
        self.assertEqual(result, new_data)


if __name__ == "__main__":
    unittest.main()
