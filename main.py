iimport data

def display_menu():
    """
    Display the main menu options.
    """
    print("\n=== Food Nutrition Checker ===")
    print("1. Search for food nutrition")
    print("2. List all available foods")
    print("3. Add new food to database")
    print("4. Exit")
    print("=" * 30)

def search_food():
    """
    Search for a food item and display its nutritional information.
    """
    name = input("Enter food name to search: ").strip().lower()
    if not name:
        print("Error: Food name cannot be empty.")
        return

    food_info = data.get_food_info(name)
    if food_info:
        print(f"\nNutritional Information for '{name.title()}':")
        print(f"Calories: {food_info['calories']} kcal")
        print(f"Protein: {food_info['protein']} g")
        print(f"Carbohydrates: {food_info['carbs']} g")
        print(f"Fat: {food_info['fat']} g")
    else:
        print(f"Error: Food '{name}' not found in database.")
        print("Try listing all foods to see available options.")

def list_foods():
    """
    Display all available food items in the database.
    """
    foods = data.get_all_foods()
    if foods:
        print("\nAvailable Foods:")
        for food in sorted(foods):
            print(f"- {food.title()}")
        print(f"\nTotal foods in database: {len(foods)}")
    else:
        print("No foods found in database.")

def parse_number(value, expect_int=False):
    """
    Parse a numeric value from a user input string.
    Accepts values with units like "150 kcal" or "6.5 g".
    """
    cleaned = value.lower().replace("kcal", "")
    cleaned = cleaned.replace("grams", "")
    cleaned = cleaned.replace("gram", "")
    cleaned = cleaned.replace("g", "")
    cleaned = cleaned.replace(",", "")
    cleaned = cleaned.strip()

    if not cleaned:
        raise ValueError("No numeric value provided")

    return int(cleaned) if expect_int else float(cleaned)


def add_new_food():
    """
    Add a new food item to the database with user input.
    """
    print("\nAdd New Food Item")
    name = input("Food name: ").strip().lower()
    if not name:
        print("Error: Food name cannot be empty.")
        return

    # Check if food already exists
    if data.get_food_info(name):
        print(f"Error: Food '{name}' already exists in database.")
        return

    try:
        calories = parse_number(input("Calories (kcal): "), expect_int=True)
        protein = parse_number(input("Protein (g): "))
        carbs = parse_number(input("Carbohydrates (g): "))
        fat = parse_number(input("Fat (g): "))

        # Validate inputs
        if calories < 0 or protein < 0 or carbs < 0 or fat < 0:
            print("Error: Nutritional values cannot be negative.")
            return

        data.add_food(name, calories, protein, carbs, fat)
        print(f"Success: '{name.title()}' added to database!")

    except ValueError:
        print("Error: Please enter valid numbers for nutritional values.")

def main():
    """
    Main function to run the Food Nutrition Checker application.
    """
    print("Welcome to Food Nutrition Checker!")
    print("A simple tool to check nutritional information of foods.")

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            search_food()
        elif choice == '2':
            list_foods()
        elif choice == '3':
            add_new_food()
        elif choice == '4':
            print("Thank you for using Food Nutrition Checker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()