import unittest
from app.persistence.data_manager import DataManager
from app.models.user import User
from app.models.city import City
from app.models.review import Review
from app.models.country import Country


class DataManagerTestCase(unittest.TestCase):
    """
    Unit tests for the DataManager class with various model objects.
    """

    def setUp(self):
        """
        Set up test environment:
        - Initialize DataManager instance.
        - Clear data for User, City, Review, and Country models.
        - Create instances of User, City, Review, and Country with test data.
        """
        self.data_manager = DataManager()
        self.data_manager.clear("User")
        self.data_manager.clear("City")
        self.data_manager.clear("Review")
        self.data_manager.clear("Country")
        self.user = User(
            email="test@example.com",
            password="password123",
            first_name="John",
            last_name="Doe",
        )
        self.city = City(name="New York", country_code="US")
        self.review = Review(
            user_id=self.user.id, place_id="123", rating=5,
            comment="Great place!"
        )
        self.country = Country(name="France", code="FR")

    def tearDown(self):
        """
        Clean up after each test:
        - Clear data for User, City, Review, and Country models.
        """
        self.data_manager.clear("User")
        self.data_manager.clear("City")
        self.data_manager.clear("Review")
        self.data_manager.clear("Country")

    # User tests
    def test_save_user(self):
        """
        Test case for saving and retrieving a User object.
        """
        self.user.save()
        retrieved_user = self.data_manager.get(self.user.id, "User")
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user["email"], self.user.email)

    def test_get_user(self):
        """
        Test case for retrieving a User object by ID.
        """
        self.user.save()
        retrieved_user = User.get(self.user.id)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, self.user.email)

    def test_update_user(self):
        """
        Test case for updating a User object.
        """
        self.user.save()
        self.user.email = "newemail@example.com"
        self.user.save()
        retrieved_user = User.get(self.user.id)
        self.assertEqual(retrieved_user.email, "newemail@example.com")

    def test_delete_user(self):
        """
        Test case for deleting a User object.
        """
        self.user.save()
        self.user.delete()
        retrieved_user = User.get(self.user.id)
        self.assertIsNone(retrieved_user)

    def test_get_all_users(self):
        """
        Test case for retrieving all User objects.
        """
        self.user.save()
        another_user = User(
            email="another@example.com",
            password="password",
            first_name="Another",
            last_name="User",
        )
        another_user.save()
        users = User.get_all()
        self.assertEqual(len(users), 2)

    def test_save_duplicate_email(self):
        """
        Test case for attempting to save
        a User object with a duplicate email.
        """
        self.user.save()
        duplicate_user = User(
            email="test@example.com",
            password="password",
            first_name="Duplicate",
            last_name="User",
        )
        with self.assertRaises(ValueError):
            duplicate_user.save()

    # City tests
    def test_save_city(self):
        """
        Test case for saving and retrieving a City object.
        """
        self.city.save()
        retrieved_city = self.data_manager.get(self.city.id, "City")
        self.assertIsNotNone(retrieved_city)
        self.assertEqual(retrieved_city["name"], self.city.name)

    def test_get_city(self):
        """
        Test case for retrieving a City object by ID.
        """
        self.city.save()
        retrieved_city = City.get(self.city.id)
        self.assertIsNotNone(retrieved_city)
        self.assertEqual(retrieved_city.name, self.city.name)

    def test_update_city(self):
        """
        Test case for updating a City object.
        """
        self.city.save()
        self.city.name = "Los Angeles"
        self.city.save()
        retrieved_city = City.get(self.city.id)
        self.assertEqual(retrieved_city.name, "Los Angeles")

    def test_delete_city(self):
        """
        Test case for deleting a City object.
        """
        self.city.save()
        self.city.delete()
        retrieved_city = City.get(self.city.id)
        self.assertIsNone(retrieved_city)

    # Review tests
    def test_save_review(self):
        """
        Test case for saving and retrieving a Review object.
        """
        self.review.save()
        retrieved_review = self.data_manager.get(self.review.id, "Review")
        self.assertIsNotNone(retrieved_review)
        self.assertEqual(retrieved_review["comment"], self.review.comment)

    def test_get_review(self):
        """
        Test case for retrieving a Review object by ID.
        """
        self.review.save()
        retrieved_review = Review.get(self.review.id)
        self.assertIsNotNone(retrieved_review)
        self.assertEqual(retrieved_review.comment, self.review.comment)

    def test_update_review(self):
        """
        Test case for updating a Review object.
        """
        self.review.save()
        self.review.comment = "Updated review"
        self.review.save()
        retrieved_review = Review.get(self.review.id)
        self.assertEqual(retrieved_review.comment, "Updated review")

    def test_delete_review(self):
        """
        Test case for deleting a Review object.
        """
        self.review.save()
        self.review.delete()
        retrieved_review = Review.get(self.review.id)
        self.assertIsNone(retrieved_review)

    # Country tests
    def test_save_and_get_country(self):
        """
        Test case for saving and retrieving a Country object.
        """
        self.country.save()
        retrieved_country = Country.get(self.country.id)
        self.assertIsNotNone(retrieved_country)
        self.assertEqual(retrieved_country.name, self.country.name)
        self.assertEqual(retrieved_country.code, self.country.code)

    def test_update_country(self):
        """
        Test case for updating a Country object.
        """
        self.country.save()
        self.country.name = "Updated Country"
        self.country.save()
        retrieved_country = Country.get(self.country.id)
        self.assertIsNotNone(retrieved_country)
        self.assertEqual(retrieved_country.name, "Updated Country")

    def test_delete_country(self):
        """
        Test case for deleting a Country object.
        """
        self.country.save()
        self.country.delete()
        retrieved_country = Country.get(self.country.id)
        self.assertIsNone(retrieved_country)

    def test_get_all_countries(self):
        """
        Test case for retrieving all Country objects.
        """
        self.country.save()
        another_country = Country(name="Spain", code="ES")
        another_country.save()
        countries = Country.get_all()
        self.assertEqual(len(countries), 2)


if __name__ == "__main__":
    unittest.main()
