#!/usr/bin/python3

import json
from persistence.IPersistenceManager import IPersistenceManager
from model.place import Place


class PlaceRepository(IPersistenceManager):
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {"places": []}

    def save_data(self):
        with open(self.filename, "w") as file:
            for place in self.data["places"]:
                if "created_at" in place:
                    place["created_at"] = place["created_at"].isoformat()
                if "updated_at" in place:
                    place["updated_at"] = place["updated_at"].isoformat()
            json.dump(self.data, file, indent=4)

    def save(self, entity):
        place_dict = entity.to_dict()
        if "created_at" in place_dict:
            place_dict["created_at"] = place_dict["created_at"].isoformat()
        if "updated_at" in place_dict:
            place_dict["updated_at"] = place_dict["updated_at"].isoformat()
        self.data["places"].append(place_dict)
        self.save_data()

    def get(self, place_id):
        for place in self.data["places"]:
            if place["place_id"] == place_id:
                return Place(**place)
        return None

    def update(self, place_id, new_data):
        for place in self.data["places"]:
            if place["place_id"] == place_id:
                place.update(new_data)
                self.save_data()
                return True
        return False

    def delete(self, place_id):
        self.data["places"] = [
            place for place in self.data["places"] if place["place_id"] != place_id
        ]
        self.save_data()
        return True

    def get_all(self):
        return [Place(**place) for place in self.data["places"]]
