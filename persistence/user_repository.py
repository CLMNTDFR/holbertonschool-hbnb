#!/usr/bin/python3

import json
from persistence.IPersistenceManager import IPersistenceManager
from model.user import User


class UserRepository(IPersistenceManager):
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {"users": []}

    def save_data(self):
        with open(self.filename, "w") as file:
            for user in self.data["users"]:
                if "created_at" in user:
                    user["created_at"] = user["created_at"].isoformat()
                if "updated_at" in user:
                    user["updated_at"] = user["updated_at"].isoformat()
            json.dump(self.data, file, indent=4)

    def save(self, entity):
        user_dict = entity.to_dict()
        if "created_at" in user_dict:
            user_dict["created_at"] = user_dict["created_at"].isoformat()
        if "updated_at" in user_dict:
            user_dict["updated_at"] = user_dict["updated_at"].isoformat()
        self.data["users"].append(user_dict)
        self.save_data()

    def get(self, user_id):
        for user in self.data["users"]:
            if user["user_id"] == user_id:
                return User(**user)
        return None

    def update(self, user_id, new_data):
        for user in self.data["users"]:
            if user["user_id"] == user_id:
                user.update(new_data)
                self.save_data()
                return True
        return False

    def delete(self, user_id):
        self.data["users"] = [
            user for user in self.data["users"] if user["user_id"] != user_id
        ]
        self.save_data()
        return True

    def get_all(self):
        return [User(**user) for user in self.data["users"]]
