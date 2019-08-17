from flask import Blueprint, render_template
from flask import request, url_for


from app import db

main_blueprint = Blueprint('main', __name__, template_folder='templates')

# The Home page is accessible to anyone
@main_blueprint.route('/')
def index():
    return render_template('index.html')
