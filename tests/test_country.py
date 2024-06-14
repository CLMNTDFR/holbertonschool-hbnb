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
            country = Country(
                name=data['name'],
                code=data['code']
            )
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
            country = Country(
                name=item['name'],
                code=item['code']
            )
            country.id = item['id']
            country.created_at = datetime.fromisoformat(item['created_at'])
            country.updated_at = datetime.fromisoformat(item['updated_at'])
            countries.append(country)
        return countries

# tests/test/test_country.py

import unittest
from app.models.country import Country

class CountryModelTestCase(unittest.TestCase):
    def setUp(self):
        self.country = Country(name="Test Country", code="TC")

    def test_save_and_get_country(self):
        self.country.save()
        retrieved_country = Country.get(self.country.id)
        self.assertIsNotNone(retrieved_country)
        self.assertEqual(retrieved_country.name, self.country.name)
        self.assertEqual(retrieved_country.code, self.country.code)

    def test_update_country(self):
        self.country.save()
        self.country.name = "Updated Country"
        self.country.save()
        retrieved_country = Country.get(self.country.id)
        self.assertEqual(retrieved_country.name, "Updated Country")

    def test_delete_country(self):
        self.country.save()
        self.country.delete()
        retrieved_country = Country.get(self.country.id)
        self.assertIsNone(retrieved_country)

    def test_get_all_countries(self):
        self.country.save()
        another_country = Country(name="Another Country", code="AC")
        another_country.save()
        countries = Country.get_all()
        self.assertEqual(len(countries), 2)

if __name__ == '__main__':
    unittest.main()
