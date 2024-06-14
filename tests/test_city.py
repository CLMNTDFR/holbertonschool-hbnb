import unittest
import os
import json
from app.models.city import City
from app.persistence.data_manager import DataManager

class CityModelTestCase(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.test_file = self.data_manager.file_path
        self.city = City(name="Paris", country_code="FR")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_get_city(self):
        self.city.save()
        retrieved_city = City.get(self.city.id)
        self.assertIsNotNone(retrieved_city)
        self.assertEqual(retrieved_city.name, self.city.name)

    def test_update_city(self):
        self.city.save()
        self.city.name = "Updated City"
        self.city.save()
        retrieved_city = City.get(self.city.id)
        self.assertEqual(retrieved_city.name, "Updated City")

    def test_delete_city(self):
        self.city.save()
        self.city.delete()
        retrieved_city = City.get(self.city.id)
        self.assertIsNone(retrieved_city)

    def test_get_all_cities(self):
        self.city.save()
        another_city = City(name="Lyon", country_code="FR")
        another_city.save()
        cities = City.get_all()
        self.assertEqual(len(cities), 2)

if __name__ == '__main__':
    unittest.main()
