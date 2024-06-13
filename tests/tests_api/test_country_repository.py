import unittest
import sys
import os
from unittest.mock import patch

# Ajouter le répertoire parent de `tests_api` au `sys.path`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Ajouter le répertoire `tests_api` au `sys.path`
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from model.country import Country
from persistence.country_repository import CountryRepository

class CountryRepositoryTestCase(unittest.TestCase):
    def setUp(self):
        self.repo = CountryRepository()

    def test_save_country(self):
        country = Country(name='France')
        self.repo.save(country)
        self.assertIn(country.country_id, self.repo.countries)
        self.assertEqual(self.repo.countries[country.country_id], country)

    def test_get_country(self):
        country = Country(name='USA')
        self.repo.save(country)
        fetched_country = self.repo.get(country.country_id)
        self.assertEqual(fetched_country, country)

    def test_get_all_countries(self):
        country1 = Country(name='France')
        country1.country_id = 1  # Simuler un identifiant unique
        country2 = Country(name='USA')
        country2.country_id = 2  # Simuler un identifiant unique

        self.repo.save(country1)
        self.repo.save(country2)

        all_countries = self.repo.get_all()

        # Debug: Print out the countries
        print(f"Countries in repository: {[country.name for country in all_countries]}")

        self.assertEqual(len(all_countries), 2)
        self.assertTrue(any(c.name == 'France' for c in all_countries))
        self.assertTrue(any(c.name == 'USA' for c in all_countries))

    def test_update_country(self):
        country = Country(name='France')
        self.repo.save(country)
        new_data = {'name': 'Updated France'}
        self.repo.update(country.country_id, new_data)
        updated_country = self.repo.get(country.country_id)
        self.assertEqual(updated_country.name, 'Updated France')

    def test_delete_country(self):
        country = Country(name='USA')
        self.repo.save(country)
        self.repo.delete(country.country_id)
        self.assertIsNone(self.repo.get(country.country_id))

if __name__ == '__main__':
    unittest.main()
