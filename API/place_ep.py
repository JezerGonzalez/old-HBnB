from flask import Blueprint, jsonify, request, abort
from models.places import Place
from models.class_reviews import Review
from models.users import User
from models.amenity import Amenity
from models.city import City

place_bp = Blueprint("place", __name__)


@place_bp.route("/places", methods=["POST"])
def create_place(self):
    """Create a place"""
    data = request.json
    if data is None:
        abort(400, description="Missing data")
    fields = ["name", "description", "longitute", "latitude", "address",
              "price", "city_id", "max_guests", "rooms", "bathrooms",
              "amenities", "host_id"]
    for field in fields:
        if field not in data:
            abort(400, description=f"Missing {fields}")
    host = User.get(data["host_id"])
    if host not in data:
        abort(400, description=f"User not found")
    place = Place.create(data["name"], data["description"], data["address"],
                         data["city_id"], data["latitude"], data["longitude"],
                         data["rooms"], data["bathrooms"], data["price"],
                         data["max_guests"])
    place.host_id = data["host_id"]
    host.add_place(place)
    place.add_amenity(amenity for amenity in data["amenities"])
    return self.__dict()


@place_bp.route("/places", methods=["GET"])
def get_places():
    """get all places"""
    places = Place.all()
    if places is None:
        abort(404, description="No places found")
    data = [place.to_dict() for place in places]
    return jsonify(data), 200


@place_bp.route("/places/<place_id>", methods=["GET"])
def get_place(place_id):
    """get a place"""
    place = Place.get(place_id)
    if place is None:
        abort(404, description="Place not found")
    return jsonify(place.to_dict()), 200


@place_bp.route("/places/<place_id>", methods=["PUT"])
def update_place(place_id):
    """update a place"""
    place = Place.get(place_id)
    if place is None:
        abort(404, description="Place not found")
    data = request.json
    if data is None:
        abort(400, description="Missing data")
    for key, value in data.items():
        if key in data and key is not place_id:
            setattr(place, key, value)
    place.update()
    return jsonify(place.to_dict()), 201


@place_bp.route("/places/<place_id>", methods=["DELETE"])
def delete_place(place_id):
    """delete a place"""
    place = Place.get(place_id)
    if place is None:
        abort(404, description="Place not found")
    host = User.get(place.host_id)
    host.places.remove(place)
    place.delete()
    return "Place deleted", 204