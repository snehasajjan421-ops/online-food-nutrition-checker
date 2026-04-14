from flask import Flask, render_template, request, jsonify
import data
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search_food():
    food_name = request.json.get('food', '').strip().lower()
    if not food_name:
        return jsonify({'error': 'Food name cannot be empty'}), 400
    
    food_info = data.get_food_info(food_name)
    if food_info:
        return jsonify(food_info)
    else:
        return jsonify({'error': f'Food "{food_name}" not found in database'}), 404

@app.route('/api/list', methods=['GET'])
def list_foods():
    foods = data.get_all_foods()
    return jsonify({'foods': sorted(foods)})

@app.route('/api/add', methods=['POST'])
def add_food():
    try:
        food_name = request.json.get('name', '').strip().lower()
        if not food_name:
            return jsonify({'error': 'Food name cannot be empty'}), 400
        
        if data.get_food_info(food_name):
            return jsonify({'error': f'Food "{food_name}" already exists'}), 400
        
        calories = int(request.json.get('calories', 0))
        protein = float(request.json.get('protein', 0))
        carbs = float(request.json.get('carbs', 0))
        fat = float(request.json.get('fat', 0))
        
        if calories < 0 or protein < 0 or carbs < 0 or fat < 0:
            return jsonify({'error': 'Nutritional values cannot be negative'}), 400
        
        data.add_food(food_name, calories, protein, carbs, fat)
        return jsonify({'success': f'"{food_name.title()}" added to database!'})
    
    except ValueError:
        return jsonify({'error': 'Invalid numeric values'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
