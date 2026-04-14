import json
import os

# File to store food data
DATA_FILE = 'food_data.json'

def load_data():
    """
    Load food data from JSON file.
    Returns a dictionary of food items with their nutritional information.
    """
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Error: Invalid JSON file. Starting with empty data.")
            return {}
    else:
        # Create initial data file with sample foods
        initial_data = {
            "apple": {"calories": 52, "protein": 0.2, "carbs": 14.0, "fat": 0.2},
            "banana": {"calories": 89, "protein": 1.1, "carbs": 23.0, "fat": 0.3},
            "chicken breast": {"calories": 165, "protein": 31.0, "carbs": 0.0, "fat": 3.6},
            "rice": {"calories": 130, "protein": 2.7, "carbs": 28.0, "fat": 0.3},
            "broccoli": {"calories": 34, "protein": 2.8, "carbs": 7.0, "fat": 0.4}
        }
        save_data(initial_data)
        return initial_data

def save_data(data):
    """
    Save food data to JSON file.
    """
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_food(name, calories, protein, carbs, fat):
    """
    Add a new food item to the database.
    """
    data = load_data()
    data[name.lower()] = {
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fat": fat
    }
    save_data(data)

def get_food_info(name):
    """
    Get nutritional information for a specific food.
    Returns the food data if found, None otherwise.
    """
    data = load_data()
    return data.get(name.lower())

def get_all_foods():
    """
    Get a list of all available food names.
    """
    data = load_data()
    return list(data.keys())