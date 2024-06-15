from flask import Blueprint, jsonify, request, abort
from models.users import User

user_bp = Blueprint("user", __name__)


@user_bp.route("/users", methods=["POST"])
def create_user():
    """Create a new user"""
    data = request.json
    if data is None:
        abort(400, description="No data provided (must be JSON)")
    fields = ["email", "password", "first_name", "last_name"]
    for field in fields:
        if field not in data:
            abort(400, description=f"Missing {field}")
    if data["email"] in User.emails:
        abort(400, description="Email already exists")
    user = User(data["first_name"], data["last_name"],
                data["email"], data["password"])
    user.save(user.id, "User", user)
    return jsonify(user.to_dict()), 201


@user_bp.route("/users", methods=["GET"])
def get_users():
    """Retrieve a list of all users"""
    users = User.all("User")
    if not users:
        abort(404, description="No users found")
    data = [user for user in users]
    return jsonify(data), 200


@user_bp.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    """Retrieve details of a specific user"""
    user = User.reload(user_id, "User")
    if user is None:
        abort(404, description="User not found")
    return jsonify(user), 200


@user_bp.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    """Update an existing user"""
    user = User.get(user_id, "User")
    if user is None:
        abort(404, description="User not found")
    data = request.json
    if data is None or not data:
        abort(400, description="No data provided (must be JSON)")
    if "email" in data:
        user.email = data["email"]
    if "password" in data:
        user.password = data["password"]
    if "first_name" in data:
        user.first_name = data["first_name"]
    if "last_name" in data:
        user.last_name = data["last_name"]
    user.update(user.id, "User", user)
    return jsonify(user.to_dict()), 201


@user_bp.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Delete a user"""
    user = User.get(user_id, "User")
    if user is None:
        abort(404, description="User not found")
    user.delete(user.id, "User")
    return "User deleted", 204