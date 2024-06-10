import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Unit tests for the City class.
    """

    def setUp(self):
        """
        Set up test case environment.
        """
        self.city = City("San Francisco", "USA")

    def test_city_creation(self):
        """
        Test the creation of a City object.
        """
        self.assertEqual(self.city.name, "San Francisco")
        self.assertEqual(self.city.country_id, "USA")

    def test_to_dict(self):
        """
        Test the to_dict method of City.
        """
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['name'], "San Francisco")
        self.assertEqual(city_dict['country_id'], "USA")

    def test_update_city(self):
        """
        Test updating attributes of a City.
        """
        self.city.name = "Los Angeles"
        self.city.save()
        self.assertEqual(self.city.name, "Los Angeles")

    def test_city_unique_id(self):
        """
        Test that each city has a unique ID.
        """
        city2 = City("New York", "USA")
        self.assertNotEqual(self.city.id, city2.id)


if __name__ == '__main__':
    unittest.main()
