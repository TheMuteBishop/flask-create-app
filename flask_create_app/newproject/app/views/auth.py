from flask import Blueprint, render_template
from flask import request, url_for


from app import db

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

# The Home page is accessible to anyone
@auth_blueprint.route('/')
def index():
    return render_template('index.html')