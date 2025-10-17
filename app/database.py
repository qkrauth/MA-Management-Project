# database setup

from . import db

# defines inventory table item model
class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f'<InventoryItem {self.name}>'