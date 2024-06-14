# app/api/v1/endpoints/amenities.py
from flask_restx import Namespace, Resource, fields

amenities_api = Namespace('amenities', description='Amenities operations')

amenity_model = amenities_api.model('Amenity', {
    'id': fields.String(required=True, description='The amenity identifier'),
    'name': fields.String(required=True, description='The amenity name')
})

# In-memory database simulation
amenities_db = {}

@amenities_api.route('/')
class AmenityList(Resource):
    @amenities_api.doc('list_amenities')
    @amenities_api.marshal_list_with(amenity_model)
    def get(self):
        '''List all amenities'''
        return list(amenities_db.values())

    @amenities_api.doc('create_amenity')
    @amenities_api.expect(amenity_model)
    @amenities_api.marshal_with(amenity_model, code=201)
    def post(self):
        '''Create a new amenity'''
        new_amenity = amenities_api.payload
        amenity_id = str(len(amenities_db) + 1)
        new_amenity['id'] = amenity_id
        amenities_db[amenity_id] = new_amenity
        return new_amenity, 201

@amenities_api.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @amenities_api.doc('get_amenity')
    @amenities_api.marshal_with(amenity_model)
    def get(self, amenity_id):
        '''Fetch an amenity given its identifier'''
        return amenities_db.get(amenity_id, None) or (None, 404)

    @amenities_api.doc('update_amenity')
    @amenities_api.expect(amenity_model)
    @amenities_api.marshal_with(amenity_model)
    def put(self, amenity_id):
        '''Update an amenity given its identifier'''
        if amenity_id in amenities_db:
            amenities_db[amenity_id] = amenities_api.payload
            amenities_db[amenity_id]['id'] = amenity_id
            return amenities_db[amenity_id]
        return None, 404

    @amenities_api.doc('delete_amenity')
    def delete(self, amenity_id):
        '''Delete an amenity given its identifier'''
        if amenity_id in amenities_db:
            del amenities_db[amenity_id]
            return '', 204
        return '', 404
