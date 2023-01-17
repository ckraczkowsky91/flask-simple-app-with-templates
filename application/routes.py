from flask import render_template, Blueprint

# Create a new blueprint
routes_bp = Blueprint('routes', __name__)

# Define a route for the basic template page
@routes_bp.route('/basic-template')
def basic_template():
    return render_template('basic-template.html')

# Define two routes for the setup page, so that
# it will be accessible through '/' and '/setup'
@routes_bp.route('/')
@routes_bp.route('/setup')
def first_page():
    return render_template('part-one.html')

# Define a route for the punchline page
@routes_bp.route('/punchline')
def second_page():
    return render_template('part-two.html')
