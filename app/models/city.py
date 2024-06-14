from datetime import datetime
import uuid
from app.persistence.data_manager import DataManager

storage = DataManager()

class City:
    def __init__(self, name, country_code, description=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.country_code = country_code
        self.description = description
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        self.updated_at = datetime.utcnow()
        storage.save(self)

    def delete(self):
        storage.delete(self.id, 'City')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'country_code': self.country_code,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @staticmethod
    def get(city_id):
        data = storage.get(city_id, 'City')
        if data:
            city = City(name=data['name'], country_code=data['country_code'], description=data.get('description'))
            city.id = data['id']
            city.created_at = datetime.fromisoformat(data['created_at'])
            city.updated_at = datetime.fromisoformat(data['updated_at'])
            return city
        return None

    @staticmethod
    def get_all():
        data = storage.get_all('City')
        cities = []
        for item in data:
            city = City(name=item['name'], country_code=item['country_code'], description=item.get('description'))
            city.id = item['id']
            city.created_at = datetime.fromisoformat(item['created_at'])
            city.updated_at = datetime.fromisoformat(item['updated_at'])
            cities.append(city)
        return cities
