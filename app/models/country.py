# app/models/country.py

import uuid
from datetime import datetime
from app.persistence.data_manager import DataManager

storage = DataManager()

class Country:
    def __init__(self, name, code):
        self.id = str(uuid.uuid4())
        self.name = name
        self.code = code
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        self.updated_at = datetime.utcnow()
        storage.save(self)

    def delete(self):
        storage.delete(self.id, 'Country')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @staticmethod
    def get(country_id):
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
        data = storage.get_all('Country')
        countries = []
        for item in data:
            country = Country(name=item['name'], code=item['code'])
            country.id = item['id']
            country.created_at = datetime.fromisoformat(item['created_at'])
            country.updated_at = datetime.fromisoformat(item['updated_at'])
            countries.append(country)
        return countries
