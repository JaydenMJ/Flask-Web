from Flask_Web import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(60),nullable = False)
    budget = db.Column(db.Integer(),nullable = False, default = 1000)
    items = db.relationship('Item',backref='owned_user', lazy = True)
    

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    barcode = db.Column(db.String(12), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False, unique=False)
    description = db.Column(db.String(1024), nullable=False, unique=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
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