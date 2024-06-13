#!/usr/bin/python3


# Initialize Flask app and Flask-RESTx API
from flask import Flask
from flask_restx import Api
from api.place_api import api as place_ns
from api.user_api import api as user_ns
from api.review_api import api as review_ns
from api.amenity_api import api as amenity_ns
from api.country_api import api as country_ns
from api.city_api import api as city_ns

app = Flask(__name__)
api = Api(app)

# Add namespaces for different endpoints
api.add_namespace(place_ns)
api.add_namespace(user_ns)
api.add_namespace(review_ns)
api.add_namespace(amenity_ns)
api.add_namespace(country_ns)
api.add_namespace(city_ns)

if __name__ == "__main__":
    app.run(debug=True)
