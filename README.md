
# 🏙️ Wishfin

> Wishfin Hackathon! 🌆🔗👤

![hackathon]![image](https://github.com/user-attachments/assets/bfc7417f-d72d-4816-a5bd-92ef982101cb)


## 🌟 Welcome to City profile Manager!

City Profile Manager is more than just another web app—it's your digital bridge connecting users to cities! 🌉✨ Built with Flask and cutting-edge web technologies, it streamlines the creation and management of user profiles linked to cities.


## ✨ Features

### 👤 User Profile Management
- 📝 Quick Setup:Create profiles easily (name + city = done!)
- 🔍 View Profiles: See all saved profiles with just one click..

### 🏙️ Dynamic City Management
- 🔄 Latest Cities: Always up-to-date city list (powered by CSV).
- 🔎 Search in Dropdown: Use the built-in search box in the dropdown to quickly find your city.
- 🚀 Automatic Updates: Auto-updates when city data changes (no refresh needed!).

### 🚦 Rate Limiting for Smooth Performance
- 🚀 Fast & Smooth: Up to 400 requests/minute.

### 🎨 User-Friendly Interface
- 🌈 Consistent, smooth user experience.

### 🔔 Stay Informed
- 🔄 City Updates: Stay in sync with real-time city list changes.
- ⚡ Quick Profile Creation: Add profiles quickly without any hassle.

### 🛡️ Robust Security
- 🔒 Protects against unauthorized actions, keeping your data safe.
- 🔐 Your information is securely stored and managed.


### 🛠️ API Endpoints
- 🏙️ `/api/cities`: Retrieve city data.
- 👥 `/api/user_profiles`: Manage user profiles.
- 🔄 `/api/cities/check-updates`: Check for city data updates.
- 🧪 `/api/test`: Verify API health.

Testing using Postman
1. For City Names
![image](https://github.com/user-attachments/assets/a1e81e9f-b087-4985-87d4-96d7eadaee53)

2.For user-profiles
![image](https://github.com/user-attachments/assets/09fa6c1c-e7e8-45f9-be48-e270c304c61e)

3.For checking updates in city_names.csv
   ![image](https://github.com/user-attachments/assets/917d7d49-07aa-4b9c-ba9a-ca67b6a78a7f)

4. For Api Testing
   ![image](https://github.com/user-attachments/assets/61e21f4f-4234-4a9b-9c0b-4347e34a4fc9)


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
   python app.py
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
