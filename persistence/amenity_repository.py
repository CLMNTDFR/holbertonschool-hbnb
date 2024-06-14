#!/usr/bin/python3
# Persistence for amenities

import json
from persistence.IPersistenceManager import IPersistenceManager
from model.amenity import Amenity


class AmenityRepository(IPersistenceManager):
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {"amenities": []}

    def save_data(self):
        with open(self.filename, 'w') as file:
            for country in self.data['countries']:
                if 'created_at' in country:
                    country['created_at'] = country['created_at'].isoformat()
                if 'updated_at' in country:
                    country['updated_at'] = country['updated_at'].isoformat()
            json.dump(self.data, file, indent=4)

    def save(self, entity):
        country_dict = entity.to_dict()
        if 'created_at' in country_dict:
            country_dict['created_at'] = country_dict['created_at'].isoformat()
        if 'updated_at' in country_dict:
            country_dict['updated_at'] = country_dict['updated_at'].isoformat()
        self.data['countries'].append(country_dict)
        self.save_data()

    def get(self, amenity_id):
        for amenity in self.data["amenities"]:
            if amenity["amenity_id"] == amenity_id:
                return Amenity(**amenity)
        return None

    def update(self, amenity_id, new_data):
        for amenity in self.data["amenities"]:
            if amenity["amenity_id"] == amenity_id:
                amenity.update(new_data)
                self.save_data()
                return True
        return False

    def delete(self, amenity_id):
        self.data["amenities"] = [
            amenity
            for amenity in self.data["amenities"]
            if amenity["amenity_id"] != amenity_id
        ]
        self.save_data()
        return True

    def get_all(self):
        return [Amenity(**amenity) for amenity in self.data["amenities"]]
