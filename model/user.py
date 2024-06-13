#!/usr/bin/python3
"""Model for representing users."""

import uuid
from datetime import datetime

class User:
    """Class representing a user."""
    def __init__(self, username, email, password):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password = password
        self.reviews = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def add_review(self, review):
        """Adds a review."""
        self.reviews.append(review)

    def list_reviews(self):
        """Lists the reviews."""
        return self.reviews

    def update_user_data(self, new_data):
        """Updates user data with new data."""
        for key, value in new_data.items():
            setattr(self, key, value)
        self.updated_at = datetime.now()

    def check_password(self, password):
        """Checks if the password is correct."""
        return self.password == password

    def to_dict(self):
        """Returns the user data as a dictionary."""
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'reviews': self.reviews,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
