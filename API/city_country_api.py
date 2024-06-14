from flask import Flask, jsonify, abort
from class_country import Country

app = Flask(__name__)


places = [
    {'id': 1, 'name': 'Place A', 'country_code': 'US', 'description': 'Description of Place A'},
    {'id': 2, 'name': 'Place B', 'country_code': 'CA', 'description': 'Description of Place B'}
]


@app.route('/places', methods=['GET'])
def get_all_places():
    return jsonify({'places': places})


@app.route('/places/<int:place_id>', methods=['GET'])
def get_place_by_id(place_id):
    place = next((p for p in places if p['id'] == place_id), None)
    if place is None:
        abort(404, description="Place not found.")
    return jsonify({'place': place})


@app.route('/countries', methods=['GET'])
def get_countries():
    countries = Country.get_all_countries()
    return jsonify({'countries': countries})

if __name__ == '__main__':
    app.run(debug=True)
