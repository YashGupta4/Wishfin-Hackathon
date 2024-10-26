
# City Profile Manager

![City Profile Manager Logo](https://example.com/city-profile-manager-logo.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Rate Limiting](#rate-limiting)
- [Testing](#testing)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)

## Introduction

City Profile Manager is a Flask-based web application designed to manage user profiles linked with cities. It offers a user-friendly interface for adding user information, dynamically populating a list of cities, and maintaining user data.

## Features

### 1. User Profile Management
- Allows creating and storing user profiles with names and city associations.
- Provides functionality to view existing user profiles.

### 2. Dynamic City List
- Fetches and displays an up-to-date list of cities from a CSV file.
- Supports search functionality for city selection.
- Automatically reflects changes when the city list is updated.

### 3. Rate Limiting
- Prevents abuse by limiting the number of requests per endpoint.
- Customizable rate limits ensure fair usage across users.

### 4. API Endpoints
- RESTful APIs for managing user profiles and cities.
- Includes endpoints for fetching, creating, and checking updates.

### 5. Error Handling
- Custom error pages for 404 and rate-limit exceedance.
- Proper error responses for API interactions.

### 6. Security
- Implements CSRF protection for form submissions.
- Ensures secure handling of sensitive information.

### 7. Responsive Design
- Provides a mobile-friendly interface for seamless usage.
- Supports responsive elements across devices.

## Installation

1. **Clone the Repository:**
   \`\`\`bash
   git clone https://github.com/yourusername/city-profile-manager.git
   cd city-profile-manager
   \`\`\`

2. **Create a Virtual Environment:**
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use \`venv\Scripts\activate\`
   \`\`\`

3. **Install Dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Set Up Environment Variables:**
   \`\`\`bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   export SECRET_KEY=your_secret_key_here
   \`\`\`

5. **Run the Application:**
   \`\`\`bash
   flask run
   \`\`\`

## Usage

1. Navigate to \`http://localhost:5000\` in your web browser.
2. Fill out the form with a name and select a city from the dropdown list.
3. Submit the form to save the user profile.
4. Use the search bar to quickly find cities.

## API Endpoints

### **GET /api/cities**
- Retrieves the list of available cities.

### **GET /api/user_profiles**
- Fetches all user profiles.

### **POST /api/user_profiles**
- Creates a new user profile.
  - Required fields: \`name\` (string), \`city_id\` (string).

### **GET /api/cities/check-updates**
- Checks if the city list has been updated.

### **GET /api/test**
- Simple test endpoint to verify API functionality.

## Rate Limiting

To prevent excessive use:
- **200 requests/day**, **50 requests/hour**, and **400 requests/minute** for most endpoints.
- **60 requests/minute** for the city update check endpoint.

## Testing

To run tests for API endpoints:
\`\`\`bash
python -m unittest discover tests
\`\`\`

This will execute all test cases in the \`tests\` directory.

## Security

- A secret key is used for session management and CSRF protection. Use a strong, unique key in production.
- Inputs are sanitized to prevent XSS attacks.
- HTTPS is recommended in production for data encryption.

## Contributing

We welcome contributions! Follow these steps:
1. Fork the repository.
2. Create a new branch for your changes.
3. Make changes with descriptive commit messages.
4. Push to your fork and submit a pull request.

Ensure your code follows the project's coding standards and includes necessary tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
