import unittest
import sys
import os
from datetime import datetime
from unittest.mock import patch, MagicMock

# Ajouter le répertoire parent de `tests_api` au `sys.path`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Ajouter le répertoire `tests_api` au `sys.path`
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from model.amenity import Amenity
from persistence.amenity_repository import AmenityRepository

class AmenityRepositoryTestCase(unittest.TestCase):
    def setUp(self):
        self.repo = AmenityRepository()

    def test_save_amenity(self):
        amenity = Amenity(name='Pool')
        self.repo.save(amenity)
        self.assertIn(amenity.amenity_id, self.repo.amenities)
        self.assertEqual(self.repo.amenities[amenity.amenity_id], amenity)

    def test_get_amenity(self):
        amenity = Amenity(name='Gym')
        self.repo.save(amenity)
        fetched_amenity = self.repo.get(amenity.amenity_id)
        self.assertEqual(fetched_amenity, amenity)

    def test_get_all_amenities(self):
        amenity1 = Amenity(name='Pool')
        amenity2 = Amenity(name='Gym')
        self.repo.save(amenity1)
        self.repo.save(amenity2)
        all_amenities = self.repo.get_all()
        self.assertIn(amenity1, all_amenities)
        self.assertIn(amenity2, all_amenities)

    def test_update_amenity(self):
        amenity = Amenity(name='Pool')
        self.repo.save(amenity)
        new_data = {'name': 'Updated Pool'}
        self.repo.update(amenity.amenity_id, new_data)
        updated_amenity = self.repo.get(amenity.amenity_id)
        self.assertEqual(updated_amenity.name, 'Updated Pool')

    def test_delete_amenity(self):
        amenity = Amenity(name='Gym')
        self.repo.save(amenity)
        self.repo.delete(amenity.amenity_id)
        self.assertIsNone(self.repo.get(amenity.amenity_id))

if __name__ == '__main__':
    unittest.main()
