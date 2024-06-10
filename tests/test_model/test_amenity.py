import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Unit tests for the Amenity class.
    """

    def setUp(self):
        """
        Set up test case environment.
        """
        self.amenity = Amenity("WiFi")

    def test_amenity_creation(self):
        """
        Test the creation of an Amenity object.
        """
        self.assertEqual(self.amenity.name, "WiFi")

    def test_to_dict(self):
        """
        Test the to_dict method of Amenity.
        """
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "WiFi")

    def test_update_amenity(self):
        """
        Test updating attributes of an Amenity.
        """
        self.amenity.name = "Air Conditioning"
        self.amenity.save()
        self.assertEqual(self.amenity.name, "Air Conditioning")

    def test_amenity_unique_id(self):
        """
        Test that each amenity has a unique ID.
        """
        amenity2 = Amenity("Parking")
        self.assertNotEqual(self.amenity.id, amenity2.id)


if __name__ == '__main__':
    unittest.main()
