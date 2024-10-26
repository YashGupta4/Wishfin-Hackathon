
# 🏙️ City Profile Manager

> Empowering User Profiles with City Connections! 🌆🔗👤

![City Profile Manager Banner](https://example.com/city-profile-manager-banner.png)

## 🌟 Welcome to City Profile Manager!

City Profile Manager is more than just another web app—it's your digital bridge connecting users to cities! 🌉✨ Built with Flask and cutting-edge web technologies, it streamlines the creation and management of user profiles linked to cities.

### 🎯 Our Mission

To create a seamless, intuitive, and enjoyable digital experience for users to connect with cities. Because in our interconnected world, location matters! 🌍

## ✨ Features

### 👤 User Profile Management
- 📝 Create profiles easily (name + city = done!)
- 🔍 View existing profiles at a glance.

### 🏙️ Dynamic City Management
- 🔄 Always up-to-date city list (powered by CSV).
- 🔎 Quick city search functionality.
- 🚀 Auto-updates when city data changes (no refresh needed!).

### 🛡️ Robust Security
- 🔒 CSRF protection to prevent unwanted actions.
- 🔐 Secure handling of sensitive information.

### 🚦 Rate Limiting for Smooth Performance
- 🚗 Up to 200 requests/day.
- 🏎️ Up to 50 requests/hour.
- 🚀 Up to 400 requests/minute.

### 🎨 User-Friendly Interface
- 📱 Responsive design for mobile and desktop.
- 🌈 Consistent, smooth user experience.

### 🔔 Stay Informed
- 🔄 Real-time city list updates.
- ⚡ Fast profile creation.

### 🛠️ API Endpoints
- 🏙️ `/api/cities`: Retrieve city data.
- 👥 `/api/user_profiles`: Manage user profiles.
- 🔄 `/api/cities/check-updates`: Check for city data updates.
- 🧪 `/api/test`: Verify API health.

## 🚀 Get Started with City Profile Manager

### 🧰 Prerequisites
- Python 3.7+ (latest version recommended).
- pip (for installing dependencies).
- Virtual environment (to keep dependencies isolated).

### 🏗️ Installation Guide

1. **Clone the repository:**
   \`\`\`bash
   git clone https://github.com/YashGupta4/Wishfin-Hackathon.git
   cd Wishfin-Hackathon
   \`\`\`

2. **Set up your virtual environment:**
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use \`venv\Scripts\activate\`
   \`\`\`

3. **Install the dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Set up environment variables:**
   \`\`\`bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   export SECRET_KEY=your_super_secret_key_here
   \`\`\`

5. **Run the application:**
   \`\`\`bash
   flask run
   \`\`\`

6. **Open your browser and navigate to:**
   \`\`\`
   http://localhost:5000
   \`\`\`

## 🗺️ Directory Structure

\`\`\`plaintext
city-profile-manager/
├── 📁 profile/
│   ├── 📄 reader.py
│   └── 📄 routes.py
├── 📁 templates/
│   ├── 📄 404.html
│   ├── 📄 error.html
│   ├── 📄 form.html
│   └── 📄 rate_limit.html
├── 📄 app.py
├── 📄 cities.csv
├── 📄 requirements.txt
└── 📄 README.md
\`\`\`

## 🤝 Contributing

We welcome city enthusiasts to enhance City Profile Manager! Follow these steps:

1. **Fork the repository.**
2. **Create a new branch:** 
   \`\`\`bash
   git checkout -b feature-name
   \`\`\`
3. **Add your changes:** 
   \`\`\`bash
   git commit -m 'Add new feature'
   \`\`\`
4. **Push your changes:** 
   \`\`\`bash
   git push origin feature-name
   \`\`\`
5. **Submit a pull request** and contribute to the future of city management!

## 📜 License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## 🙏 Acknowledgements

Special thanks to the following technologies:
- [Flask](https://flask.palletsprojects.com/) 🧪
- [Python](https://www.python.org/) 🐍
- [CSV Module](https://docs.python.org/3/library/csv.html) 📊
- [HTML/CSS/JavaScript](https://developer.mozilla.org/en-US/docs/Web) 🎨

## 📞 Get in Touch

Have questions, ideas, or feedback? Connect with us at [info.guptayash@gmail.com](mailto:info.guptayash@gmail.com) 📧

---

Built with ❤️ by Yash Gupta
