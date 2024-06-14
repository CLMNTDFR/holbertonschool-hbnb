from flask_restx import Namespace, Resource, fields

cities_api = Namespace('cities', description='Cities operations')

city_model = cities_api.model('City', {
    'id': fields.String(required=True, description='The city identifier'),
    'name': fields.String(required=True, description='The city name'),
    'description': fields.String(required=True, description='The city description'),
})

# In-memory database simulation
cities_db = {}

@cities_api.route('/')
class CityList(Resource):
    @cities_api.doc('list_cities')
    @cities_api.marshal_list_with(city_model)
    def get(self):
        '''List all cities'''
        return list(cities_db.values())

    @cities_api.doc('create_city')
    @cities_api.expect(city_model)
    @cities_api.marshal_with(city_model, code=201)
    def post(self):
        '''Create a new city'''
        new_city = cities_api.payload
        city_id = str(len(cities_db) + 1)
        new_city['id'] = city_id
        cities_db[city_id] = new_city
        return new_city, 201

@cities_api.route('/<string:city_id>')
class CityResource(Resource):
    @cities_api.doc('get_city')
    @cities_api.marshal_with(city_model)
    def get(self, city_id):
        '''Fetch a city given its identifier'''
        city = cities_db.get(city_id)
        if city is None:
            cities_api.abort(404, "City not found")
        return city

    @cities_api.doc('update_city')
    @cities_api.expect(city_model)
    @cities_api.marshal_with(city_model)
    def put(self, city_id):
        '''Update a city given its identifier'''
        if city_id not in cities_db:
            cities_api.abort(404, "City not found")
        updated_city = cities_api.payload
        updated_city['id'] = city_id
        cities_db[city_id] = updated_city
        return updated_city

    @cities_api.doc('delete_city')
    def delete(self, city_id):
        '''Delete a city given its identifier'''
        if city_id in cities_db:
            del cities_db[city_id]
            return '', 204
        cities_api.abort(404, "City not found")
