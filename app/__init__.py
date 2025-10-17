# starts flask and connects everything

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os

# creating database and serialize tools
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    load_dotenv() # loads environment variables from .env
    app = Flask(__name__, instance_relative_config=True) # creates flask app object

    # database setup and turns off warning feature
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mashop.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # connects to this flask app
    db.init_app(app)
    ma.init_app(app)

    # imports inventory route and registers them so flask knows the endpoint
    from .routes.inventory_routes import inventory_bp
    app.register_blueprint(inventory_bp, url_prefix='api/inventory')

    return app