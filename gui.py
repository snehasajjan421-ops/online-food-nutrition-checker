import tkinter as tk
from tkinter import messagebox, simpledialog
import data

class FoodNutritionChecker:
    """
    A simple GUI application for checking food nutrition information.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Food Nutrition Checker")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Load initial data
        self.food_data = data.load_data()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        """
        Create and arrange all GUI widgets.
        """
        # Title
        title_label = tk.Label(self.root, text="Food Nutrition Checker",
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Search frame
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Search Food:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
        self.search_entry = tk.Entry(search_frame, width=30, font=("Arial", 10))
        self.search_entry.grid(row=0, column=1, padx=5)
        self.search_entry.bind("<Return>", lambda e: self.search_food())

        search_button = tk.Button(search_frame, text="Search", command=self.search_food,
                                 bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        search_button.grid(row=0, column=2, padx=5)

        # Results text area
        self.result_text = tk.Text(self.root, height=10, width=60, wrap=tk.WORD,
                                  font=("Arial", 10))
        self.result_text.pack(pady=10)
        self.result_text.config(state=tk.DISABLED)

        # Buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=10)

        list_button = tk.Button(buttons_frame, text="List All Foods", command=self.list_foods,
                               bg="#2196F3", fg="white", font=("Arial", 10))
        list_button.grid(row=0, column=0, padx=10)

        add_button = tk.Button(buttons_frame, text="Add New Food", command=self.add_food_dialog,
                              bg="#FF9800", fg="white", font=("Arial", 10))
        add_button.grid(row=0, column=1, padx=10)

        clear_button = tk.Button(buttons_frame, text="Clear Results", command=self.clear_results,
                                bg="#9C27B0", fg="white", font=("Arial", 10))
        clear_button.grid(row=0, column=2, padx=10)

        # Exit button
        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit,
                               bg="#F44336", fg="white", font=("Arial", 10, "bold"))
        exit_button.pack(pady=10)

    def search_food(self):
        """
        Search for a food item and display its nutritional information.
        """
        food_name = self.search_entry.get().strip().lower()
        if not food_name:
            messagebox.showerror("Error", "Please enter a food name to search.")
            return

        food_info = data.get_food_info(food_name)
        if food_info:
            result = f"Nutritional Information for '{food_name.title()}':\n\n"
            result += f"• Calories: {food_info['calories']} kcal\n"
            result += f"• Protein: {food_info['protein']} g\n"
            result += f"• Carbohydrates: {food_info['carbs']} g\n"
            result += f"• Fat: {food_info['fat']} g"
            self.display_result(result)
        else:
            messagebox.showerror("Food Not Found",
                               f"'{food_name}' not found in database.\n\nClick 'List All Foods' to see available options.")

    def list_foods(self):
        """
        Display all available food items in the database.
        """
        foods = data.get_all_foods()
        if foods:
            result = f"Available Foods ({len(foods)} total):\n\n"
            for food in sorted(foods):
                result += f"• {food.title()}\n"
            self.display_result(result)
        else:
            messagebox.showinfo("No Foods", "No foods found in database.")

    def add_food_dialog(self):
        """
        Open a dialog to add a new food item.
        """
        # Create dialog window
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Food")
        dialog.geometry("300x250")
        dialog.resizable(False, False)

        # Center the dialog
        dialog.transient(self.root)
        dialog.grab_set()

        # Food name
        tk.Label(dialog, text="Food Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        name_entry = tk.Entry(dialog, width=20)
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Nutritional values
        fields = [
            ("Calories (kcal):", "calories"),
            ("Protein (g):", "protein"),
            ("Carbohydrates (g):", "carbs"),
            ("Fat (g):", "fat")
        ]

        entries = {}
        for i, (label, key) in enumerate(fields, 1):
            tk.Label(dialog, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(dialog, width=20)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[key] = entry

        def add_food():
            name = name_entry.get().strip().lower()
            if not name:
                messagebox.showerror("Error", "Food name cannot be empty.")
                return

            # Check if food already exists
            if data.get_food_info(name):
                messagebox.showerror("Error", f"'{name}' already exists in database.")
                return

            try:
                calories = int(entries['calories'].get())
                protein = float(entries['protein'].get())
                carbs = float(entries['carbs'].get())
                fat = float(entries['fat'].get())

                # Validate inputs
                if calories < 0 or protein < 0 or carbs < 0 or fat < 0:
                    messagebox.showerror("Error", "Nutritional values cannot be negative.")
                    return

                data.add_food(name, calories, protein, carbs, fat)
                self.food_data = data.load_data()  # Refresh data
                messagebox.showinfo("Success", f"'{name.title()}' added successfully!")
                dialog.destroy()

            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers for nutritional values.")

        # Buttons
        button_frame = tk.Frame(dialog)
        button_frame.grid(row=5, column=0, columnspan=2, pady=10)

        tk.Button(button_frame, text="Add", command=add_food,
                 bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Cancel", command=dialog.destroy,
                 bg="#F44336", fg="white").grid(row=0, column=1, padx=5)

    def display_result(self, text):
        """
        Display text in the results area.
        """
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, text)
        self.result_text.config(state=tk.DISABLED)

    def clear_results(self):
        """
        Clear the results text area.
        """
        self.display_result("")

def main():
    """
    Main function to run the GUI application.
    """
    root = tk.Tk()
    app = FoodNutritionChecker(root)
    root.mainloop()

if __name__ == "__main__":
    main()