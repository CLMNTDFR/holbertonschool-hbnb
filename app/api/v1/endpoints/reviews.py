from flask_restx import Namespace, Resource, fields

# Create a namespace for reviews API with a brief description
reviews_api = Namespace("reviews", description="Reviews operations")

# Define the data model for Review using Flask-RESTx fields
review_model = reviews_api.model(
    "Review",
    {
        "id": fields.String(
            required=True, description="The review identifier"
        ),
        "user_id": fields.String(
            required=True, description="The user identifier"
        ),
        "place_id": fields.String(
            required=True, description="The place identifier"
        ),
        "rating": fields.Integer(
            required=True, description="The rating"
        ),
        "text": fields.String(
            required=True, description="The review text"
        ),
    },
)

# In-memory database simulation for reviews
reviews_db = {}


@reviews_api.route("/")
class ReviewList(Resource):
    @reviews_api.doc("list_reviews")
    @reviews_api.marshal_list_with(review_model)
    def get(self):
        """List all reviews"""
        return list(reviews_db.values())
    # Return a list of all reviews stored in reviews_db

    @reviews_api.doc("create_review")
    @reviews_api.expect(review_model)
    @reviews_api.marshal_with(review_model, code=201)
    def post(self):
        """Create a new review"""
        new_review = reviews_api.payload
        # Extract the payload from the request
        review_id = str(len(reviews_db) + 1)
        # Generate a new ID for the review
        new_review["id"] = review_id
        # Assign the generated ID to the new review
        reviews_db[review_id] = new_review
        # Store the new review in the database
        return new_review, 201
    # Return the newly created review with HTTP status code 201


@reviews_api.route("/<string:review_id>")
class ReviewResource(Resource):
    @reviews_api.doc("get_review")
    @reviews_api.marshal_with(review_model)
    def get(self, review_id):
        """Fetch a review given its identifier"""
        review = reviews_db.get(review_id)
        # Retrieve the review from the database
        if review is None:
            reviews_api.abort(404, "Review not found")
            # Return HTTP status code 404 if review is not found
        return review
    # Return the fetched review

    @reviews_api.doc("update_review")
    @reviews_api.expect(review_model)
    @reviews_api.marshal_with(review_model)
    def put(self, review_id):
        """Update a review given its identifier"""
        if review_id not in reviews_db:
            reviews_api.abort(404, "Review not found")
            # Return HTTP status code 404 if review is not found
        updated_review = reviews_api.payload
        # Extract the payload from the request
        updated_review["id"] = review_id
        # Ensure the ID remains unchanged
        reviews_db[review_id] = updated_review
        # Update the review in the database
        return updated_review, 200
    # Return the updated review with HTTP status code 200

    @reviews_api.doc("delete_review")
    def delete(self, review_id):
        """Delete a review given its identifier"""
        if review_id in reviews_db:
            del reviews_db[review_id]
            # Delete the review from the database
            return "", 204
        # Return empty response with HTTP status code 204 for successful delet
        reviews_api.abort(404, "Review not found")
        # Return HTTP status code 404 if review is not found
