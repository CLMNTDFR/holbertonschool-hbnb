from datetime import datetime
import uuid
from app.persistence.data_manager import DataManager

storage = DataManager()


class Amenity:
    """
    A class to represent an Amenity.
    """

    def __init__(self, name):
        """
        Initialize a new Amenity instance.

        Args:
            name (str): The name of the amenity.
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Save the amenity to the storage.
        """
        self.updated_at = datetime.utcnow()
        storage.save(self)

    def delete(self):
        """
        Delete the amenity from the storage.
        """
        storage.delete(self.id, 'Amenity')

    def to_dict(self):
        """
        Convert the Amenity instance to a dictionary.

        Returns:
            dict: The dictionary representation of the amenity.
        """
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @staticmethod
    def get(amenity_id):
        """
        Retrieve an amenity by its ID.

        Args:
            amenity_id (str): The ID of the amenity.

        Returns:
            Amenity: The amenity instance if found, None otherwise.
        """
        data = storage.get(amenity_id, 'Amenity')
        if data:
            amenity = Amenity(name=data['name'])
            amenity.id = data['id']
            amenity.created_at = datetime.fromisoformat(data['created_at'])
            amenity.updated_at = datetime.fromisoformat(data['updated_at'])
            return amenity
        return None

    @staticmethod
    def get_all():
        """
        Retrieve all amenities from the storage.

        Returns:
            list: A list of Amenity instances.
        """
        data = storage.get_all('Amenity')
        amenities = []
        for item in data:
            amenity = Amenity(name=item['name'])
            amenity.id = item['id']
            amenity.created_at = datetime.fromisoformat(item['created_at'])
            amenity.updated_at = datetime.fromisoformat(item['updated_at'])
            amenities.append(amenity)
        return amenities
