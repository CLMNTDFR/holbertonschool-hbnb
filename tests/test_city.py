import unittest
import os
from app.models.city import City
from app.persistence.data_manager import DataManager


class CityModelTestCase(unittest.TestCase):
    """
    Unit tests for the City model operations.
    """

    def setUp(self):
        """
        Set up test environment:
        - Initialize DataManager instance.
        - Create test file path for DataManager.
        - Create a City instance with initial data.
        """
        self.data_manager = DataManager()
        self.test_file = self.data_manager.file_path
        self.city = City(name="Paris", country_code="FR")

    def tearDown(self):
        """
        Clean up test environment:
        - Remove the test file created by DataManager.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_get_city(self):
        """
        Test case for saving and retrieving a City object.
        """
        self.city.save()
        retrieved_city = City.get(self.city.id)
        self.assertIsNotNone(retrieved_city)
        self.assertEqual(retrieved_city.name, self.city.name)

    def test_update_city(self):
        """
        Test case for updating a City object.
        """
        self.city.save()
        self.city.name = "Updated City"
        self.city.save()
        retrieved_city = City.get(self.city.id)
        self.assertEqual(retrieved_city.name, "Updated City")

    def test_delete_city(self):
        """
        Test case for deleting a City object.
        """
        self.city.save()
        self.city.delete()
        retrieved_city = City.get(self.city.id)
        self.assertIsNone(retrieved_city)

    def test_get_all_cities(self):
        """
        Test case for retrieving all City objects.
        """
        self.city.save()
        another_city = City(name="Lyon", country_code="FR")
        another_city.save()
        cities = City.get_all()
        self.assertEqual(len(cities), 2)


if __name__ == "__main__":
    unittest.main()
