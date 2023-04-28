from Flask_Web import db,login_manager
from Flask_Web import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(60),nullable = False)
    budget = db.Column(db.Integer(),nullable = False, default = 1000)
    items = db.relationship('Item',backref='owned_user', lazy = True)
    
    @property
    def prettier_budget(self):
        if len(str(self.budget))>=4:
            number_with_commas = "{:,}$".format(self.budget)
            return number_with_commas
        else:
            return f'{self.budget:}$'

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self,plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self,attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password)
            
        


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