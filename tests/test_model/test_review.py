import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Unit tests for the Review class.
    """

    def setUp(self):
        """
        Set up test case environment.
        """
        self.review = Review("user_1", "place_1", "Great place to stay!")

    def test_review_creation(self):
        """
        Test the creation of a Review object.
        """
        self.assertEqual(self.review.user_id, "user_1")
        self.assertEqual(self.review.place_id, "place_1")
        self.assertEqual(self.review.text, "Great place to stay!")

    def test_to_dict(self):
        """
        Test the to_dict method of Review.
        """
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['user_id'], "user_1")
        self.assertEqual(review_dict['place_id'], "place_1")
        self.assertEqual(review_dict['text'], "Great place to stay!")

    def test_update_review(self):
        """
        Test updating attributes of a Review.
        """
        self.review.text = "Amazing experience!"
        self.review.save()
        self.assertEqual(self.review.text, "Amazing experience!")

    def test_review_unique_id(self):
        """
        Test that each review has a unique ID.
        """
        review2 = Review("user_2", "place_2", "Had a wonderful time!")
        self.assertNotEqual(self.review.id, review2.id)


if __name__ == '__main__':
    unittest.main()
