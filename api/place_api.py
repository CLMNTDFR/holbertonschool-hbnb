#!/usr/bin/python3
# API for managing places

from flask import request
from flask_restx import Namespace, Resource, fields
from DataManager import DataManager

api = Namespace('places', description='Place related operations')

data_manager = DataManager()

# Data model for creating a place
place_model = api.model('Place', {
    'place_id': fields.String(description='Place ID'),
    'name': fields.String(required=True, description='Place name'),
    'description': fields.String(description='Place description'),
    'address': fields.String(description='Place address'),
    'city_id': fields.String(required=True, description='City ID'),
    'latitude': fields.Float(description='Latitude'),
    'longitude': fields.Float(description='Longitude'),
    'host_id': fields.String(required=True, description='Host ID'),
    'number_of_rooms': fields.Integer(description='Number of rooms'),
    'number_of_bathrooms': fields.Integer(description='Number of bathrooms'),
    'price_per_night': fields.Float(description='Price per night'),
    'max_guests': fields.Integer(description='Maximum number of guests'),
    'amenity_ids': fields.List(fields.String, description='List of \
                               amenity IDs'),
    'created_at': fields.DateTime(description='Creation date'),
    'updated_at': fields.DateTime(description='Last update date')
})

@api.route('/')
class Places(Resource):
    @api.marshal_list_with(place_model)
    def get(self):
        """Retrieve all places."""
        all_places = data_manager.get_all_places()
        return all_places

    @api.expect(place_model, validate=True)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid request')
    def post(self):
        """Create a new place."""
        new_place_data = request.json
        place_id = data_manager.save_place(new_place_data)
        response_message = {'message': 'Place successfully created', \
                            'place_id': place_id}
        return response_message, 201

@api.route('/<string:place_id>')
class PlaceResource(Resource):
    @api.marshal_with(place_model)
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Retrieve a place by its ID."""
        place_data = data_manager.get_place(place_id)
        if place_data:
            return place_data
        else:
            api.abort(404, "Place not found")

    @api.expect(place_model, validate=True)
    @api.response(204, 'Place successfully updated')
    @api.response(400, 'Invalid request')
    @api.response(404, 'Place not found')
    def put(self, place_id):
        """Update an existing place."""
        new_place_data = request.json
        updated = data_manager.update_place(place_id, new_place_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "Place not found")

    @api.response(204, 'Place successfully deleted')
    @api.response(404, 'Place not found')
    def delete(self, place_id):
        """Delete an existing place."""
        deleted = data_manager.delete_place(place_id)
        if deleted:
            return '', 204
        else:
            api.abort(404, "Place not found")
