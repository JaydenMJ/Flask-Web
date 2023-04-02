from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# This code sets the URI (Uniform Resource Identifier) for the SQLite database about.db 
# in a Flask web application using SQLAlchemy. 
# The app refers to the Flask application created earlier in the code. 
# This URI will be used by SQLAlchemy to connect to the SQLite database.

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///about.db'

db = SQLAlchemy(app)






