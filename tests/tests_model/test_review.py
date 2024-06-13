import unittest
from datetime import datetime
import uuid
from model.review import Review

class TestReview(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.user_id = "USER123"
        self.place_id = "PLACE123"
        self.rating = 5
        self.comment = "Amazing place!"
        self.review = Review(self.user_id, self.place_id, self.rating, self.comment)

    def test_review_creation(self):
        """Test if the review is created with correct attributes."""
        self.assertEqual(self.review.user_id, self.user_id)
        self.assertEqual(self.review.place_id, self.place_id)
        self.assertEqual(self.review.rating, self.rating)
        self.assertEqual(self.review.comment, self.comment)
        self.assertIsInstance(self.review.review_id, str)
        self.assertTrue(uuid.UUID(self.review.review_id, version=4))
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)
        self.assertLessEqual(self.review.created_at, datetime.now())
        self.assertLessEqual(self.review.updated_at, datetime.now())

    def test_to_dict(self):
        """Test the to_dict method."""
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['review_id'], self.review.review_id)
        self.assertEqual(review_dict['user_id'], self.review.user_id)
        self.assertEqual(review_dict['place_id'], self.review.place_id)
        self.assertEqual(review_dict['rating'], self.review.rating)
        self.assertEqual(review_dict['comment'], self.review.comment)
        self.assertEqual(review_dict['created_at'], self.review.created_at)
        self.assertEqual(review_dict['updated_at'], self.review.updated_at)

if __name__ == '__main__':
    unittest.main()
