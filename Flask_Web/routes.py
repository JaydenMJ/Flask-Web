from Flask_Web import app,db
from flask import render_template, redirect, url_for, flash,get_flashed_messages
from Flask_Web.models import Item, User
from Flask_Web.forms import RegisterForm, LoginForm
from flask_login import login_user

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
                              password=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('about_page'))
    if form.errors != {}: # No error 
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html',form=form)

@app.route('/Login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username = form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password = form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('about_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')


    return render_template('login.html',form=form)
