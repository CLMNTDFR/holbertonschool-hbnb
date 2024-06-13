#!/usr/bin/python3
# Model for representing amenities

from datetime import datetime
import uuid

class Amenity:
    """Class representing an amenity."""
    def __init__(self, name):
        self.amenity_id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the amenity data as a dictionary."""
        return {
            'amenity_id': self.amenity_id,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
