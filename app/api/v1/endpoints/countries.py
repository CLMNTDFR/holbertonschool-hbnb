# app/api/v1/endpoints/countries.py
from flask_restx import Namespace, Resource, fields

countries_api = Namespace('countries', description='Country operations')

country_model = countries_api.model('Country', {
    'id': fields.String(required=True, description='The country identifier'),
    'name': fields.String(required=True, description='The country name')
})

# In-memory database simulation
countries_db = {}

@countries_api.route('/')
class CountryList(Resource):
    @countries_api.doc('list_countries')
    @countries_api.marshal_list_with(country_model)
    def get(self):
        '''List all countries'''
        return list(countries_db.values()), 200

    @countries_api.doc('create_country')
    @countries_api.expect(country_model)
    @countries_api.marshal_with(country_model, code=201)
    def post(self):
        '''Create a new country'''
        new_country = countries_api.payload
        country_id = str(len(countries_db) + 1)
        new_country['id'] = country_id
        countries_db[country_id] = new_country
        return new_country, 201

@countries_api.route('/<string:country_id>')
class CountryResource(Resource):
    @countries_api.doc('get_country')
    @countries_api.marshal_with(country_model)
    def get(self, country_id):
        '''Fetch a country given its identifier'''
        country = countries_db.get(country_id)
        if country is None:
            countries_api.abort(404, "Country not found")
        return country, 200

    @countries_api.doc('update_country')
    @countries_api.expect(country_model)
    @countries_api.marshal_with(country_model)
    def put(self, country_id):
        '''Update a country given its identifier'''
        if country_id not in countries_db:
            countries_api.abort(404, "Country not found")
        updated_country = countries_api.payload
        updated_country['id'] = country_id
        countries_db[country_id] = updated_country
        return updated_country, 200

    @countries_api.doc('delete_country')
    def delete(self, country_id):
        '''Delete a country given its identifier'''
        if country_id in countries_db:
            del countries_db[country_id]
            return '', 204
        countries_api.abort(404, "Country not found")
