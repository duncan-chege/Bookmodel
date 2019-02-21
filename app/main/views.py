from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User
from .. import db

#landing page

@main.route('/')
def index():

    title = 'Home - Book A Model '

    return render_template('index.html', title = title)

@main.route('/categories')
def categories():

    title = 'Model Categories'

    return render_template('categories.html',title=title)

@main.route('/categories/male')
def male():
    title = 'Male Models'
    return render_template('male.html', title = title)

@main.route('/male/profile')
def profile():
    title = 'Male Profile'
    return render_template('profile.html', title = title)
