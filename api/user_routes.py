from flask import Blueprint, request, jsonify
from models.user import User
from models.base_model import db
import re

user_bp = Blueprint("user_bp", __name__)


def is_valid_email(email):
    """
    Validate the email format using a regex pattern.

    Args:
        email (str): The email to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$"
    return re.search(regex, email) is not None


@user_bp.route("/", methods=["POST"])
def create_user():
    """
    Endpoint to create a new user.

    Expects a JSON payload with 'email', 'password',
    'first_name', and 'last_name'.

    Returns:
        JSON response with the created user's data
        and status code 201 if successful,
        or an error message and appropriate status
        code if validation fails.
    """
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    first_name = data.get("first_name")
    last_name = data.get("last_name")

    if not email or not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400
    if not first_name or not last_name:
        return jsonify({"error": "First name and last name are required"}), 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "Email already exists"}), 409

    new_user = User(
        email=email, password=password, first_name=first_name, last_name=last_name
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201


@user_bp.route("/", methods=["GET"])
def get_users():
    """
    Endpoint to retrieve all users.

    Returns:
        JSON response with a list of all users
        and status code 200.
    """
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200


@user_bp.route("/<string:user_id>", methods=["GET"])
def get_user(user_id):
    """
    Endpoint to retrieve a specific user by ID.

    Args:
        user_id (str): The ID of the user to retrieve.

    Returns:
        JSON response with the user's data and status
        code 200 if found,
        or an error message and status code 404 if
        the user is not found.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200


@user_bp.route("/<string:user_id>", methods=["PUT"])
def update_user(user_id):
    """
    Endpoint to update an existing user.

    Args:
        user_id (str): The ID of the user to update.

    Expects a JSON payload with optional 'email',
    'password', 'first_name', and 'last_name'.

    Returns:
        JSON response with the updated user's data and status
        code 200 if successful,
        or an error message and appropriate status code if
        validation fails or the user is not found.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    first_name = data.get("first_name")
    last_name = data.get("last_name")

    if email and not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if password:
        user.password = password
    if email:
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"error": "Email already exists"}), 409
        user.email = email

    db.session.commit()
    return jsonify(user.to_dict()), 200


@user_bp.route("/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """
    Endpoint to delete a user by ID.

    Args:
        user_id (str): The ID of the user to delete.

    Returns:
        Empty response with status code 204 if successful,
        or an error message and status code 404 if the user is not found.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return "", 204
