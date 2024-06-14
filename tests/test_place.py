import unittest
import os
import json
from app.models.place import Place
from app.persistence.data_manager import DataManager

class PlaceModelTestCase(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.test_file = self.data_manager.file_path
        self.place = Place(
            name="Test Place",
            description="A nice place",
            address="123 Test St",
            city_id="city123",
            latitude=12.34,
            longitude=56.78,
            host_id="host123",
            num_rooms=3,
            num_bathrooms=2,
            price_per_night=100.0,
            max_guests=4
        )

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_get_place(self):
        self.place.save()
        retrieved_place = Place.get(self.place.id)
        self.assertIsNotNone(retrieved_place)
        self.assertEqual(retrieved_place.name, self.place.name)

    def test_update_place(self):
        self.place.save()
        self.place.name = "Updated Place"
        self.place.save()
        retrieved_place = Place.get(self.place.id)
        self.assertEqual(retrieved_place.name, "Updated Place")

    def test_delete_place(self):
        self.place.save()
        self.place.delete()
        retrieved_place = Place.get(self.place.id)
        self.assertIsNone(retrieved_place)

    def test_get_all_places(self):
        self.place.save()
        another_place = Place(
            name="Another Place",
            description="Another nice place",
            address="456 Another St",
            city_id="city123",
            latitude=34.56,
            longitude=78.90,
            host_id="host123",
            num_rooms=2,
            num_bathrooms=1,
            price_per_night=80.0,
            max_guests=2
        )
        another_place.save()
        places = Place.get_all()
        self.assertEqual(len(places), 2)

if __name__ == '__main__':
    unittest.main()
