#!/usr/bin/python3
# Model for representing countries

from datetime import datetime
import uuid

class Country:
    """Class representing a country."""
    def __init__(self, name):
        self.country_id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the country data as a dictionary."""
        return {
            'country_id': self.country_id,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
