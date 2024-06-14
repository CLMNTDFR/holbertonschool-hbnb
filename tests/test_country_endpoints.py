import unittest
import json
from app import create_app

class CountryEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_country(self):
        response = self.client.post('/api/v1/countries/', data=json.dumps({
            'name': 'France'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_countries(self):
        response = self.client.post('/api/v1/countries/', data=json.dumps({
            'name': 'France'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client.get('/api/v1/countries/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.get_json()), 1)

    def test_get_country(self):
        response = self.client.post('/api/v1/countries/', data=json.dumps({
            'name': 'France'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        country_id = response.get_json()['id']
        response = self.client.get(f'/api/v1/countries/{country_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'France')

    def test_update_country(self):
        response = self.client.post('/api/v1/countries/', data=json.dumps({
            'name': 'France'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        country_id = response.get_json()['id']
        response = self.client.put(f'/api/v1/countries/{country_id}', data=json.dumps({
            'name': 'Germany'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'Germany')

    def test_delete_country(self):
        response = self.client.post('/api/v1/countries/', data=json.dumps({
            'name': 'France'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        country_id = response.get_json()['id']
        response = self.client.delete(f'/api/v1/countries/{country_id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
