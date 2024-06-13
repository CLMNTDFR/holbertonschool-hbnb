import unittest
import sys
import os
from flask import Flask, json
from flask_restx import Api
from unittest.mock import MagicMock

# Add the parent directory of `tests_api` to `sys.path`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Add the `tests_api` directory to `sys.path`
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Importing from amenity_api in the same directory
from api.amenity_api import api, data_manager

class AmenityApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(api, path='/amenities')
        self.client = self.app.test_client()

        # Mocking the DataManager methods
        data_manager.get_all_amenities = MagicMock(return_value=\
                                                   [{'name': 'Pool'}, {'name': 'Gym'}])
        data_manager.save_amenity = MagicMock(return_value='amenity_123')
        data_manager.get_amenity = MagicMock(side_effect=lambda id: \
                                             {'name': 'Pool'} if id == 'amenity_123' else None)
        data_manager.delete_amenity = MagicMock(side_effect=lambda id: id ==\
                                                 'amenity_123')
        data_manager.update_amenity = MagicMock(side_effect=lambda id, data: id == \
                                                'amenity_123')

    def test_get_all_amenities(self):
        response = self.client.get('/amenities/')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], 'Pool')
        self.assertEqual(data[1]['name'], 'Gym')

    def test_create_amenity(self):
        response = self.client.post('/amenities/', data=json.dumps\
                                    ({'name': 'Spa'}), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Amenity successfully created')
        self.assertEqual(data['amenity_id'], 'amenity_123')

    def test_get_amenity(self):
        response = self.client.get('/amenities/amenity_123')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Pool')

        response = self.client.get('/amenities/nonexistent_id')
        self.assertEqual(response.status_code, 404)

    def test_delete_amenity(self):
        response = self.client.delete('/amenities/amenity_123')
        self.assertEqual(response.status_code, 204)

        response = self.client.delete('/amenities/nonexistent_id')
        self.assertEqual(response.status_code, 404)

    def test_update_amenity(self):
        response = self.client.put('/amenities/amenity_123', \
                                   data=json.dumps({'name': 'Sauna'}), \
                                    content_type='application/json')
        self.assertEqual(response.status_code, 204)

        response = self.client.put('/amenities/nonexistent_id', \
                                   data=json.dumps({'name': 'Sauna'}), \
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
