
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///about.db'
app.config['SECRET_KEY'] = 'd432cdd4ef8bd1da8d584f82'
db = SQLAlchemy(app)

from Flask_Web import routes