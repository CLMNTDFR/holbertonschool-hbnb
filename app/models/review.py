from datetime import datetime
import uuid
from app.persistence.data_manager import DataManager

storage = DataManager()


class Review:
    """
    A class to represent a Review.
    """

    def __init__(self, user_id, place_id, rating, comment):
        """
        Initialize a new Review instance.

        Args:
            user_id (str): The ID of the user who wrote the review.
            place_id (str): The ID of the place being reviewed.
            rating (int): The rating given to the place.
            comment (str): The comment of the review.
        """
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Save the review to the storage.
        """
        self.updated_at = datetime.utcnow()
        storage.save(self)

    def delete(self):
        """
        Delete the review from the storage.
        """
        storage.delete(self.id, 'Review')

    def to_dict(self):
        """
        Convert the Review instance to a dictionary.

        Returns:
            dict: The dictionary representation of the review.
        """
        return {
            'id': self.id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': self.rating,
            'comment': self.comment,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @staticmethod
    def get(review_id):
        """
        Retrieve a review by its ID.

        Args:
            review_id (str): The ID of the review.

        Returns:
            Review: The review instance if found, None otherwise.
        """
        data = storage.get(review_id, 'Review')
        if data:
            review = Review(
                user_id=data['user_id'],
                place_id=data['place_id'],
                rating=data['rating'],
                comment=data['comment']
            )
            review.id = data['id']
            review.created_at = datetime.fromisoformat(data['created_at'])
            review.updated_at = datetime.fromisoformat(data['updated_at'])
            return review
        return None

    @staticmethod
    def get_all():
        """
        Retrieve all reviews from the storage.

        Returns:
            list: A list of Review instances.
        """
        data = storage.get_all('Review')
        reviews = []
        for item in data:
            review = Review(
                user_id=item['user_id'],
                place_id=item['place_id'],
                rating=item['rating'],
                comment=item['comment']
            )
            review.id = item['id']
            review.created_at = datetime.fromisoformat(item['created_at'])
            review.updated_at = datetime.fromisoformat(item['updated_at'])
            reviews.append(review)
        return reviews
