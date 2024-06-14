import unittest
import os
from app.models.amenity import Amenity
from app.persistence.data_manager import DataManager


class AmenityModelTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up before each test:
        - Initialize DataManager instance.
        - Set test_file attribute to DataManager's file path.
        - Create an initial Amenity instance with name 'WiFi'.
        """
        self.data_manager = DataManager()
        self.test_file = self.data_manager.file_path
        self.amenity = Amenity(name="WiFi")

    def tearDown(self):
        """
        Clean up after each test:
        - Remove the test file if it exists.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_get_amenity(self):
        """
        Test saving and retrieving an Amenity instance.
        """
        self.amenity.save()  # Save the Amenity instance
        retrieved_amenity = Amenity.get(
            self.amenity.id
        )  # Retrieve the Amenity by its ID
        self.assertIsNotNone(
            retrieved_amenity
        )  # Assert that the retrieved Amenity is not None
        self.assertEqual(
            retrieved_amenity.name, self.amenity.name
        )  # Assert that the names match

    def test_update_amenity(self):
        """
        Test updating an Amenity instance.
        """
        self.amenity.save()  # Save the initial Amenity instance
        self.amenity.name = "Updated Amenity"  # Update the name attribute
        self.amenity.save()  # Save the updated Amenity instance
        retrieved_amenity = Amenity.get(self.amenity.id)  # Retrieve Amenity
        self.assertEqual(
            retrieved_amenity.name, "Updated Amenity"
        )  # Assert the updated name

    def test_delete_amenity(self):
        """
        Test deleting an Amenity instance.
        """
        self.amenity.save()  # Save the Amenity instance
        self.amenity.delete()  # Delete the Amenity instance
        retrieved_amenity = Amenity.get(
            self.amenity.id
        )  # Try to retrieve the deleted Amenity
        self.assertIsNone(
            retrieved_amenity
        )  # Assert that the retrieved Amenity is None

    def test_get_all_amenities(self):
        """
        Test retrieving all Amenities.
        """
        self.amenity.save()  # Save the first Amenity instance
        another_amenity = Amenity(name="Pool")  # Create another Amenity
        another_amenity.save()  # Save the second Amenity instance
        amenities = Amenity.get_all()  # Retrieve all Amenities
        self.assertEqual(
            len(amenities), 2
        )  # Assert that there are two Amenities in total


if __name__ == "__main__":
    unittest.main()
