from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User,
from wtforms import ValidationError

class RegistrationForm(FlaskForm):

    email = StringField('Email',validators=[Required(),Email()])
    username = StringField('username',validators = [Required()])
    agency = StringField('Agency Name',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('join us today')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('Sorry there is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Sorry that username is taken')

    def validate_agency(self,data_field):
        if User.query.filter_by(agency = data_field.data).first():
            raise ValidationError('Sorry NO agency with that name registered')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    agency = AgencyField('Agency',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
