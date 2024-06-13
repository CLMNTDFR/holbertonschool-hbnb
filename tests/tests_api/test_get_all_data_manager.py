import unittest
from unittest.mock import MagicMock
from uuid import uuid4
from DataManager import DataManager
from model.place import Place
from model.user import User
from model.review import Review
from model.amenity import Amenity
from model.country import Country
from model.city import City


class DataManagerGetAllTestCase(unittest.TestCase):
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
    def test_get_all_places(self):
        places = [
            Place(
                name="Place 1",
                description="Description 1",
                address="Address 1",
                city_id=str(uuid4()),
                latitude=40.7128,
                longitude=-74.0060,
                host_id=str(uuid4()),
                number_of_rooms=3,
                number_of_bathrooms=2,
                price_per_night=150,
                max_guests=4,
                amenity_ids=[str(uuid4()), str(uuid4())],
            ),
            Place(
                name="Place 2",
                description="Description 2",
                address="Address 2",
                city_id=str(uuid4()),
                latitude=34.0522,
                longitude=-118.2437,
                host_id=str(uuid4()),
                number_of_rooms=2,
                number_of_bathrooms=1,
                price_per_night=100,
                max_guests=2,
                amenity_ids=[str(uuid4()), str(uuid4())],
            ),
        ]
        self.data_manager.place_repository.get_all.return_value = places

        result = self.data_manager.get_all_places()
        self.data_manager.place_repository.get_all.assert_called_once()
        self.assertEqual(result, places)

    # Tests for User
    def test_get_all_users(self):
        users = [
            User(
                username="john_doe",  # Utilisez 'username' au lieu de 'first_name'
                email="john.doe@example.com",
                password="password_123",
            ),
            User(
                username="jane_smith",  # Utilisez 'username' au lieu de 'first_name'
                email="jane.smith@example.com",
                password="password_456",
            ),
        ]
        self.data_manager.user_repository.get_all.return_value = users

        result = self.data_manager.get_all_users()
        self.data_manager.user_repository.get_all.assert_called_once()
        self.assertEqual(result, users)
    # Tests for Review
    def test_get_all_reviews(self):
        reviews = [
            Review(
                comment="Review 1",
                user_id=str(uuid4()),
                place_id=str(uuid4()),
                rating=5,
            ),
            Review(
                comment="Review 2",
                user_id=str(uuid4()),
                place_id=str(uuid4()),
                rating=4,
            ),
        ]
        self.data_manager.review_repository.get_all.return_value = reviews

        result = self.data_manager.get_all_reviews()
        self.data_manager.review_repository.get_all.assert_called_once()
        self.assertEqual(result, reviews)

    # Tests for Amenity
    def test_get_all_amenities(self):
        amenities = [Amenity(name="Amenity 1"), Amenity(name="Amenity 2")]
        self.data_manager.amenity_repository.get_all.return_value = amenities

        result = self.data_manager.get_all_amenities()
        self.data_manager.amenity_repository.get_all.assert_called_once()
        self.assertEqual(result, amenities)

    # Tests for Country
    def test_get_all_countries(self):
        countries = [Country(name="Country 1"), Country(name="Country 2")]
        self.data_manager.country_repository.get_all.return_value = countries

        result = self.data_manager.get_all_countries()
        self.data_manager.country_repository.get_all.assert_called_once()
        self.assertEqual(result, countries)

    # Tests for City
    def test_get_all_cities(self):
        cities = [
            City(name="City 1", country_id=str(uuid4())),
            City(name="City 2", country_id=str(uuid4())),
        ]
        self.data_manager.city_repository.get_all.return_value = cities

        result = self.data_manager.get_all_cities()
        self.data_manager.city_repository.get_all.assert_called_once()
        self.assertEqual(result, cities)


if __name__ == "__main__":
    unittest.main()
