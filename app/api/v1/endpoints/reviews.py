from flask_restx import Namespace, Resource, fields

reviews_api = Namespace('reviews', description='Reviews operations')

review_model = reviews_api.model('Review', {
    'id': fields.String(required=True, description='The review identifier'),
    'user_id': fields.String(required=True, description='The user identifier'),
    'place_id': fields.String(required=True, description='The place identifier'),
    'rating': fields.Integer(required=True, description='The rating'),
    'text': fields.String(required=True, description='The review text'),
})

# In-memory database simulation
reviews_db = {}

@reviews_api.route('/')
class ReviewList(Resource):
    @reviews_api.doc('list_reviews')
    @reviews_api.marshal_list_with(review_model)
    def get(self):
        '''List all reviews'''
        return list(reviews_db.values())

    @reviews_api.doc('create_review')
    @reviews_api.expect(review_model)
    @reviews_api.marshal_with(review_model, code=201)
    def post(self):
        '''Create a new review'''
        new_review = reviews_api.payload
        review_id = str(len(reviews_db) + 1)
        new_review['id'] = review_id
        reviews_db[review_id] = new_review
        return new_review, 201

@reviews_api.route('/<string:review_id>')
class ReviewResource(Resource):
    @reviews_api.doc('get_review')
    @reviews_api.marshal_with(review_model)
    def get(self, review_id):
        '''Fetch a review given its identifier'''
        review = reviews_db.get(review_id)
        if review is None:
            reviews_api.abort(404, "Review not found")
        return review

    @reviews_api.doc('update_review')
    @reviews_api.expect(review_model)
    @reviews_api.marshal_with(review_model)
    def put(self, review_id):
        '''Update a review given its identifier'''
        if review_id not in reviews_db:
            reviews_api.abort(404, "Review not found")
        updated_review = reviews_api.payload
        updated_review['id'] = review_id
        reviews_db[review_id] = updated_review
        return updated_review, 200

    @reviews_api.doc('delete_review')
    def delete(self, review_id):
        '''Delete a review given its identifier'''
        if review_id in reviews_db:
            del reviews_db[review_id]
            return '', 204
        reviews_api.abort(404, "Review not found")
