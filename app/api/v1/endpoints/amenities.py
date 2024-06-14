from flask_restx import Namespace, Resource, fields

# Create a namespace for amenities API with a brief description
amenities_api = Namespace("amenities", description="Amenities operations")

# Define the data model for Amenity using Flask-RESTx fields
amenity_model = amenities_api.model(
    "Amenity",
    {
        "id": fields.String(
            required=True,
            description="The amenity identifier"
        ),
        "name": fields.String(
            required=True,
            description="The amenity name"
        ),
    },
)

# In-memory database simulation for amenities
amenities_db = {}


@amenities_api.route("/")
class AmenityList(Resource):
    @amenities_api.doc("list_amenities")
    @amenities_api.marshal_list_with(amenity_model)
    def get(self):
        """List all amenities"""
        return list(amenities_db.values())

    @amenities_api.doc("create_amenity")
    @amenities_api.expect(amenity_model)
    @amenities_api.marshal_with(amenity_model, code=201)
    def post(self):
        """Create a new amenity"""
        new_amenity = amenities_api.payload
        # Extract the payload from the request
        amenity_id = str(len(amenities_db) + 1)
        # Generate a new ID for the amenity
        new_amenity["id"] = amenity_id
        # Assign the generated ID to the new amenity
        amenities_db[amenity_id] = new_amenity
        # Store the new amenity in the database
        return new_amenity, 201
        # Return the created amenity with HTTP status code 201


@amenities_api.route("/<string:amenity_id>")
class AmenityResource(Resource):
    @amenities_api.doc("get_amenity")
    @amenities_api.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Fetch an amenity given its identifier"""
        return amenities_db.get(amenity_id, None) or (None, 404)
        # Return the amenity or 404 if not found

    @amenities_api.doc("update_amenity")
    @amenities_api.expect(amenity_model)
    @amenities_api.marshal_with(amenity_model)
    def put(self, amenity_id):
        """Update an amenity given its identifier"""
        if amenity_id in amenities_db:
            # Check if the amenity exists
            amenities_db[amenity_id] = amenities_api.payload
            # Update the amenity with the new payload
            amenities_db[amenity_id]["id"] = amenity_id
            # Ensure the ID remains unchanged
            return amenities_db[amenity_id]
            # Return the updated amenity
        return None, 404
        # Return 404 if the amenity ID doesn't exist

    @amenities_api.doc("delete_amenity")
    def delete(self, amenity_id):
        """Delete an amenity given its identifier"""
        if amenity_id in amenities_db:
            # Check if the amenity exists
            del amenities_db[amenity_id]
            # Delete the amenity from the database
            return "", 204
            # Return empty response with HTTP status code 204
        return "", 404
        # Return 404 if the amenity ID doesn't exist
