from flask import Blueprint, jsonify, request, abort
from models.class_reviews import Review
from models.places import Place
from models.users import User


review_bp = Blueprint("review", __name__)


@review_bp.route("/places/<place_id>/reviews", methods=["POST"])
def create_review(place_id):
    """Creates a new review"""
    place = Place.get(place_id)
    if place is None:
        abort(404, description="Place not found")
    data = request.json
    if data is None:
        abort(400, description="Missing data")
    fields = ["user_id", "rating", "review"]
    for field in fields:
        if field not in data:
            abort(400, description=f"Missing {field}")
    user = User.get(data["user_id"])
    if user is None:
        abort(404, description="User not found")
    if user.id == place.host_id:
        abort(400, description="Host cannot review their own place")
    review = Review.create(data["user_id"], data["place_id"], data["text"],
                           data["rating"])
    place.add_review(review)
    user.add_review(review)
    return jsonify(review.to_dict()), 201


@review_bp.route("/reviews/<review_id>", methods=["GET"])
def get_review(review_id):
    """Gets a review by id"""
    review = Review.get(review_id)
    if review is None:
        abort(404, description="Review not found")
    return jsonify(review.to_dict()), 200


@review_bp.route("/reviews/<review_id>", methods=["PUT"])
def update_review(review_id):
    """Update a review"""
    review = Review.get(review_id)
    if review is None:
        abort(404, description="Review not found")
    review.review = request.json["review"]
    review.rating = request.json["rating"]
    return jsonify(review.to_dict), 201


@review_bp.route("/review/<review_id>", methods=["DELETE"])
def delete_review(review_id):
    """Deletes a review"""
    review = Review.get(review_id)
    if review is None:
        abort(404, description="Review not found")
    review.delete()
    return "Review successfuly deleted", 204


@review_bp.route("/places/<place_id>/reviews", methods=["GET"])
def get_place_reviews(place_id):
    """Retrieve all reviews for a specific place"""
    place = Place.get(place_id)
    if place is None:
        abort(404, description="Place not found")
    if place.reviews is None:
        abort(404, description="Place has no reviews")
    place_reviews = [review.to_dict() for review in place.reviews]
    return jsonify(place_reviews), 200


@review_bp.route("/users/<user_id>/reviews", methods=["GET"])
def get_user_reviews(user_id):
    """Retrieve all reviews written by a specific user"""
    user = User.get(user_id)
    if user is None:
        abort(404, description="User not found")
    if user.reviews is None:
        abort(404, description="User has no reviews")
    user_reviews = [review.to_dict() for review in user.reviews]
    return jsonify(user_reviews), 200
