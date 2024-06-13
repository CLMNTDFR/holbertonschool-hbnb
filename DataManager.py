#!/usr/bin/python3
# Data manager for handling CRUD operations across different entity types

from persistence.place_repository import PlaceRepository
from persistence.user_repository import UserRepository
from persistence.review_repository import ReviewRepository
from persistence.amenity_repository import AmenityRepository
from persistence.country_repository import CountryRepository
from persistence.city_repository import CityRepository
from model.place import Place
from model.user import User
from model.review import Review
from model.amenity import Amenity
from model.country import Country
from model.city import City


class DataManager:
    def __init__(self):
        self.place_repository = PlaceRepository()
        self.user_repository = UserRepository()
        self.review_repository = ReviewRepository()
        self.amenity_repository = AmenityRepository()
        self.country_repository = CountryRepository()
        self.city_repository = CityRepository()

    # Methods for Place
    def save_place(self, place_data):
        place = Place(**place_data)
        self.place_repository.save(place)
        return place.place_id

    def get_place(self, place_id):
        return self.place_repository.get(place_id)

    def update_place(self, place_id, new_data):
        return self.place_repository.update(place_id, new_data)

    def delete_place(self, place_id):
        return self.place_repository.delete(place_id)

    def get_all_places(self):
        return self.place_repository.get_all()

    # Methods for User
    def save_user(self, user_data):
        user = User(**user_data)
        self.user_repository.save(user)
        return user.user_id

    def get_user(self, user_id):
        return self.user_repository.get(user_id)

    def update_user(self, user_id, new_data):
        return self.user_repository.update(user_id, new_data)

    def delete_user(self, user_id):
        return self.user_repository.delete(user_id)

    def get_all_users(self):
        return self.user_repository.get_all()

    # Methods for Review
    def save_review(self, review_data):
        review = Review(**review_data)
        self.review_repository.save(review)
        return review.review_id

    def get_review(self, review_id):
        return self.review_repository.get(review_id)

    def update_review(self, review_id, new_data):
        return self.review_repository.update(review_id, new_data)

    def delete_review(self, review_id):
        return self.review_repository.delete(review_id)

    def get_all_reviews(self):
        return self.review_repository.get_all()

    # Methods for Amenity
    def save_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repository.save(amenity)
        return amenity.amenity_id

    def get_amenity(self, amenity_id):
        return self.amenity_repository.get(amenity_id)

    def update_amenity(self, amenity_id, new_data):
        return self.amenity_repository.update(amenity_id, new_data)

    def delete_amenity(self, amenity_id):
        return self.amenity_repository.delete(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repository.get_all()

    # Methods for Country
    def save_country(self, country_data):
        country = Country(**country_data)
        self.country_repository.save(country)
        return country.country_id

    def get_country(self, country_id):
        return self.country_repository.get(country_id)

    def update_country(self, country_id, new_data):
        return self.country_repository.update(country_id, new_data)

    def delete_country(self, country_id):
        return self.country_repository.delete(country_id)

    def get_all_countries(self):
        return self.country_repository.get_all()

    # Methods for City
    def save_city(self, city_data):
        city = City(**city_data)
        self.city_repository.save(city)
        return city.city_id

    def get_city(self, city_id):
        return self.city_repository.get(city_id)

    def update_city(self, city_id, new_data):
        return self.city_repository.update(city_id, new_data)

    def delete_city(self, city_id):
        return self.city_repository.delete(city_id)

    def get_all_cities(self):
        return self.city_repository.get_all()
