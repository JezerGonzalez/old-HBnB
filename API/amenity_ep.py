from flask import Blueprint, jsonify, request, abort
from models.amenity import Amenity

amenity_bp = Blueprint("amenity", __name__)


@amenity_bp.route("/amenities", methods=["POST"])
def create_amenity():
    """Create a new amenity"""
    data = request.json
    if data is None:
        abort(400, description="No data provided (must be JSON)")
    if "name" not in data:
        abort(400, description="Missing name")
    amenity = Amenity.create(data["name"])
    return jsonify(amenity.to_dict()), 201


@amenity_bp.route("/amenities", methods=["GET"])    
def get_amenities():
    """Get all amenities"""
    amenities = Amenity.all()
    if amenities is None:
        abort(404, description="No amenities found")
    data = [amenity.to_dict() for amenity in amenities]
    return jsonify(data), 200


@amenity_bp.route("/amenities/<amenity_id>", methods=["GET"])
def get_amenity(amenity_id):
    """Get a specific amenity"""
    amenity = Amenity.get(amenity_id)
    if amenity is None:
        abort(404, description="Amenity not found")
    return jsonify(amenity.to_dict()), 200


@amenity_bp.route("/amenities/<amenity_id>", methods=["DELETE"])
def delete_amenity(amenity_id):
    """Delete a specific amenity"""
    amenity = Amenity.get(amenity_id)
    if amenity is None:
        abort(404, description="Amenity not found")
    amenity.delete()
    return jsonify(amenity.delete()), 200


@amenity_bp.route("/amenities/<amenity_id>", methods=["PUT"])
def update_amenity(amenity_id):
    """Update a specific amenity"""
    amenity = Amenity.get(amenity_id)
    if amenity is None:
        abort(404, description="Amenity not found")
    data = request.json
    if data is None:
        abort(400, description="No data provided (must be JSON)")
    if "name" not in data:
        abort(400, description="Missing name")
    amenity.name = data["name"]
    amenity.update()
    return jsonify(amenity.to_dict()), 200