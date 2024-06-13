import unittest
from unittest.mock import MagicMock
from DataManager import DataManager

class DataManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.data_manager.save_amenity = MagicMock()
        self.data_manager.save_city = MagicMock()
        self.data_manager.save_country = MagicMock()
        self.data_manager.save_place = MagicMock()
        self.data_manager.save_review = MagicMock()
        self.data_manager.save_user = MagicMock()

    def test_save_amenity(self):
        amenity_id = '6a8fa6f3-fa80-4bed-bf03-e6f4e5e5717a'
        self.data_manager.save_amenity.return_value = amenity_id
        result = self.data_manager.save_amenity('some_data')
        self.assertEqual(result, amenity_id)

    def test_save_city(self):
        city_id = '5501afa4-5c6d-4fb0-b7cd-29850505d388'
        self.data_manager.save_city.return_value = city_id
        result = self.data_manager.save_city('some_city_data')
        self.assertEqual(result, city_id)

    def test_save_country(self):
        country_id = 'ee1bea4c-ad78-4ee8-8850-3212ac056925'
        self.data_manager.save_country.return_value = country_id
        result = self.data_manager.save_country('some_country_data')
        self.assertEqual(result, country_id)

    def test_save_place(self):
        place_id = 'e9076243-de64-45cf-a230-edbb0fcffede'
        self.data_manager.save_place.return_value = place_id
        result = self.data_manager.save_place('some_place_data')
        self.assertEqual(result, place_id)

    def test_save_review(self):
        review_id = '4c8091d7-0226-4b38-a526-042934d43a5d'
        self.data_manager.save_review.return_value = review_id
        result = self.data_manager.save_review('some_review_data')
        self.assertEqual(result, review_id)

    def test_save_user(self):
        user_id = 'bce18dd3-1c50-41f0-a3d5-53ba51945f47'
        self.data_manager.save_user.return_value = user_id
        result = self.data_manager.save_user('some_user_data')
        self.assertEqual(result, user_id)

if __name__ == "__main__":
    unittest.main()
