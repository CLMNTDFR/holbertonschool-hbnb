import unittest
from models.user import User
from models.place import Place


class TestUser(unittest.TestCase):
    """
    Unit tests for the User class.
    """

    def setUp(self):
        """
        Set up test case environment.
        """
        self.user = User("test@example.com", "password", "Test", "User")
        self.place = Place(
            name="Test Place",
            description="A place to test",
            address="123 Test St",
            city_id="city123",
            latitude=0.0,
            longitude=0.0,
            host=self.user,
            number_of_rooms=1,
            number_of_bathrooms=1,
            price_per_night=100,
            max_guests=2
        )

    def test_user_creation(self):
        """
        Test the creation of a User object.
        """
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")

    def test_to_dict(self):
        """
        Test the to_dict method of User.
        """
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['first_name'], "Test")
        self.assertEqual(user_dict['last_name'], "User")

    def test_update_user(self):
        """
        Test updating attributes of a User.
        """
        self.user.first_name = "Updated"
        self.user.save()
        self.assertEqual(self.user.first_name, "Updated")

    def test_user_unique_id(self):
        """
        Test that each user has a unique ID.
        """
        user2 = User("another@example.com", "password", "Another", "User")
        self.assertNotEqual(self.user.id, user2.id)

    def test_host_place(self):
        """
        Test hosting a place.
        """
        self.user.host_place(self.place)
        self.assertIn(self.place, self.user.places_hosted)

    def test_book_place(self):
        """
        Test booking a place.
        """
        self.user.book_place(self.place)
        self.assertIn(self.place, self.user.places_booked)


if __name__ == '__main__':
    unittest.main()
