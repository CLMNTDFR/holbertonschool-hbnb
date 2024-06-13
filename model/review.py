#!/usr/bin/python3
# Model for representing reviews

from datetime import datetime
import uuid

class Review:
    """Class representing a review."""
    def __init__(self, user_id, place_id, rating, comment):
        self.review_id = str(uuid.uuid4())
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the review data as a dictionary."""
        return {
            'review_id': self.review_id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': self.rating,
            'comment': self.comment,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
