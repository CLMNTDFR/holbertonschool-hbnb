#!/usr/bin/python3
# Persistence for countries

from datetime import datetime
from model.country import Country
from persistence.IPersistenceManager import IPersistenceManager

class CountryRepository(IPersistenceManager):
    """Class for managing the persistence of countries."""
    def __init__(self):
        self.countries = {}

    def save(self, country):
        """Saves a country."""
        country.created_at = datetime.now()
        country.updated_at = datetime.now()
        self.countries[country.country_id] = country

    def get(self, country_id):
        """Fetches a country."""
        return self.countries.get(country_id)

    def get_all(self):
        """Fetches all countries."""
        return list(self.countries.values())

    def update(self, country_id, new_country_data):
        """Updates an existing country."""
        if country_id in self.countries:
            country = self.countries[country_id]
            for key, value in new_country_data.items():
                setattr(country, key, value)
            country.updated_at = datetime.now()
            self.save(country)
            return True
        return False

    def delete(self, country_id):
        """Deletes an existing country."""
        if country_id in self.countries:
            del self.countries[country_id]
            return True
        return False
