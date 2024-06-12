import unittest
from app import app, db
from models.user import User

class UserTestCase(unittest.TestCase):

    def setUp(self):
        """
        Set up the test case with a new Flask application
        and a clean database.
        """
        self.app = app.test_client()
        # Initialize any necessary resources

    def tearDown(self):
        """
        Tear down the test case by removing the database
        session and dropping all tables.
        """
        # Clean up any resources used
        pass

    def test_create_user(self):
        """
        Test creating a new user.
        """
        response = self.app.post(
            "/users/",
            json={
                "email": "test@example.com",
                "password": "password123",
                "first_name": "Test",
                "last_name": "User",
            },
        )
        self.assertEqual(response.status_code, 201)

    # Add other test methods as needed

if __name__ == "__main__":
    unittest.main()
