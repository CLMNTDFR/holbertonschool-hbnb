from flask_restx import Namespace, Resource, fields

places_api = Namespace('places', description='Places operations')

place_model = places_api.model('Place', {
    'id': fields.String(required=True, description='The place identifier'),
    'name': fields.String(required=True, description='The place name'),
    'description': fields.String(required=True, description='The place description'),
})

# In-memory database simulation
places_db = {}

@places_api.route('/')
class PlaceList(Resource):
    @places_api.doc('list_places')
    @places_api.marshal_list_with(place_model)
    def get(self):
        '''List all places'''
        return list(places_db.values())

    @places_api.doc('create_place')
    @places_api.expect(place_model)
    @places_api.marshal_with(place_model, code=201)
    def post(self):
        '''Create a new place'''
        new_place = places_api.payload
        place_id = str(len(places_db) + 1)
        new_place['id'] = place_id
        places_db[place_id] = new_place
        return new_place, 201

@places_api.route('/<string:place_id>')
class PlaceResource(Resource):
    @places_api.doc('get_place')
    @places_api.marshal_with(place_model)
    def get(self, place_id):
        '''Fetch a place given its identifier'''
        place = places_db.get(place_id)
        if place is None:
            places_api.abort(404, "Place not found")
        return place

    @places_api.doc('update_place')
    @places_api.expect(place_model)
    @places_api.marshal_with(place_model)
    def put(self, place_id):
        '''Update a place given its identifier'''
        if place_id not in places_db:
            places_api.abort(404, "Place not found")
        updated_place = places_api.payload
        updated_place['id'] = place_id
        places_db[place_id] = updated_place
        return updated_place, 200

    @places_api.doc('delete_place')
    def delete(self, place_id):
        '''Delete a place given its identifier'''
        if place_id in places_db:
            del places_db[place_id]
            return '', 204
        places_api.abort(404, "Place not found")
