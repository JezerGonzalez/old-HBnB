from flask import Flask, jsonify, abort
from models.class_country import Country
from models.city import City

app = Flask('city_country')

countries = Country.get_all_countries()
cities = City.get_all_cities()

@app.route('/countries', methods=['GET'])
def get_all_countries():
    """Endpoint para obtener todos los países."""
    return jsonify({'countries': countries})


@app.route('/countries/<string:country_code>', methods=['GET'])
def get_country_by_code(country_code):
    """Endpoint para obtener un país por su código de país."""
    country = next((c for c in countries if c['code'] == country_code), None)
    if country is None:
        abort(404, description="Country not found.")
    return jsonify({'country': country})


@app.route('/countries/<string:country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    """Endpoint para obtener todas las ciudades de un país específico por su código de país."""
    country_cities = [city for city in cities if city['country_code'] == country_code]
    return jsonify({'cities': country_cities})


@app.route('/cities/<int:city_id>', methods=['GET'])
def get_city_by_id(city_id):
    """Endpoint para obtener una ciudad por su ID de ciudad."""
    city = next((city for city in cities if city['id'] == city_id), None)
    if city is None:
        abort(404, description="City not found.")
    return jsonify({'city': city})
