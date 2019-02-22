from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class BookForm(FlaskForm):

    email = StringField('Your Email Address',validators=[Required(),Email()])
    model_name = StringField('Model Name',validators=[Required()])
    model_age = StringField('Model Age',validators = [Required()])
    event_venue = StringField('Venue of your modeling event/others',validators = [Required()])
    hours_booked = StringField('Total Hours you are booking our Model',validators = [Required()])
    model_jd = StringField('Tell us more about what the model will be doing at your event',validators = [Required()])
    submit = SubmitField('Book')
