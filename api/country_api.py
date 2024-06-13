#!/usr/bin/python3
# API for managing countries

from flask import request
from flask_restx import Namespace, Resource, fields
from DataManager import DataManager

api = Namespace('countries', description='Country related operations')

data_manager = DataManager()

# Data model for displaying a country
country_model = api.model('Country', {
    'country_id': fields.String(description='Country ID'),
    'name': fields.String(required=True, description='Country name'),
    'created_at': fields.DateTime(description='Creation date'),
    'updated_at': fields.DateTime(description='Last update date')
})

@api.route('/')
class Countries(Resource):
    @api.marshal_list_with(country_model)
    def get(self):
        """Retrieve all countries."""
        all_countries = data_manager.get_all_countries()
        return all_countries

    @api.expect(country_model, validate=True)
    @api.response(201, 'Country successfully created')
    @api.response(400, 'Invalid request')
    def post(self):
        """Create a new country."""
        new_country_data = request.json
        country_id = data_manager.save_country(new_country_data)
        response_message = {'message': 'Country successfully created', 'country_id': country_id}
        return response_message, 201

@api.route('/<string:country_id>')
class CountryResource(Resource):
    @api.marshal_with(country_model)
    @api.response(404, 'Country not found')
    def get(self, country_id):
        """Retrieve a country by its ID."""
        country_data = data_manager.get_country(country_id)
        if country_data:
            return country_data
        else:
            api.abort(404, "Country not found")

    @api.expect(country_model, validate=True)
    @api.response(204, 'Country successfully updated')
    @api.response(400, 'Invalid request')
    @api.response(404, 'Country not found')
    def put(self, country_id):
        """Update an existing country."""
        new_country_data = request.json
        updated = data_manager.update_country(country_id, new_country_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "Country not found")

    @api.response(204, 'Country successfully deleted')
    @api.response(404, 'Country not found')
    def delete(self, country_id):
        """Delete an existing country."""
        deleted = data_manager.delete_country(country_id)
        if deleted:
            return '', 204
        else:
            api.abort(404, "Country not found")
