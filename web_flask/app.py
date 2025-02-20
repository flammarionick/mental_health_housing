#!/usr/bin/python3
"""Initialize the Flask app."""
from flask import Flask, render_template
from models import storage
from api.v1.views.app_views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the database connection after each request."""
    storage.close()

@app.route('/')
def index():
    """Serve the main page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)