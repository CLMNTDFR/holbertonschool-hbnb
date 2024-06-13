#!/usr/bin/python3
# API for managing reviews

from flask import request
from flask_restx import Namespace, Resource, fields
from DataManager import DataManager

api = Namespace('reviews', description='Review related operations')

data_manager = DataManager()

# Data model for creating a review
review_model = api.model('Review', {
    'review_id': fields.String(description='Review ID'),
    'user_id': fields.String(required=True, description='User ID'),
    'place_id': fields.String(required=True, description='Place ID'),
    'rating': fields.Integer(required=True, description='Rating'),
    'comment': fields.String(description='Comment'),
    'created_at': fields.DateTime(description='Creation date'),
    'updated_at': fields.DateTime(description='Last update date')
})

@api.route('/')
class Reviews(Resource):
    @api.marshal_list_with(review_model)
    def get(self):
        """Retrieve all reviews."""
        all_reviews = data_manager.get_all_reviews()
        return all_reviews

    @api.expect(review_model, validate=True)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid request')
    def post(self):
        """Create a new review."""
        new_review_data = request.json
        review_id = data_manager.save_review(new_review_data)
        response_message = {'message': 'Review successfully created', \
                            'review_id': review_id}
        return response_message, 201

@api.route('/<string:review_id>')
class ReviewResource(Resource):
    @api.marshal_with(review_model)
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Retrieve a review by its ID."""
        review_data = data_manager.get_review(review_id)
        if review_data:
            return review_data
        else:
            api.abort(404, "Review not found")

    @api.expect(review_model, validate=True)
    @api.response(204, 'Review successfully updated')
    @api.response(400, 'Invalid request')
    @api.response(404, 'Review not found')
    def put(self, review_id):
        """Update an existing review."""
        new_review_data = request.json
        updated = data_manager.update_review(review_id, new_review_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "Review not found")

    @api.response(204, 'Review successfully deleted')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete an existing review."""
        deleted = data_manager.delete_review(review_id)
        if deleted:
            return '', 204
        else:
            api.abort(404, "Review not found")
