#!/usr/bin/python3
# API for managing amenities

from flask import request
from flask_restx import Namespace, Resource, fields
from DataManager import DataManager

api = Namespace('amenities', description='Amenity related operations')

data_manager = DataManager()

# Data model for creating an amenity
amenity_model = api.model('Amenity', {
    'amenity_id': fields.String(description='Amenity ID'),
    'name': fields.String(required=True, description='Amenity name'),
    'created_at': fields.DateTime(description='Creation date'),
    'updated_at': fields.DateTime(description='Last update date')
})

@api.route('/')
class Amenities(Resource):
    @api.marshal_list_with(amenity_model)
    def get(self):
        """Retrieve all amenities."""
        all_amenities = data_manager.get_all_amenities()
        return all_amenities

    @api.expect(amenity_model, validate=True)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid request')
    def post(self):
        """Create a new amenity."""
        new_amenity_data = request.json
        amenity_id = data_manager.save_amenity(new_amenity_data)
        response_message = {'message': 'Amenity successfully created', 'amenity_id': amenity_id}
        return response_message, 201

@api.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @api.marshal_with(amenity_model)
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Retrieve an amenity by its ID."""
        amenity_data = data_manager.get_amenity(amenity_id)
        if amenity_data:
            return amenity_data
        else:
            api.abort(404, "Amenity not found")

    @api.expect(amenity_model, validate=True)
    @api.response(204, 'Amenity successfully updated')
    @api.response(400, 'Invalid request')
    @api.response(404, 'Amenity not found')
    def put(self, amenity_id):
        """Update an existing amenity."""
        new_amenity_data = request.json
        updated = data_manager.update_amenity(amenity_id, new_amenity_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "Amenity not found")

    @api.response(204, 'Amenity successfully deleted')
    @api.response(404, 'Amenity not found')
    def delete(self, amenity_id):
        """Delete an existing amenity."""
        deleted = data_manager.delete_amenity(amenity_id)
        if deleted:
            return '', 204
        else:
            api.abort(404, "Amenity not found")
