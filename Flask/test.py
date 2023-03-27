from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# This code sets the URI (Uniform Resource Identifier) for the SQLite database about.db 
# in a Flask web application using SQLAlchemy. 
# The app refers to the Flask application created earlier in the code. 
# This URI will be used by SQLAlchemy to connect to the SQLite database.

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///about.db'

db = SQLAlchemy(app)

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



    


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home_New.html')


@app.route('/About')
@app.route('/about')
def about_page():
    items = Item.query.all()

    return render_template('about_New.html',items=items)


if __name__ == '__main__' :
    app.run(debug=True)