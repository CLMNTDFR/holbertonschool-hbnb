import uuid
from datetime import datetime
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class for handling place information.
    """

    def __init__(self, name, description, address, city_id, latitude,
                 longitude, host, number_of_rooms, number_of_bathrooms,
                 price_per_night, max_guests):
        """
        Initialize a new Place instance.
        """
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host.id  # Reference to the host user
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.amenities = []
        self.reviews = []
        self.bookings = []  # List of users who booked this place

    def add_amenity(self, amenity):
        """
        Add an amenity to the place.
        """
        self.amenities.append(amenity)

    def add_review(self, review):
        """
        Add a review to the place.
        """
        self.reviews.append(review)

    def add_booking(self, user):
        """
        Add a user to the list of users who booked this place.
        """
        self.bookings.append(user)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        the instance's __dict__.
        """
        place_dict = super().to_dict()
        place_dict.update({
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city_id': self.city_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'host_id': self.host_id,
            'number_of_rooms': self.number_of_rooms,
            'number_of_bathrooms': self.number_of_bathrooms,
            'price_per_night': self.price_per_night,
            'max_guests': self.max_guests,
            'amenities': [amenity.to_dict() for amenity in self.amenities],
            'reviews': [review.to_dict() for review in self.reviews],
            'bookings': [user.id for user in self.bookings]
        })
        return place_dict
