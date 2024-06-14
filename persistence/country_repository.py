#!/usr/bin/python3
# Persistence for countries

import json
from persistence.IPersistenceManager import IPersistenceManager
from model.country import Country


class CountryRepository(IPersistenceManager):
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {"countries": []}

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def save(self, entity):
        self.data["countries"].append(entity.to_dict())
        self.save_data()

    def get(self, country_id):
        for country in self.data["countries"]:
            if country["country_id"] == country_id:
                return Country(**country)
        return None

    def update(self, country_id, new_data):
        for country in self.data["countries"]:
            if country["country_id"] == country_id:
                country.update(new_data)
                self.save_data()
                return True
        return False

    def delete(self, country_id):
        self.data["countries"] = [
            country
            for country in self.data["countries"]
            if country["country_id"] != country_id
        ]
        self.save_data()
        return True

    def get_all(self):
        return [Country(**country) for country in self.data["countries"]]
