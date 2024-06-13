from flask import Flask, Blueprint, request, jsonify
from class_country import Country  # Assuming Country class is defined in class_country.py

app = Flask(__name__)

# Preload countries using Country class
countries_bp = Blueprint('countries', __name__)
countries_db = {country['code']: country for country in Country.all()}

@countries_bp.route('/', methods=['GET'])
def get_countries():
    return jsonify(list(countries_db.values())), 200

@countries_bp.route('/<string:country_code>', methods=['GET'])
def get_country(country_code):
    country = countries_db.get(country_code)
    if not country:
        return jsonify({"error": "Country not found"}), 404
    return jsonify(country), 200

# Restrict PUT and DELETE methods for countries
@countries_bp.route('/<string:country_code>', methods=['PUT', 'DELETE'])
def restricted_methods(country_code):
    return jsonify({"error": "Updating and deleting countries is not allowed"}), 405

# Blueprint for cities
cities_bp = Blueprint('cities', __name__)

cities_db = {}
city_id_counter = 1

@cities_bp.route('/', methods=['POST'])
def create_city():
    global city_id_counter
    data = request.get_json()
    data['id'] = city_id_counter
    cities_db[city_id_counter] = data
    city_id_counter += 1
    return jsonify(data), 201

@cities_bp.route('/', methods=['GET'])
def get_cities():
    cities = []
    for city_id, city_data in cities_db.items():
        country_code = city_data.get('country_code')
        country = countries_db.get(country_code)
        if country:
            city_with_country = {
                **city_data,
                'country_name': country['name']
            }
            cities.append(city_with_country)
    return jsonify(cities), 200

@cities_bp.route('/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city = cities_db.get(city_id)
    if not city:
        return jsonify({"error": "City not found"}), 404
    country_code = city.get('country_code')
    country = countries_db.get(country_code)
    if country:
        city['country_name'] = country['name']
    return jsonify(city), 200

@cities_bp.route('/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    if city_id not in cities_db:
        return jsonify({"error": "City not found"}), 404
    data = request.get_json()
    data['id'] = city_id
    cities_db[city_id] = data
    return jsonify(data), 200

@cities_bp.route('/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    if city_id not in cities_db:
        return jsonify({"error": "City not found"}), 404
    del cities_db[city_id]
    return '', 204

# Register blueprints
app.register_blueprint(countries_bp, url_prefix='/countries')
app.register_blueprint(cities_bp, url_prefix='/cities')

if __name__ == '__main__':
    app.run(debug=True)
