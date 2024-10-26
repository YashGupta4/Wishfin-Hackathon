from flask import Blueprint, render_template, request, redirect, url_for, flash
from .reader import read_cities, save_user_profile

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/', methods=['GET', 'POST'])
def profile_form():
    cities = read_cities()
    print(f"Cities passed to template: {cities}")  # Debug print
    if request.method == 'POST':
        name = request.form.get('name')
        city_id = request.form.get('city')
        if name and city_id:
            save_user_profile(name, city_id)
            flash('Profile saved successfully!', 'success')
            return redirect(url_for('profile.profile_form'))
        else:
            flash('Please fill out all fields.', 'error')
    return render_template('form.html', cities=cities)