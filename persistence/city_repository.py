#!/usr/bin/python3
# Persistence for cities

from datetime import datetime
from model.city import City
from persistence.IPersistenceManager import IPersistenceManager

class CityRepository(IPersistenceManager):
    """Class for managing the persistence of cities."""
    def __init__(self):
        self.cities = {}

    def save(self, city):
        """Saves a city."""
        city.created_at = datetime.now()
        city.updated_at = datetime.now()
        self.cities[city.city_id] = city

    def get(self, city_id):
        """Fetches a city."""
        return self.cities.get(city_id)

    def get_all(self):
        """Fetches all cities."""
        return list(self.cities.values())

    def update(self, city_id, new_city_data):
        """Updates an existing city."""
        if city_id in self.cities:
            city = self.cities[city_id]
            for key, value in new_city_data.items():
                setattr(city, key, value)
            city.updated_at = datetime.now()
            self.save(city)
            return True
        return False

    def delete(self, city_id):
        """Deletes an existing city."""
        if city_id in self.cities:
            del self.cities[city_id]
            return True
        return False
