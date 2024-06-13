#!/usr/bin/python3
# Persistence for users

from datetime import datetime
from model.user import User
from persistence.IPersistenceManager import IPersistenceManager

class UserRepository(IPersistenceManager):
    """Class for managing the persistence of users."""
    def __init__(self):
        self.users = {}

    def save(self, user):
        """Saves a user."""
        user.created_at = datetime.now()
        user.updated_at = datetime.now()
        self.users[user.user_id] = user

    def get(self, user_id):
        """Fetches a user."""
        return self.users.get(user_id)

    def get_all(self):
        """Fetches all users."""
        return list(self.users.values())

    def update(self, user_id, new_user_data):
        """Updates an existing user."""
        if user_id in self.users:
            user = self.users[user_id]
            user.update_user_data(new_user_data)
            user.updated_at = datetime.now()
            self.save(user)
            return True
        return False

    def delete(self, user_id):
        """Deletes an existing user."""
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
