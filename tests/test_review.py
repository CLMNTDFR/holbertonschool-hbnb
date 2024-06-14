import unittest
from datetime import datetime
from app.models.review import Review
from app.persistence.data_manager import DataManager


class ReviewModelTestCase(unittest.TestCase):
    """
    Unit tests for the Review model.
    """

    def setUp(self):
        """
        Set up test environment:
        - Initialize DataManager instance.
        - Create a Review instance with test data.
        """
        self.data_manager = DataManager()
        self.review = Review(
            user_id="123", place_id="456", rating=5, comment="Great place!"
        )

    def test_save_and_get_review(self):
        """Test case for saving and retrieving a Review object."""
        self.review.save()
        retrieved_review = Review.get(self.review.id)
        self.assertIsNotNone(retrieved_review)
        self.assertEqual(retrieved_review.comment, "Great place!")

    def test_get_all_reviews(self):
        """Test case for retrieving all reviews."""
        self.review.save()
        reviews = Review.get_all()
        self.assertIn(self.review.id, [review.id for review in reviews])

    def test_update_review(self):
        """Test case for updating a Review object."""
        self.review.save()
        self.review.comment = "Updated comment"
        self.review.save()
        retrieved_review = Review.get(self.review.id)
        self.assertEqual(retrieved_review.comment, "Updated comment")

    def test_delete_review(self):
        """Test case for deleting a Review object."""
        self.review.save()
        review_id = self.review.id
        self.review.delete()
        retrieved_review = Review.get(review_id)
        self.assertIsNone(retrieved_review)


if __name__ == "__main__":
    unittest.main()
