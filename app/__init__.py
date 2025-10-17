from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .database import db
import os

ma = Marshmallow()

# starts flask and connects everything
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('instance.config.Config')

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)

    # Register blueprints (routes)
    from .routes.inventory_routes import inventory_bp
    from .routes.order_routes import order_bp
    from .routes.invoice_routes import invoice_bp

    app.register_blueprint(inventory_bp, url_prefix="/api/inventory")
    app.register_blueprint(order_bp, url_prefix="/api/orders")
    app.register_blueprint(invoice_bp, url_prefix="/api/invoices")

    with app.app_context():
        db.create_all()

    return app
