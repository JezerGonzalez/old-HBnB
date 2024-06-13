from flask import Flask, Blueprint, jsonify

# Define Flask application and blueprints
app = Flask(__name__)
countries_bp = Blueprint('countries', __name__)

# Pre-loaded countries data
countries = {
    "AF": {"name": "Afghanistan", "code": "AF"},
    "AL": {"name": "Albania", "code": "AL"},
    "DZ": {"name": "Algeria", "code": "DZ"},
    # ... truncated for brevity ...
    "ZM": {"name": "Zambia", "code": "ZM"},
    "ZW": {"name": "Zimbabwe", "code": "ZW"}
}

# Initialize country_id_counter for generating unique IDs
country_id_counter = len(countries)

@countries_bp.route('/', methods=['GET'])
def get_countries():
    return jsonify(list(countries.values())), 200

@countries_bp.route('/<string:country_code>', methods=['GET'])
def get_country(country_code):
    country = countries.get(country_code)
    if not country:
        return jsonify({"error": "Country not found"}), 404
    return jsonify(country), 200

@countries_bp.route('/<string:country_code>', methods=['PUT'])
def update_country(country_code):
    if country_code not in countries:
        return jsonify({"error": "Country not found"}), 404
    data = request.get_json()
    data['code'] = country_code  # Ensure 'code' is not changed
    countries[country_code] = data
    return jsonify(data), 200

@countries_bp.route('/<string:country_code>', methods=['DELETE'])
def delete_country(country_code):
    if country_code not in countries:
        return jsonify({"error": "Country not found"}), 404
    del countries[country_code]
    return '', 204

# Register blueprint to the main Flask application
app.register_blueprint(countries_bp, url_prefix='/countries')

# Blueprint for managing reviews
reviews_bp = Blueprint('reviews', __name__)

# Example: placeholder for reviews data
reviews = {
    "place1": [
        {"id": 1, "text": "Great place!", "rating": 5},
        {"id": 2, "text": "Needs improvement.", "rating": 3}
    ],
    "place2": [
        {"id": 3, "text": "Awesome experience!", "rating": 5}
    ]
}

@reviews_bp.route('/places/<string:place_id>/reviews', methods=['GET'])
def get_reviews(place_id):
    if place_id not in reviews:
        return jsonify({"error": "Place not found"}), 404
    return jsonify(reviews[place_id]), 200

@reviews_bp.route('/places/<string:place_id>/reviews', methods=['POST'])
def create_review(place_id):
    data = request.get_json()
    # Validate data as per your requirements
    new_review = {
        "id": len(reviews.get(place_id, [])) + 1,
        "text": data.get("text"),
        "rating": data.get("rating")
    }
    reviews.setdefault(place_id, []).append(new_review)
    return jsonify(new_review), 201

# Register reviews blueprint to the main Flask application
app.register_blueprint(reviews_bp)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
