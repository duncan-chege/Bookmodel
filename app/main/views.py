from flask import render_template
from . import main
#landing page

@main.route('/')
def index():

    title = 'Home - Book A Model ke'

    return render_template('index.html', title = title)
