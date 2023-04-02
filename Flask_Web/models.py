from Flask_Web import db
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    barcode = db.Column(db.String(12), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False, unique=False)
    description = db.Column(db.String(1024), nullable=False, unique=False)

    def __repr__(self):
        return f'Item {self.name}'
    # Python shell python
    # from market import app,db
    # app.app_context().push()
    # db.create_all()

    # for item in Item.query.all():
# ...     item.name
# ...     item.barcode
# ...     item.price
# ...     item.id

#     >>> for item in Item.query.filter_by(price=500):
# ...     item.name