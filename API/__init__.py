from flask import Flask
from .user_ep import user_bp
from .place_ep import place_bp
from .review_ep import review_bp
from .amenity_ep import amenity_bp
from .cc_ep import cc_bp

def create_app():
    app = Flask("HBnB")

    @app.route("/")
    def home():
        """HBnB home page"""
        return "Welcome to HBnB"

    app.register_blueprint(user_bp)
    app.register_blueprint(place_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(amenity_bp)
    app.register_blueprint(cc_bp)


    return app