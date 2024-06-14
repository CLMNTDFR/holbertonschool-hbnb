#!/usr/bin/python3
# Persistence for cities

import json
from persistence.IPersistenceManager import IPersistenceManager
from model.city import City


class CityRepository(IPersistenceManager):
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {"cities": []}

    def save_data(self):
        with open(self.filename, 'w') as file:
            for city in self.data['cities']:
                if 'created_at' in city:
                    city['created_at'] = city['created_at'].isoformat()
                if 'updated_at' in city:
                    city['updated_at'] = city['updated_at'].isoformat()
            json.dump(self.data, file, indent=4)

    def save(self, entity):
        city_dict = entity.to_dict()
        if 'created_at' in city_dict:
            city_dict['created_at'] = city_dict['created_at'].isoformat()
        if 'updated_at' in city_dict:
            city_dict['updated_at'] = city_dict['updated_at'].isoformat()
        self.data['cities'].append(city_dict)
        self.save_data()

    def get(self, city_id):
        for city in self.data["cities"]:
            if city["city_id"] == city_id:
                return City(**city)
        return None

    def update(self, city_id, new_data):
        for city in self.data["cities"]:
            if city["city_id"] == city_id:
                city.update(new_data)
                self.save_data()
                return True
        return False

    def delete(self, city_id):
        self.data["cities"] = [
            city for city in self.data["cities"] if city["city_id"] != city_id
        ]
        self.save_data()
        return True

    def get_all(self):
        return [City(**city) for city in self.data["cities"]]
