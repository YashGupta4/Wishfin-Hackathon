import csv
import os
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    return chardet.detect(raw_data)['encoding']

def read_cities():
    cities = []
    file_path = os.path.join(os.path.dirname(__file__), '..', 'city_name.csv')
    print(f"Attempting to read cities from: {file_path}")  # Debug print
    
    if not os.path.exists(file_path):
        print(f"Error: {file_path} does not exist.")
        return cities

    try:
        encoding = detect_encoding(file_path)
        print(f"Detected encoding: {encoding}")  # Debug print
        
        with open(file_path, 'r', encoding=encoding) as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"Processing row: {row}")  # Debug print
                cities.append({'id': row['id'], 'name': row['name']})
        
        print(f"Read {len(cities)} cities")  # Debug print
    except FileNotFoundError:
        print("city_name.csv file not found. Please create it with id and name columns.")
    except Exception as e:
        print(f"Error reading city_name.csv: {str(e)}")
        import traceback
        print(traceback.format_exc())  # Print full traceback
    
    return cities


def save_user_profile(name, city_id):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'user_profiles.csv')
    try:
        # Check if the file exists, if not create it with headers
        if not os.path.exists(file_path):
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['name', 'city_id'])

        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([name, city_id])
        print(f"Saved user profile: {name}, {city_id}")  # Debug print
    except Exception as e:
        print(f"Error saving user profile: {str(e)}")
        raise  # Re-raise the exception to be caught in the route handler


def read_user_profiles():
    profiles = []
    file_path = os.path.join(os.path.dirname(__file__), '..', 'user_profiles.csv')
    try:
        encoding = detect_encoding(file_path)
        with open(file_path, 'r', encoding=encoding) as file:
            reader = csv.DictReader(file)
            for row in reader:
                profiles.append({'name': row['name'], 'city_id': row['city_id']})
        print(f"Read {len(profiles)} user profiles")  # Debug print
    except FileNotFoundError:
        print("user_profiles.csv file not found.")
    except Exception as e:
        print(f"Error reading user_profiles.csv: {str(e)}")
    return profiles