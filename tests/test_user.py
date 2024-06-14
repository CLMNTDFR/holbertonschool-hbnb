# tests/test/test_data_manager.py

import unittest
from app.models.user import User
from app.persistence.data_manager import DataManager


class DataManagerTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up test environment:
        - Initialize DataManager instance.
        - Clear 'User' collection in storage.
        - Create a User instance for testing.
        """
        self.storage = DataManager()
        self.storage.clear("User")
        self.user = User(
            email="test@example.com",
            first_name="Test",
            last_name="User",
            password="password",
        )

    def test_save_user(self):
        """Test saving a User object."""
        try:
            self.user.save()
        except ValueError:
            self.fail("save() raised ValueError unexpectedly!")

    def test_update_user(self):
        """Test updating a User object."""
        self.user.save()
        self.user.first_name = "Updated"
        self.user.save()
        updated_user = User.get(self.user.id)
        self.assertEqual(updated_user.first_name, "Updated")

    def test_save_and_get_user(self):
        """Test saving and retrieving a User object."""
        self.user.save()
        retrieved_user = User.get(self.user.id)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, self.user.email)
        self.assertEqual(retrieved_user.first_name, self.user.first_name)
        self.assertEqual(retrieved_user.last_name, self.user.last_name)
        self.assertEqual(
            retrieved_user.password, self.user.password
        )  # Assurez-vous que le mot de passe est géré correctement

    def tearDown(self):
        """
        Clean up after each test:
        - Clear 'User' collection in storage.
        """
        self.storage.clear("User")


if __name__ == "__main__":
    unittest.main()
