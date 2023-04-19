from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import length, Email, EqualTo, DataRequired, ValidationError
from Flask_Web.models import User
class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check): # This is a custom validator for username. fixed syntax
        # can do validate_<field_name> to create a custom validator for that field
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username.')
        
    def validate_email_address(self, email_address_to_check): # This is a custom validator for email. fixed syntax
        # can do validate_<field_name> to create a custom validator for that field
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already exists! Please try a different email address.')
        
    
    username = StringField(label='Username: ', validators=[length(min=2, max=30),DataRequired()])
    email = StringField(label='Email: ',validators=[Email(), DataRequired()])
    password = PasswordField(label='Password: ', validators=[length(min=6), DataRequired()])
    confirm_password = PasswordField(label='Confirm Password: ', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Sign Up')




