#!/usr/bin/python3
# Model for representing cities

from datetime import datetime
import uuid

class City:
    """Class representing a city."""
    def __init__(self, name, country_id):
        self.city_id = str(uuid.uuid4())
        self.name = name
        self.country_id = country_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the city data as a dictionary."""
        return {
            'city_id': self.city_id,
            'name': self.name,
            'country_id': self.country_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
