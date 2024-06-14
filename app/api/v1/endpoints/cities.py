from flask_restx import Namespace, Resource, fields

# Create a namespace for cities API with a brief description
cities_api = Namespace("cities", description="Cities operations")

# Define the data model for City using Flask-RESTx fields
city_model = cities_api.model(
    "City",
    {
        "id": fields.String(
            required=True,
            description="The city identifier"
        ),
        "name": fields.String(
            required=True,
            description="The city name"
        ),
        "description": fields.String(
            required=True,
            description="The city description"
        ),
    },
)

# In-memory database simulation for cities
cities_db = {}


@cities_api.route("/")
class CityList(Resource):
    @cities_api.doc("list_cities")
    @cities_api.marshal_list_with(city_model)
    def get(self):
        """List all cities"""
        return list(cities_db.values())
        # Return a list of all cities in the in-memory database

    @cities_api.doc("create_city")
    @cities_api.expect(city_model)
    @cities_api.marshal_with(city_model, code=201)
    def post(self):
        """Create a new city"""
        new_city = cities_api.payload
        # Extract the payload from the request
        city_id = str(len(cities_db) + 1)
        # Generate a new ID for the city
        new_city["id"] = city_id
        # Assign the generated ID to the new city
        cities_db[city_id] = new_city
        # Store the new city in the database
        return new_city, 201
        # Return the newly created city with HTTP status code 201


@cities_api.route("/<string:city_id>")
class CityResource(Resource):
    @cities_api.doc("get_city")
    @cities_api.marshal_with(city_model)
    def get(self, city_id):
        """Fetch a city given its identifier"""
        city = cities_db.get(city_id)
        # Retrieve the city from the database
        if city is None:
            cities_api.abort(404, "City not found")
            # Return HTTP status code 404 if city is not found
        return city
        # Return the fetched city

    @cities_api.doc("update_city")
    @cities_api.expect(city_model)
    @cities_api.marshal_with(city_model)
    def put(self, city_id):
        """Update a city given its identifier"""
        if city_id not in cities_db:
            cities_api.abort(404, "City not found")
            # Return HTTP status code 404 if city is not found
        updated_city = cities_api.payload
        # Extract the payload from the request
        updated_city["id"] = city_id
        # Ensure the ID remains unchanged
        cities_db[city_id] = updated_city
        # Update the city in the database
        return updated_city
        # Return the updated city

    @cities_api.doc("delete_city")
    def delete(self, city_id):
        """Delete a city given its identifier"""
        if city_id in cities_db:
            del cities_db[city_id]
            # Delete the city from the database
            return "", 204
            # Return empty response with HTTP status code 204
        cities_api.abort(404, "City not found")
        # Return HTTP status code 404 if city is not found
