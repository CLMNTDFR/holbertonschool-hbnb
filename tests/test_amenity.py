import unittest
import os
import json
from app.models.amenity import Amenity
from app.persistence.data_manager import DataManager

class AmenityModelTestCase(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.test_file = self.data_manager.file_path
        self.amenity = Amenity(name="WiFi")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_get_amenity(self):
        self.amenity.save()
        retrieved_amenity = Amenity.get(self.amenity.id)
        self.assertIsNotNone(retrieved_amenity)
        self.assertEqual(retrieved_amenity.name, self.amenity.name)

    def test_update_amenity(self):
        self.amenity.save()
        self.amenity.name = "Updated Amenity"
        self.amenity.save()
        retrieved_amenity = Amenity.get(self.amenity.id)
        self.assertEqual(retrieved_amenity.name, "Updated Amenity")

    def test_delete_amenity(self):
        self.amenity.save()
        self.amenity.delete()
        retrieved_amenity = Amenity.get(self.amenity.id)
        self.assertIsNone(retrieved_amenity)

    def test_get_all_amenities(self):
        self.amenity.save()
        another_amenity = Amenity(name="Pool")
        another_amenity.save()
        amenities = Amenity.get_all()
        self.assertEqual(len(amenities), 2)

if __name__ == '__main__':
    unittest.main()
