from flask import Blueprint, jsonify, request, abort
from models.users import User
from models.class_reviews import Review

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
    user = User.create(data["first_name"], data["last_name"],
                       data["email"], data["password"])
    return jsonify(user.to_dict()), 201


@user_bp.route("/users", methods=["GET"])
def get_users(user_id):
    """Get all users"""
    users = User.get(user_id)
    if users is None:
        abort(404, description="User not found")
    data = [user.to_dict() for user in users]
    return jsonify(data), 200


@user_bp.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    """Get a specific user"""
    user = User.get(user_id)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user.to_dict()), 200


@user_bp.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    """Update a specific user"""
    user = User.get(user_id)
    if user is None:
        abort(404, description="User not found")
    data = request.json
    if data is None:
        abort(400, description="No data provided (must be JSON)")
    for key, value in data.items():
        if key in data and key is not user_id:
            setattr(user, key, value)
    user.update()
    return jsonify(user.to_dict()), 201


@user_bp.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Delete a specific user"""
    user = User.get(user_id)
    if user is None:
        abort(404, description="User not found")
    user.delete()
    return "Delete successful", 204
