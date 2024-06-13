import unittest
import sys
import os
from datetime import datetime
from unittest.mock import patch

# Ajouter le répertoire parent de `tests_api` au `sys.path`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Ajouter le répertoire `tests_api` au `sys.path`
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from model.city import City
from persistence.city_repository import CityRepository

class CityRepositoryTestCase(unittest.TestCase):
    def setUp(self):
        self.repo = CityRepository()

    def test_save_city(self):
        city = City(name='Paris', country_id='1')
        self.repo.save(city)
        self.assertIn(city.city_id, self.repo.cities)
        self.assertEqual(self.repo.cities[city.city_id], city)

    def test_get_city(self):
        city = City(name='New York', country_id='2')
        self.repo.save(city)
        fetched_city = self.repo.get(city.city_id)
        self.assertEqual(fetched_city, city)

    def test_get_all_cities(self):
        city1 = City(name='Paris', country_id='1')
        city2 = City(name='New York', country_id='2')
        self.repo.save(city1)
        self.repo.save(city2)
        all_cities = self.repo.get_all()
        self.assertIn(city1, all_cities)
        self.assertIn(city2, all_cities)

    def test_update_city(self):
        city = City(name='Paris', country_id='1')
        self.repo.save(city)
        new_data = {'name': 'Updated Paris', 'country_id': '1'}
        self.repo.update(city.city_id, new_data)
        updated_city = self.repo.get(city.city_id)
        self.assertEqual(updated_city.name, 'Updated Paris')

    def test_delete_city(self):
        city = City(name='New York', country_id='2')
        self.repo.save(city)
        self.repo.delete(city.city_id)
        self.assertIsNone(self.repo.get(city.city_id))

if __name__ == '__main__':
    unittest.main()
