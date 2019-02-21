from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User, Detail
from .. import db
from .forms import BookForm
from ..email import mail_message


#landing page

@main.route('/')
def index():


    title = 'Home - Book A Model '

    return render_template('index.html', title = title)

@main.route('/categories', methods=["POST", "GET"])
def categories():

    title = 'Model Categories'

    book_form = BookForm()
    if book_form.validate_on_submit():
        detail = Detail(email = book_form.email.data,model_name = book_form.model_name.data, model_age = book_form.model_age.data,event_venue = book_form.event_venue.data,hours_booked = book_form.hours_booked.data,model_jd = book_form.model_jd.data)
        db.session.add(detail)
        db.session.commit()

        mail_message("Welcome to BOOKMODEL","email/welcome_user",detail.email,detail=detail)

    return render_template('categories.html',title=title,book_form=book_form)
