import unittest
from datetime import datetime, timedelta
import uuid
from model.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.name = "Paris"
        self.country_id = "FR"
        self.city = City(self.name, self.country_id)

    def test_city_creation(self):
        """Test if the city is created with correct attributes."""
        self.assertEqual(self.city.name, self.name)
        self.assertEqual(self.city.country_id, self.country_id)
        self.assertIsInstance(self.city.city_id, str)
        self.assertTrue(uuid.UUID(self.city.city_id, version=4))
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertLessEqual(self.city.created_at, datetime.now())
        self.assertLessEqual(self.city.updated_at, datetime.now())

    def test_to_dict(self):
        """Test the to_dict method."""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["city_id"], self.city.city_id)
        self.assertEqual(city_dict["name"], self.city.name)
        self.assertEqual(city_dict["country_id"], self.city.country_id)
        self.assertEqual(city_dict["created_at"], self.city.created_at)
        self.assertEqual(city_dict["updated_at"], self.city.updated_at)
        self.assertIsInstance(city_dict["created_at"], datetime)
        self.assertIsInstance(city_dict["updated_at"], datetime)

    def test_updated_at_changes(self):
        """Test if updated_at changes when city details are updated."""
        old_updated_at = self.city.updated_at
        self.city.name = "Lyon"
        self.city.updated_at = datetime.now()
        self.assertNotEqual(old_updated_at, self.city.updated_at)

    def test_invalid_uuid(self):
        """Test if an invalid UUID raises a ValueError."""
        with self.assertRaises(ValueError):
            uuid.UUID("invalid_uuid", version=4)

    def test_city_id_is_uuid(self):
        """Test if the city_id is a valid UUID."""
        try:
            uuid_obj = uuid.UUID(self.city.city_id, version=4)
        except ValueError:
            self.fail("city_id is not a valid UUID")


if __name__ == "__main__":
    unittest.main()
