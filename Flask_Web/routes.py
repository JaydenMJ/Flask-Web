from Flask_Web import app
from flask import render_template
from Flask_Web.models import Item


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home_New.html')


@app.route('/About')
@app.route('/about')

def about_page():
    items = Item.query.all()
    return render_template('about_New.html',items=items)

