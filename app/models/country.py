import uuid
from datetime import datetime
from app.persistence.data_manager import DataManager

storage = DataManager()


class Country:
    """
    A class to represent a Country.
    """

    def __init__(self, name, code):
        """
        Initialize a new Country instance.

        Args:
            name (str): The name of the country.
            code (str): The code of the country.
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.code = code
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Save the country to the storage.
        """
        self.updated_at = datetime.utcnow()
        storage.save(self)

    def delete(self):
        """
        Delete the country from the storage.
        """
        storage.delete(self.id, 'Country')

    def to_dict(self):
        """
        Convert the Country instance to a dictionary.

        Returns:
            dict: The dictionary representation of the country.
        """
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @staticmethod
    def get(country_id):
        """
        Retrieve a country by its ID.

        Args:
            country_id (str): The ID of the country.

        Returns:
            Country: The country instance if found, None otherwise.
        """
        data = storage.get(country_id, 'Country')
        if data:
            country = Country(name=data['name'], code=data['code'])
            country.id = data['id']
            country.created_at = datetime.fromisoformat(data['created_at'])
            country.updated_at = datetime.fromisoformat(data['updated_at'])
            return country
        return None

    @staticmethod
    def get_all():
        """
        Retrieve all countries from the storage.

        Returns:
            list: A list of Country instances.
        """
        data = storage.get_all('Country')
        countries = []
        for item in data:
            country = Country(name=item['name'], code=item['code'])
            country.id = item['id']
            country.created_at = datetime.fromisoformat(item['created_at'])
            country.updated_at = datetime.fromisoformat(item['updated_at'])
            countries.append(country)
        return countries
