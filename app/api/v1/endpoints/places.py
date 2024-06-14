from flask_restx import Namespace, Resource, fields

# Create a namespace for places API with a brief description
places_api = Namespace("places", description="Places operations")

# Define the data model for Place using Flask-RESTx fields
place_model = places_api.model(
    "Place",
    {
        "id": fields.String(
            required=True, description="The place identifier"
        ),
        "name": fields.String(
            required=True, description="The place name"
        ),
        "description": fields.String(
            required=True, description="The place description"
        ),
    },
)

# In-memory database simulation for places
places_db = {}


@places_api.route("/")
class PlaceList(Resource):
    @places_api.doc("list_places")
    @places_api.marshal_list_with(place_model)
    def get(self):
        """List all places"""
        return list(places_db.values())
    # Return a list of all places stored in places_db

    @places_api.doc("create_place")
    @places_api.expect(place_model)
    @places_api.marshal_with(place_model, code=201)
    def post(self):
        """Create a new place"""
        new_place = places_api.payload
        # Extract the payload from the request
        place_id = str(len(places_db) + 1)
        # Generate a new ID for the place
        new_place["id"] = place_id
        # Assign the generated ID to the new place
        places_db[place_id] = new_place
        # Store the new place in the database
        return new_place, 201
    # Return the newly created place with HTTP status code 201


@places_api.route("/<string:place_id>")
class PlaceResource(Resource):
    @places_api.doc("get_place")
    @places_api.marshal_with(place_model)
    def get(self, place_id):
        """Fetch a place given its identifier"""
        place = places_db.get(place_id)
        # Retrieve the place from the database
        if place is None:
            places_api.abort(404, "Place not found")
            # Return HTTP status code 404 if place is not found
        return place
    # Return the fetched place

    @places_api.doc("update_place")
    @places_api.expect(place_model)
    @places_api.marshal_with(place_model)
    def put(self, place_id):
        """Update a place given its identifier"""
        if place_id not in places_db:
            places_api.abort(404, "Place not found")
            # Return HTTP status code 404 if place is not found
        updated_place = places_api.payload
        # Extract the payload from the request
        updated_place["id"] = place_id
        # Ensure the ID remains unchanged
        places_db[place_id] = updated_place
        # Update the place in the database
        return updated_place, 200
    # Return the updated place with HTTP status code 200

    @places_api.doc("delete_place")
    def delete(self, place_id):
        """Delete a place given its identifier"""
        if place_id in places_db:
            del places_db[place_id]
            # Delete the place from the database
            return "", 204
        # Return empty response with HTTP status code 204 for successful delet
        places_api.abort(404, "Place not found")
        # Return HTTP status code 404 if place is not found
