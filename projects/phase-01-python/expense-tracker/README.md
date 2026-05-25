# Project 1 — Expense Tracker CLI

**Phase:** Python Foundations  
**Skills Practiced:** Variables, Lists, Dictionaries, Loops, Functions, File Handling, Exception Handling

---

## 📋 Project Overview

Build a command-line Expense Tracker that allows a user to:
- Add expenses (date, category, amount, description)
- View all expenses in a formatted table
- View a summary by category
- Save expenses to a CSV file and load them on startup
- Delete an expense by ID

---

## 🎯 Business Context

Every professional tracks expenses — from personal budgets to business travel claims.
This project simulates a simple version of tools like Expensify or Zoho Expense.

---

## 🗂️ Folder Structure

```text
expense-tracker/
├── README.md
├── requirements.txt
├── expense_tracker.py      ← main application
├── utils.py                ← helper functions
└── data/
    └── expenses.csv        ← persistent storage (created on first run)
```

---

## ⚙️ Features to Build

### Minimum (required)
- [x] Add an expense (category, amount, description)
- [x] List all expenses in a table
- [x] Category-wise summary with totals
- [x] CSV persistence (load on start, save after changes)

### Stretch (optional)
- [ ] Filter expenses by date range
- [ ] Filter by category
- [ ] Monthly budget limit with alert
- [ ] Export summary report to a text file

---

## 🧪 Sample Interaction

```
=== EXPENSE TRACKER ===
1. Add expense
2. View all expenses
3. View summary
4. Delete expense
5. Exit
Choice: 1

Date (YYYY-MM-DD) [today]: 
Category (food/travel/bills/entertainment/other): food
Amount: 450
Description: Lunch at Cafe

✓ Expense added. Total: ₹450.00 in food

---

ID   Date         Category        Amount    Description
--   ----------   --------        ------    -----------
1    2024-03-15   food            ₹450.00   Lunch at Cafe
2    2024-03-15   travel          ₹320.00   Auto to office
3    2024-03-16   bills           ₹999.00   Netflix subscription
```

---

## 💡 Hints (read only if stuck)

**Hint 1 — Data structure:**  
Store each expense as a dictionary:  
`{"id": 1, "date": "2024-03-15", "category": "food", "amount": 450.0, "description": "Lunch"}`  
Keep all expenses in a list of dictionaries.

**Hint 2 — Persistence:**  
Use the `csv` module with `DictWriter`/`DictReader` to save and load.

**Hint 3 — Menu loop:**  
Use a `while True` loop for the menu. Break when user chooses "Exit".

**Hint 4 — Input validation:**  
Wrap `input()` calls in `try/except` to handle invalid amounts.

---

## 📝 Start Here

Open `expense_tracker.py` and build the solution yourself.  
The file contains a skeleton with TODO comments to guide you.

---

## ✅ Done Criteria

Your project is complete when:
1. You can add, view, and delete expenses
2. Data persists across program restarts (CSV)
3. Summary shows totals per category
4. Invalid input does not crash the program
