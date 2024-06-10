import unittest
from models.country import Country


class TestCountry(unittest.TestCase):
    """
    Unit tests for the Country class.
    """

    def setUp(self):
        """
        Set up test case environment.
        """
        self.country = Country("United States")

    def test_country_creation(self):
        """
        Test the creation of a Country object.
        """
        self.assertEqual(self.country.name, "United States")

    def test_to_dict(self):
        """
        Test the to_dict method of Country.
        """
        country_dict = self.country.to_dict()
        self.assertEqual(country_dict['name'], "United States")

    def test_update_country(self):
        """
        Test updating attributes of a Country.
        """
        self.country.name = "Canada"
        self.country.save()
        self.assertEqual(self.country.name, "Canada")

    def test_country_unique_id(self):
        """
        Test that each country has a unique ID.
        """
        country2 = Country("Mexico")
        self.assertNotEqual(self.country.id, country2.id)


if __name__ == '__main__':
    unittest.main()
