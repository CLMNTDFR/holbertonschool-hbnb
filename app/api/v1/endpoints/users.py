from flask_restx import Namespace, Resource, fields

# Create a namespace for users API with a brief description
user_ns = Namespace("users", description="User operations")

# Define the data model for User using Flask-RESTx fields
user_model = user_ns.model(
    "User",
    {
        "id": fields.String(
            required=True, description="The user identifier"
        ),
        "email": fields.String(
            required=True, description="The user email"
        ),
        "first_name": fields.String(
            required=True, description="The user first name"
        ),
        "last_name": fields.String(
            required=True, description="The user last name"
        ),
    },
)

# In-memory database simulation for users
users_db = {}


@user_ns.route("/")
class UserList(Resource):
    @user_ns.doc("list_users")
    @user_ns.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        return list(users_db.values())
        # Return a list of all users stored in users_db

    @user_ns.doc("create_user")
    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        new_user = user_ns.payload
        # Extract the payload from the request
        user_id = str(len(users_db) + 1)
        # Generate a new ID for the user
        new_user["id"] = user_id
        # Assign the generated ID to the new user
        users_db[user_id] = new_user
        # Store the new user in the database
        return new_user, 201
        # Return the newly created user with HTTP status code 201


@user_ns.route("/<string:user_id>")
class UserResource(Resource):
    @user_ns.doc("get_user")
    @user_ns.marshal_with(user_model)
    def get(self, user_id):
        """Fetch a user given its identifier"""
        user = users_db.get(user_id)
        # Retrieve the user from the database
        if user is None:
            user_ns.abort(404, "User not found")
            # Return HTTP status code 404 if user is not found
        return user
        # Return the fetched user

    @user_ns.doc("update_user")
    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model)
    def put(self, user_id):
        """Update a user given its identifier"""
        if user_id not in users_db:
            user_ns.abort(404, "User not found")
            # Return HTTP status code 404 if user is not found
        updated_user = user_ns.payload
        # Extract the payload from the request
        updated_user["id"] = user_id
        # Ensure the ID remains unchanged
        users_db[user_id] = updated_user
        # Update the user in the database
        return updated_user, 200
        # Return the updated user with HTTP status code 200

    @user_ns.doc("delete_user")
    def delete(self, user_id):
        """Delete a user given its identifier"""
        if user_id in users_db:
            del users_db[user_id]
            # Delete the user from the database
            return "", 204
            # Return empty response with HTTP status code 204
        user_ns.abort(404, "User not found")
        # Return HTTP status code 404 if user is not found
