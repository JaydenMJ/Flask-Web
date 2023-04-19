from Flask_Web import app,db
from flask import render_template, redirect, url_for, flash,get_flashed_messages
from Flask_Web.models import Item, User
from Flask_Web.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home_New.html')


@app.route('/About')
@app.route('/about')

def about_page():
    items = Item.query.all()
    return render_template('about_New.html',items=items)

@app.route('/Register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password_hash=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('about_page'))
    if form.errors != {}: # No error 
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html',form=form)