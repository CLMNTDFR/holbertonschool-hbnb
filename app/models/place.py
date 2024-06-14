from datetime import datetime
import uuid
from app.persistence.data_manager import DataManager

storage = DataManager()


class Place:
    """
    A class to represent a Place.
    """

    def __init__(
        self,
        name,
        description,
        address,
        city_id,
        latitude,
        longitude,
        host_id,
        num_rooms,
        num_bathrooms,
        price_per_night,
        max_guests,
    ):
        """
        Initialize a new Place instance.

        Args:
            name (str): The name of the place.
            description (str): The description of the place.
            address (str): The address of the place.
            city_id (str): The ID of the city where the place is located.
            latitude (float): The latitude of the place.
            longitude (float): The longitude of the place.
            host_id (str): The ID of the host.
            num_rooms (int): The number of rooms in the place.
            num_bathrooms (int): The number of bathrooms in the place.
            price_per_night (float): The price per night for the place.
            max_guests (int): The maximum number of guests the
                                place can accommodate.
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Save the place to the storage.
        """
        self.updated_at = datetime.utcnow()
        storage.save(self)

    def delete(self):
        """
        Delete the place from the storage.
        """
        storage.delete(self.id, "Place")

    def to_dict(self):
        """
        Convert the Place instance to a dictionary.

        Returns:
            dict: The dictionary representation of the place.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "city_id": self.city_id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "host_id": self.host_id,
            "num_rooms": self.num_rooms,
            "num_bathrooms": self.num_bathrooms,
            "price_per_night": self.price_per_night,
            "max_guests": self.max_guests,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def get(place_id):
        """
        Retrieve a place by its ID.

        Args:
            place_id (str): The ID of the place.

        Returns:
            Place: The place instance if found, None otherwise.
        """
        data = storage.get(place_id, "Place")
        if data:
            place = Place(
                name=data["name"],
                description=data["description"],
                address=data["address"],
                city_id=data["city_id"],
                latitude=data["latitude"],
                longitude=data["longitude"],
                host_id=data["host_id"],
                num_rooms=data["num_rooms"],
                num_bathrooms=data["num_bathrooms"],
                price_per_night=data["price_per_night"],
                max_guests=data["max_guests"],
            )
            place.id = data["id"]
            place.created_at = datetime.fromisoformat(data["created_at"])
            place.updated_at = datetime.fromisoformat(data["updated_at"])
            return place
        return None

    @staticmethod
    def get_all():
        """
        Retrieve all places from the storage.

        Returns:
            list: A list of Place instances.
        """
        data = storage.get_all("Place")
        places = []
        for item in data:
            place = Place(
                name=item["name"],
                description=item["description"],
                address=item["address"],
                city_id=item["city_id"],
                latitude=item["latitude"],
                longitude=item["longitude"],
                host_id=item["host_id"],
                num_rooms=item["num_rooms"],
                num_bathrooms=item["num_bathrooms"],
                price_per_night=item["price_per_night"],
                max_guests=item["max_guests"],
            )
            place.id = item["id"]
            place.created_at = datetime.fromisoformat(item["created_at"])
            place.updated_at = datetime.fromisoformat(item["updated_at"])
            places.append(place)
        return places
