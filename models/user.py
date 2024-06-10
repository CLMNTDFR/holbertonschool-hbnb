from models.base_model import BaseModel
import uuid
from datetime import datetime


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    """

    def __init__(self, email, password, first_name, last_name):
        """
        Initialize a new User instance.
        """
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.places_hosted = []  # List of places hosted by this user
        self.places_booked = []  # List of places booked by this user

    def host_place(self, place):
        """
        Add a place to the list of places hosted by this user.
        """
        self.places_hosted.append(place)

    def book_place(self, place):
        """
        Add a place to the list of places booked by this user.
        """
        self.places_booked.append(place)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        the instance's __dict__.
        """
        user_dict = super().to_dict()
        user_dict.update({
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'places_hosted': [place.id for place in self.places_hosted],
            'places_booked': [place.id for place in self.places_booked]
        })
        return user_dict
