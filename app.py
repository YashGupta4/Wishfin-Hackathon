from flask import Flask, flash, render_template, send_from_directory, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from profile.routes import profile_bp
from profile.reader import read_cities, save_user_profile, read_user_profiles
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wishfin'

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
@limiter.limit("400 per minute")
def index():
    return profile_bp.profile_form()

# Add a simple API endpoint for testing
@app.route('/api/test', methods=['GET'])
@limiter.limit("400 per minute")
def test_api():
    return jsonify({"message": "This is a test API endpoint"}), 200

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# New API routes
@app.route('/api/cities', methods=['GET'])
@limiter.limit("400 per minute")
def get_cities():
    cities = read_cities()
    return jsonify(cities), 200

@app.route('/api/user_profiles', methods=['GET'])
@limiter.limit("400 per minute")
def get_user_profiles():
    profiles = read_user_profiles()
    return jsonify(profiles), 200

@app.route('/api/user_profiles', methods=['POST'])
@limiter.limit("400 per minute")
def add_user_profile():
    data = request.json
    if not data or 'name' not in data or 'city_id' not in data:
        return jsonify({"error": "Invalid data. Please provide name and city_id."}), 400
    
    try:
        save_user_profile(data['name'], data['city_id'])
        return jsonify({"message": "User profile saved successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Global variable to store the last modification time of the CSV file
last_modified_time = 0

# Function to check if the CSV file has been modified
def csv_modified():
    global last_modified_time
    csv_path = os.path.join(os.path.dirname(__file__), 'city_name.csv')
    current_modified_time = os.path.getmtime(csv_path)
    if current_modified_time > last_modified_time:
        last_modified_time = current_modified_time
        return True
    return False

@app.route('/api/cities/check-updates', methods=['GET'])
@limiter.limit("60 per minute")  # This route keeps its original rate limit
def check_city_updates():
    if csv_modified():
        cities = read_cities()
        return jsonify({"updated": True, "cities": cities}), 200
    return jsonify({"updated": False}), 200

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({"error": "Rate limit exceeded", "message": str(e)}), 429

@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)