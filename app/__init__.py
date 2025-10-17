# starts flask and connects everything

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from .database import db
import os

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)

    #database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mashop.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    from .routes.inventory_routes import inventory_bp
    app.register_blueprint(inventory_bp, url_prefix='api/inventory')

    return app