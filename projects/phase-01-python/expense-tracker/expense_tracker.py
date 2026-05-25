"""
Expense Tracker — Main Application
Project 1 of Phase 1: Python Foundations

Instructions:
- Read each TODO comment and implement the function.
- Start with the simpler functions first (add, display).
- The skeleton is provided to guide your structure.
- Refer to Days 1-12 theory if you need a refresher.
"""
import csv
import os
import datetime

# ─── Configuration ────────────────────────────────────────────────────────────

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "expenses.csv")
CATEGORIES = ["food", "travel", "bills", "entertainment", "health", "shopping", "other"]
CSV_FIELDS = ["id", "date", "category", "amount", "description"]


# ─── Data Layer ───────────────────────────────────────────────────────────────

def load_expenses():
    """
    Load expenses from the CSV file.
    Returns a list of expense dictionaries.
    If the file does not exist, return an empty list.
    """
    # TODO: Check if DATA_FILE exists using os.path.exists()
    # TODO: If it exists, open it with csv.DictReader and return list of rows
    #       Remember to convert 'amount' to float and 'id' to int
    # TODO: If it does not exist, return []
    pass   # replace with your implementation


def save_expenses(expenses):
    """
    Save the list of expenses to CSV.
    Creates the data/ directory if it doesn't exist.
    """
    # TODO: Use os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    # TODO: Open DATA_FILE with csv.DictWriter, write header, then all rows
    pass   # replace with your implementation


# ─── Core Functions ───────────────────────────────────────────────────────────

def get_next_id(expenses):
    """Return the next available ID (max existing ID + 1, or 1 if empty)."""
    # TODO: If expenses is empty, return 1
    # TODO: Otherwise return max(e['id'] for e in expenses) + 1
    pass


def add_expense(expenses):
    """
    Prompt the user for expense details, validate, append, and save.
    """
    print("\n--- Add Expense ---")

    # TODO: Ask for date (default today if blank), validate format YYYY-MM-DD
    # TODO: Ask for category, validate against CATEGORIES list
    # TODO: Ask for amount, validate it is a positive float
    # TODO: Ask for description (optional)
    # TODO: Create expense dict with next id, append to expenses, save
    # TODO: Print confirmation with amount and running category total
    pass


def display_expenses(expenses):
    """
    Print all expenses in a formatted table.
    """
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n" + "=" * 70)
    print(f"{'ID':<5} {'Date':<12} {'Category':<15} {'Amount':>10}  Description")
    print("-" * 70)

    # TODO: Loop through expenses and print each row
    # TODO: Format amount as ₹X,XXX.XX
    pass

    print("=" * 70)
    total = sum(e["amount"] for e in expenses)
    print(f"{'Total':<33} ₹{total:>9,.2f}")


def display_summary(expenses):
    """
    Print a category-wise summary with totals and percentages.
    """
    if not expenses:
        print("\nNo expenses to summarise.")
        return

    # TODO: Build a dict: {category: total_amount}
    # TODO: Sort by total descending
    # TODO: Print formatted summary table with % of total
    pass


def delete_expense(expenses):
    """
    Ask for an expense ID and remove it from the list.
    """
    display_expenses(expenses)
    if not expenses:
        return

    # TODO: Ask for ID, validate it exists
    # TODO: Find the expense, confirm deletion, remove from list, save
    pass


# ─── Menu ─────────────────────────────────────────────────────────────────────

def show_menu():
    print("\n" + "=" * 35)
    print("       EXPENSE TRACKER")
    print("=" * 35)
    print("  1. Add expense")
    print("  2. View all expenses")
    print("  3. View summary")
    print("  4. Delete expense")
    print("  5. Exit")
    print("-" * 35)


def main():
    """Main application loop."""
    expenses = load_expenses()
    print(f"Loaded {len(expenses)} expense(s).")

    while True:
        show_menu()
        choice = input("Choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            display_expenses(expenses)
        elif choice == "3":
            display_summary(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("\nGoodbye! Your expenses have been saved.")
            break
        else:
            print("Invalid choice. Enter 1–5.")


if __name__ == "__main__":
    main()
