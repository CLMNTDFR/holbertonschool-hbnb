#!/usr/bin/python3
# Persistence for places

from datetime import datetime
from model.place import Place
from persistence.IPersistenceManager import IPersistenceManager

class PlaceRepository(IPersistenceManager):
    """Class for managing the persistence of places."""
    def __init__(self):
        self.places = {}

    def save(self, place):
        """Saves a place."""
        place.created_at = datetime.now()
        place.updated_at = datetime.now()
        self.places[place.place_id] = place

    def get(self, place_id):
        """Fetches a place."""
        return self.places.get(place_id)

    def get_all(self):
        """Fetches all places."""
        return list(self.places.values())

    def update(self, place_id, new_place_data):
        """Updates an existing place."""
        if place_id in self.places:
            place = self.places[place_id]
            place.update_place_data(new_place_data)
            place.updated_at = datetime.now()
            self.save(place)
            return True
        return False

    def delete(self, place_id):
        """Deletes an existing place."""
        if place_id in self.places:
            del self.places[place_id]
            return True
        return False
