from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import length, Email, EqualTo, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='Username: ', validators=[length(min=2, max=30),DataRequired()])
    email = StringField(label='Email: ',validators=[Email(), DataRequired()])
    password = PasswordField(label='Password: ', validators=[length(min=6), DataRequired()])
    confirm_password = PasswordField(label='Confirm Password: ', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Sign Up')




