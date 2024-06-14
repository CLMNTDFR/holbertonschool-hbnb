from flask_restx import Namespace, Resource, fields

# Create a namespace for countries API with a brief description
countries_api = Namespace("countries", description="Country operations")

# Define the data model for Country using Flask-RESTx fields
country_model = countries_api.model(
    "Country",
    {
        "id": fields.String(
            required=True,
            description="The country identifier"
        ),
        "name": fields.String(
            required=True,
            description="The country name"
        ),
    },
)

# In-memory database simulation for countries
countries_db = {}


@countries_api.route("/")
class CountryList(Resource):
    @countries_api.doc("list_countries")
    @countries_api.marshal_list_with(country_model)
    def get(self):
        """List all countries"""
        return list(countries_db.values()), 200
        # Return a list of all countries with HTTP status code 200

    @countries_api.doc("create_country")
    @countries_api.expect(country_model)
    @countries_api.marshal_with(country_model, code=201)
    def post(self):
        """Create a new country"""
        new_country = countries_api.payload
        # Extract the payload from the request
        country_id = str(len(countries_db) + 1)
        # Generate a new ID for the country
        new_country["id"] = country_id
        # Assign the generated ID to the new country
        countries_db[country_id] = new_country
        # Store the new country in the database
        return new_country, 201
        # Return the newly created country with HTTP status code 201


@countries_api.route("/<string:country_id>")
class CountryResource(Resource):
    @countries_api.doc("get_country")
    @countries_api.marshal_with(country_model)
    def get(self, country_id):
        """Fetch a country given its identifier"""
        country = countries_db.get(country_id)
        # Retrieve the country from the database
        if country is None:
            countries_api.abort(404, "Country not found")
            # Return HTTP status code 404 if country is not found
        return country, 200
        # Return the fetched country with HTTP status code 200

    @countries_api.doc("update_country")
    @countries_api.expect(country_model)
    @countries_api.marshal_with(country_model)
    def put(self, country_id):
        """Update a country given its identifier"""
        if country_id not in countries_db:
            countries_api.abort(404, "Country not found")
            # Return HTTP status code 404 if country is not found
        updated_country = countries_api.payload
        # Extract the payload from the request
        updated_country["id"] = country_id
        # Ensure the ID remains unchanged
        countries_db[country_id] = updated_country
        # Update the country in the database
        return updated_country, 200
        # Return the updated country with HTTP status code 200

    @countries_api.doc("delete_country")
    def delete(self, country_id):
        """Delete a country given its identifier"""
        if country_id in countries_db:
            del countries_db[country_id]
            # Delete the country from the database
            return "", 204
            # Return empty response with HTTP status code 204
        countries_api.abort(404, "Country not found")
        # Return HTTP status code 404 if country is not found
