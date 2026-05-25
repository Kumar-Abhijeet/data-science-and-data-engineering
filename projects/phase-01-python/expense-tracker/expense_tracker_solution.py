"""
Expense Tracker — Reference Solution

IMPORTANT: Only look at this after you have built your own version.
Compare your solution with this one — both can be correct.
"""
import csv
import os
import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "expenses.csv")
CATEGORIES = ["food", "travel", "bills", "entertainment", "health", "shopping", "other"]
CSV_FIELDS = ["id", "date", "category", "amount", "description"]


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    expenses = []
    with open(DATA_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["amount"] = float(row["amount"])
            expenses.append(row)
    return expenses


def save_expenses(expenses):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(expenses)


def get_next_id(expenses):
    return max((e["id"] for e in expenses), default=0) + 1


def add_expense(expenses):
    print("\n--- Add Expense ---")

    # Date
    date_str = input(f"Date (YYYY-MM-DD) [today]: ").strip()
    if not date_str:
        date_str = datetime.date.today().isoformat()
    else:
        try:
            datetime.date.fromisoformat(date_str)
        except ValueError:
            print("Invalid date format. Using today.")
            date_str = datetime.date.today().isoformat()

    # Category
    print(f"Categories: {', '.join(CATEGORIES)}")
    while True:
        category = input("Category: ").strip().lower()
        if category in CATEGORIES:
            break
        print(f"  Please choose from: {', '.join(CATEGORIES)}")

    # Amount
    while True:
        try:
            amount = float(input("Amount (₹): ").strip())
            if amount <= 0:
                raise ValueError
            break
        except ValueError:
            print("  Enter a valid positive number.")

    # Description
    description = input("Description (optional): ").strip()

    expense = {
        "id": get_next_id(expenses),
        "date": date_str,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    save_expenses(expenses)

    cat_total = sum(e["amount"] for e in expenses if e["category"] == category)
    print(f"\n✓ Added ₹{amount:,.2f} ({category}). Running total: ₹{cat_total:,.2f}")


def display_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n" + "=" * 70)
    print(f"{'ID':<5} {'Date':<12} {'Category':<15} {'Amount':>10}  Description")
    print("-" * 70)
    for e in expenses:
        print(f"{e['id']:<5} {e['date']:<12} {e['category']:<15} ₹{e['amount']:>9,.2f}  {e['description']}")
    print("=" * 70)
    total = sum(e["amount"] for e in expenses)
    print(f"{'Total':<33} ₹{total:>9,.2f}")


def display_summary(expenses):
    if not expenses:
        print("\nNo expenses to summarise.")
        return

    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    grand_total = sum(summary.values())
    sorted_summary = sorted(summary.items(), key=lambda x: x[1], reverse=True)

    print("\n" + "=" * 45)
    print(f"{'Category':<20} {'Total':>10}  {'Share':>7}")
    print("-" * 45)
    for category, total in sorted_summary:
        pct = (total / grand_total) * 100
        print(f"{category:<20} ₹{total:>9,.2f}  {pct:>6.1f}%")
    print("=" * 45)
    print(f"{'GRAND TOTAL':<20} ₹{grand_total:>9,.2f}")


def delete_expense(expenses):
    display_expenses(expenses)
    if not expenses:
        return

    try:
        exp_id = int(input("\nEnter ID to delete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return

    match = next((e for e in expenses if e["id"] == exp_id), None)
    if not match:
        print(f"No expense with ID {exp_id}.")
        return

    confirm = input(f"Delete '{match['description']}' (₹{match['amount']:,.2f})? [y/N]: ").strip().lower()
    if confirm == "y":
        expenses.remove(match)
        save_expenses(expenses)
        print("✓ Deleted.")
    else:
        print("Cancelled.")


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
