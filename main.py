from flask import Flask
from application.routes import routes_bp

# Create a new Flask app
app = Flask(__name__, template_folder='templates')

# Register the routes blueprint with the app
app.register_blueprint(routes_bp)

# Start the app
app.run()
