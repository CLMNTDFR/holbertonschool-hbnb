import logging
from flask import Flask, jsonify
from flask_restx import Api
from .api.v1.endpoints.users import user_ns as users_api
from .api.v1.endpoints.places import places_api
from .api.v1.endpoints.reviews import reviews_api
from .api.v1.endpoints.amenities import amenities_api
from .api.v1.endpoints.cities import cities_api
from .api.v1.endpoints.countries import countries_api

# Configure logging level to DEBUG
logging.basicConfig(level=logging.DEBUG)

def create_app():
    # Initialize Flask application
    app = Flask(__name__)

    # Initialize Flask-RESTx API extension with versioning and documentation
    api = Api(app, version='1.0', title='HBnB API',
              description='A simple API for HBnB Evolution project')

    # Add namespaces (API endpoints) to the API
    api.add_namespace(users_api, path='/api/v1/users')
    api.add_namespace(places_api, path='/api/v1/places')
    api.add_namespace(reviews_api, path='/api/v1/reviews')
    api.add_namespace(amenities_api, path='/api/v1/amenities')
    api.add_namespace(cities_api, path='/api/v1/cities')
    api.add_namespace(countries_api, path='/api/v1/countries')

    # Define a route for the home endpoint
    @app.route('/')
    def home():
        return jsonify(message="Welcome to the HBnB API")

    return app

if __name__ == "__main__":
    # If this script is executed directly, create and run the Flask app
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
