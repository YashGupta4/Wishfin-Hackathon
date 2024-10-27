import os
from functools import wraps
from flask import Flask, flash, render_template, send_from_directory, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache
from dotenv import load_dotenv
from profile.routes import profile_bp
from profile.reader import read_cities, save_user_profile, read_user_profiles
import jwt
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-jwt-secret-key')
port = int(os.getenv("PORT", 5000))

# Initialize the rate limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["2000 per day", "500 per hour"],
    storage_uri="memory://"
)

# Initialize caching
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Register the blueprint
app.register_blueprint(profile_bp)

# Token verification function
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=["HS256"])
            # You might want to add additional checks here, like verifying the user still exists
        except jwt.ExpiredSignatureError: # code
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401

        return f(*args, **kwargs)

    return decorated

@app.route('/')
@limiter.limit("400 per minute")
def index():
    return profile_bp.profile_form()

@app.route('/api/test', methods=['GET'])
@limiter.limit("400 per minute")
@token_required
def test_api():
    return jsonify({"message": "This is a test API endpoint"}), 200

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/api/cities', methods=['GET'])
@limiter.limit("400 per minute")
@token_required
def get_cities():
    cities = read_cities()
    return jsonify(cities), 200

@app.route('/api/user_profiles', methods=['GET'])
@limiter.limit("400 per minute")
@token_required
def get_user_profiles():
    profiles = read_user_profiles()
    return jsonify(profiles), 200

@app.route('/api/user_profiles', methods=['POST'])
@limiter.limit("400 per minute")
@token_required
def add_user_profile():
    data = request.json
    if not data:
        return jsonify({"error": "Empty submission. Please provide data."}), 400
    
    name = data.get('name')
    city_id = data.get('city_id')
    
    if not name or not city_id:
        missing_fields = []
        if not name:
            missing_fields.append('name')
        if not city_id:
            missing_fields.append('city_id')
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400
    
    if not name.strip():
        return jsonify({"error": "Name cannot be empty or just whitespace."}), 400
    
    try:
        save_user_profile(data['name'], data['city_id'])
        cache.delete('cities')  # Invalidate the cities cache
        return jsonify({"message": "User profile saved successfully"}), 201
    except Exception as e:
        app.logger.error(f"Error saving user profile: {str(e)}")
        return jsonify({"error": "An error occurred while saving the user profile."}), 500

# Global variable to store the last modification time of the CSV file
last_modified_time = 0

# Function to check if the CSV file has been modified
def csv_modified():
    global last_modified_time
    csv_path = os.path.join(os.path.dirname(__file__), 'city_name.csv')
    current_modified_time = os.path.getmtime(csv_path)
    if current_modified_time > last_modified_time:
        last_modified_time = current_modified_time
        cache.delete('cities')  # Invalidate the cities cache
        return True
    return False

@app.route('/api/cities/check-updates', methods=['GET'])
@limiter.limit("60 per minute")
@token_required
def check_city_updates():
    if csv_modified():
        cities = read_cities()
        return jsonify({"updated": True, "cities": cities}), 200
    return jsonify({"updated": False}), 200

@app.route('/api/token', methods=['POST'])
def generate_token():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return  jsonify({'message': 'Could not verify', 'WWW-Authenticate': 'Basic realm="Login required!"'}), 401

    if auth.username == os.getenv('API_USERNAME') and auth.password == os.getenv('API_PASSWORD'):
        token = jwt.encode({'user': auth.username, 'exp': datetime.utcnow() + timedelta(hours=24)},
                           app.config['JWT_SECRET_KEY'])
        return jsonify({'token': token})

    return jsonify({'message': 'Could not verify', 'WWW-Authenticate': 'Basic realm="Login required!"'}), 401

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({"error": "Rate limit exceeded", "message": str(e)}), 429

@app.errorhandler(Exception)
def handle_error(e):
    app.logger.error(f"An unexpected error occurred: {str(e)}")
    return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
