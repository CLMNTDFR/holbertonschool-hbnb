#!/usr/bin/python3
# Persistence for review

import json
from persistence.IPersistenceManager import IPersistenceManager
from model.review import Review


class ReviewRepository(IPersistenceManager):
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {"reviews": []}

    def save_data(self):
        with open(self.filename, 'w') as file:
            for review in self.data['reviews']:
                if 'created_at' in review:
                    review['created_at'] = review['created_at'].isoformat()
                if 'updated_at' in review:
                    review['updated_at'] = review['updated_at'].isoformat()
            json.dump(self.data, file, indent=4)

    def save(self, entity):
        review_dict = entity.to_dict()
        if 'created_at' in review_dict:
            review_dict['created_at'] = review_dict['created_at'].isoformat()
        if 'updated_at' in review_dict:
            review_dict['updated_at'] = review_dict['updated_at'].isoformat()
        self.data['reviews'].append(review_dict)
        self.save_data()

    def get(self, review_id):
        for review in self.data["reviews"]:
            if review["review_id"] == review_id:
                return Review(**review)
        return None

    def update(self, review_id, new_data):
        for review in self.data["reviews"]:
            if review["review_id"] == review_id:
                review.update(new_data)
                self.save_data()
                return True
        return False

    def delete(self, review_id):
        self.data["reviews"] = [
            review
            for review in self.data["reviews"]
            if review["review_id"] != review_id
        ]
        self.save_data()
        return True

    def get_all(self):
        return [Review(**review) for review in self.data["reviews"]]
