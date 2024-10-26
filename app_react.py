from flask import Flask, flash, render_template, send_from_directory, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from profile.routes import profile_bp
import os
from profile.reader import read_cities, save_user_profile  # Add this import
import os
from flask_cors import CORS  # Add this import


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Initialize the rate limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)

# Register the blueprint
app.register_blueprint(profile_bp)

# Add a route for the root URL
@app.route('/')
@limiter.limit("4 per minute")  # Updated to 4 requests per minute
def index():
    return profile_bp.profile_form()

# Add a new route to fetch cities
@app.route('/api/cities', methods=['GET'])
@limiter.limit("4 per minute")
def get_cities():
    cities = read_cities()
    return jsonify(cities)

# Add a route for saving the profile
@app.route('/api/profile', methods=['POST'])
@limiter.limit("4 per minute")
def save_profile():
    data = request.json
    try:
        save_user_profile(data['name'], data['cityId'])
        return jsonify({"message": "Profile saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Failed to save profile", "message": str(e)}), 500
    

# Add a simple API endpoint for testing
@app.route('/api/test', methods=['GET'])
@limiter.limit("4 per minute")  # Apply the same rate limit to this endpoint
def test_api():
    return jsonify({"message": "This is a test API endpoint"}), 200

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(429)  # Add an error handler for rate limit exceeded
def ratelimit_handler(e):
    return jsonify({"error": "Rate limit exceeded", "message": str(e)}), 429

@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)