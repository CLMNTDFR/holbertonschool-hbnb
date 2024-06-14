import uuid
from datetime import datetime
from app.persistence.data_manager import DataManager
import unittest
from app.models.country import Country

storage = DataManager()


class Country:
    """
    Model class representing a country.
    """

    def __init__(self, name, code):
        """
        Initialize a new Country instance.

        Args:
        - name (str): The name of the country.
        - code (str): The country code.

        Initializes:
        - id (str): Unique identifier for the country.
        - created_at (datetime): Timestamp of when the country instance
        was created.
        - updated_at (datetime): Timestamp of when the country instance
        was last updated.
        """
        self.id = str(uuid.uuid4())  # Generate a new UUID for the country
        self.name = name
        self.code = code
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Save the current state of the country instance to the data storage.
        """
        self.updated_at = datetime.utcnow()  # Update the timestamp
        storage.save(self)

    def delete(self):
        """
        Delete the current country instance from the data storage.
        """
        storage.delete(self.id, "Country")

    def to_dict(self):
        """
        Convert the country instance to a dictionary representation.

        Returns:
        - dict: Dictionary containing the country's attributes.
        """
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def get(country_id):
        """
        Retrieve a country instance from storage by its ID.

        Args:
        - country_id (str): The ID of the country to retrieve.

        Returns:
        - Country or None: The retrieved Country instance or None if not found.
        """
        data = storage.get(country_id, "Country")
        if data:
            country = Country(name=data["name"], code=data["code"])
            country.id = data["id"]
            country.created_at = datetime.fromisoformat(data["created_at"])
            country.updated_at = datetime.fromisoformat(data["updated_at"])
            return country
        return None

    @staticmethod
    def get_all():
        """
        Retrieve all country instances from storage.

        Returns:
        - list: List of Country instances.
        """
        data = storage.get_all("Country")
        countries = []
        for item in data:
            country = Country(name=item["name"], code=item["code"])
            country.id = item["id"]
            country.created_at = datetime.fromisoformat(item["created_at"])
            country.updated_at = datetime.fromisoformat(item["updated_at"])
            countries.append(country)
        return countries


class CountryModelTestCase(unittest.TestCase):
    """
    Unit tests for the Country model class.
    """

    def setUp(self):
        """
        Set up test environment:
        - Create a new Country instance with test data.
        """
        self.country = Country(name="Test Country", code="TC")

    def test_save_and_get_country(self):
        """
        Test case for saving and retrieving a Country instance.
        """
        self.country.save()
        retrieved_country = Country.get(self.country.id)
        self.assertIsNotNone(retrieved_country)
        self.assertEqual(retrieved_country.name, self.country.name)
        self.assertEqual(retrieved_country.code, self.country.code)

    def test_update_country(self):
        """
        Test case for updating a Country instance.
        """
        self.country.save()
        self.country.name = "Updated Country"
        self.country.save()
        retrieved_country = Country.get(self.country.id)
        self.assertEqual(retrieved_country.name, "Updated Country")

    def test_delete_country(self):
        """
        Test case for deleting a Country instance.
        """
        self.country.save()
        self.country.delete()
        retrieved_country = Country.get(self.country.id)
        self.assertIsNone(retrieved_country)

    def test_get_all_countries(self):
        """
        Test case for retrieving all Country instances.
        """
        self.country.save()
        another_country = Country(name="Another Country", code="AC")
        another_country.save()
        countries = Country.get_all()
        self.assertEqual(len(countries), 2)


if __name__ == "__main__":
    unittest.main()
