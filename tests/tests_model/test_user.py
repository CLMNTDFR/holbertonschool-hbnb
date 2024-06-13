import unittest
from datetime import datetime
import uuid
from model.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.username = "testuser"
        self.email = "testuser@example.com"
        self.password = "password123"
        self.user = User(self.username, self.email, self.password)

    def test_user_creation(self):
        """Test if the user is created with correct attributes."""
        self.assertEqual(self.user.username, self.username)
        self.assertEqual(self.user.email, self.email)
        self.assertEqual(self.user.password, self.password)
        self.assertIsInstance(self.user.user_id, str)
        self.assertTrue(uuid.UUID(self.user.user_id, version=4))
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertLessEqual(self.user.created_at, datetime.now())
        self.assertLessEqual(self.user.updated_at, datetime.now())
        self.assertEqual(self.user.reviews, [])

    def test_add_review(self):
        """Test adding a review."""
        review = "Great user!"
        self.user.add_review(review)
        self.assertIn(review, self.user.reviews)

    def test_list_reviews(self):
        """Test listing reviews."""
        review1 = "Great user!"
        review2 = "Very responsive!"
        self.user.add_review(review1)
        self.user.add_review(review2)
        self.assertEqual(self.user.list_reviews(), [review1, review2])

    def test_update_user_data(self):
        """Test updating user data."""
        new_data = {"username": "newusername", "email": "newemail@example.com"}
        self.user.update_user_data(new_data)
        self.assertEqual(self.user.username, "newusername")
        self.assertEqual(self.user.email, "newemail@example.com")
        self.assertLessEqual(self.user.updated_at, datetime.now())

    def test_check_password(self):
        """Test checking the password."""
        self.assertTrue(self.user.check_password(self.password))
        self.assertFalse(self.user.check_password("wrongpassword"))

    def test_to_dict(self):
        """Test the to_dict method."""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["user_id"], self.user.user_id)
        self.assertEqual(user_dict["username"], self.user.username)
        self.assertEqual(user_dict["email"], self.user.email)
        self.assertEqual(user_dict["password"], self.user.password)
        self.assertEqual(user_dict["reviews"], self.user.reviews)
        self.assertEqual(user_dict["created_at"], self.user.created_at)
        self.assertEqual(user_dict["updated_at"], self.user.updated_at)


if __name__ == "__main__":
    unittest.main()
