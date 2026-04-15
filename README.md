# Food Nutrition Checker

A simple Python application to check nutritional information of various foods. This project demonstrates basic Python programming concepts including file I/O, data structures, functions, and GUI development with Tkinter.

## Features

- **Search Foods**: Look up nutritional information by food name
- **List Foods**: View all available foods in the database
- **Add Foods**: Insert new food items with their nutritional data
- **CLI Interface**: Command-line interface for terminal users
- **GUI Interface**: Simple graphical interface using Tkinter
- **Data Persistence**: Stores food data in JSON format

## Nutritional Information Displayed

- Calories (kcal)
- Protein (grams)
- Carbohydrates (grams)
- Fat (grams)

## Project Structure

```
food_nutrition_checker/
├── main.py          # CLI version of the application
├── gui.py           # GUI version using Tkinter
├── data.py          # Data management functions
├── food_data.json   # JSON database file (created automatically)
└── README.md        # This file
```

## Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python installations)
- Flask (for web version)

## Installation

1. Clone or download the project files
2. Ensure Python 3.6+ is installed on your system
3. No additional packages required (uses only standard library)

## How to Run

### CLI Version (Command Line Interface)

```bash
python main.py
```

**Menu Options:**
1. Search for food nutrition
2. List all available foods
3. Add new food to database
4. Exit

### GUI Version (Graphical User Interface)

```bash
python gui.py
```

**Features:**
- Search bar for food lookup
- Buttons to list all foods or add new foods
- Clear results button
- User-friendly dialog boxes for adding foods

### Web Version (Browser Interface)

```bash
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000/` in your browser.

**Features:**
- Browser-based food search
- List all foods with clickable entries
- Add new food items through a web form
- Live feedback and validation

## Sample Usage

### CLI Version

```
=== Food Nutrition Checker ===
1. Search for food nutrition
2. List all available foods
3. Add new food to database
4. Exit
==============================
Enter your choice (1-4): 1
Enter food name to search: apple

Nutritional Information for 'Apple':
Calories: 52 kcal
Protein: 0.2 g
Carbohydrates: 14.0 g
Fat: 0.2 g

Press Enter to continue...
```

### GUI Version

1. Run `python gui.py`
2. Enter "banana" in the search box and click "Search"
3. Nutritional information will appear in the text area
4. Click "List All Foods" to see all available items
5. Click "Add New Food" to add a new food item

## Sample Data

The application comes with sample data including:
- Apple
- Banana
- Chicken Breast
- Rice
- Broccoli

## Adding New Foods

You can add new foods through either interface:

**CLI:** Choose option 3 and follow the prompts
**GUI:** Click "Add New Food" button and fill in the dialog

All nutritional values should be entered as positive numbers.

## Data Storage

- Food data is stored in `food_data.json`
- File is created automatically on first run
- Data persists between application runs
- JSON format makes it easy to edit manually if needed

## Error Handling

- Handles missing food searches gracefully
- Validates numerical inputs for nutritional data
- Prevents duplicate food entries
- Shows appropriate error messages

## Code Structure

### data.py
- `load_data()`: Loads food data from JSON file
- `save_data()`: Saves food data to JSON file
- `add_food()`: Adds new food to database
- `get_food_info()`: Retrieves specific food information
- `get_all_foods()`: Returns list of all food names

### main.py (CLI)
- `display_menu()`: Shows menu options
- `search_food()`: Handles food search functionality
- `list_foods()`: Displays all available foods
- `add_new_food()`: Adds new food with validation
- `main()`: Main application loop

### gui.py (GUI)
- `FoodNutritionChecker` class: Main GUI application
- Methods for search, list, add functionality
- Tkinter widgets for user interaction

## Learning Objectives

This project demonstrates:
- Modular code organization
- File I/O operations
- Dictionary and JSON data structures
- Function decomposition
- Error handling and validation
- GUI development with Tkinter
- User input processing
- Data persistence

## Future Enhancements

Possible improvements:
- Search suggestions/auto-complete
- Food categories (fruits, vegetables, meats, etc.)
- Nutritional calculations (daily totals)
- Import/export functionality
- Unit conversions
- More detailed nutritional information

## License

This project is open source and available under the MIT License.