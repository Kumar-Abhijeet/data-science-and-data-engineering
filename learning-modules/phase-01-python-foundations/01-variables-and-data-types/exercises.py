"""
Day 1 — Variables and Data Types
Exercises

Instructions:
- Attempt each exercise yourself FIRST.
- Use hints only if stuck.
- Solutions are in the solutions/ folder — check only AFTER attempting.
"""

# ─── Exercise 1 ──────────────────────────────────────────────────────────────
# Create variables for a product listing:
#   - product_name (str): any product
#   - price (float): price in rupees
#   - quantity (int): number in stock
#   - is_available (bool): whether it is in stock
#
# Then print a formatted summary like:
#   Product   : Wireless Mouse
#   Price     : ₹1,299.00
#   Quantity  : 45
#   Available : Yes
#
# Hint: use an f-string and a ternary expression for Yes/No

# YOUR CODE HERE


# ─── Exercise 2 ──────────────────────────────────────────────────────────────
# Ask the user for:
#   - their name
#   - their current age
#
# Print: "Hello [name]! You will retire in [65 - age] years."
#
# Hint: input() always returns a str — convert age to int before maths

# YOUR CODE HERE


# ─── Exercise 3 ──────────────────────────────────────────────────────────────
# Given the string: "  data science  "
# Print it:
#   a) with whitespace removed
#   b) in title case (first letter of each word capitalised)
#   c) with spaces replaced by hyphens
#   d) with its character length (after stripping)

# YOUR CODE HERE


# ─── Exercise 4 ──────────────────────────────────────────────────────────────
# A salesperson's data comes in as strings from a form:
#   sales_str = "85000"
#   commission_rate_str = "0.12"
#
# Calculate:
#   commission = sales * commission_rate
#   total_earnings = sales + commission
#
# Print: "Total earnings: ₹XX,XXX.XX"

# YOUR CODE HERE


# ─── Exercise 5 — Debugging ───────────────────────────────────────────────────
# Fix all errors in the code below. Run it to confirm no errors.

# BUG 1: invalid variable name
# 1st_employee = "Ravi"
# print(1st_employee)

# BUG 2: type mismatch
# discount = "500"
# final_price = 2000 - discount
# print(final_price)

# BUG 3: variable used before assignment
# print(f"Total: {total}")
# total = 1000 + 500

# BUG 4: wrong f-string syntax
# name = "Kumar"
# print("Hello, " + name + ", your score is " score)

# YOUR FIXED CODE HERE


# ─── Exercise 6 — Challenge ───────────────────────────────────────────────────
# Build a "Simple Invoice" generator.
# Ask the user for:
#   - Customer name
#   - Product name
#   - Unit price (float)
#   - Quantity (int)
#   - GST rate as a percentage (e.g. 18 for 18%)
#
# Calculate:
#   - Subtotal = unit price × quantity
#   - GST amount = subtotal × (rate / 100)
#   - Total = subtotal + GST
#
# Print a formatted invoice:
# ─────────────────────────────────
#          INVOICE
# ─────────────────────────────────
# Customer : [name]
# Product  : [product]
# Qty      : [qty] × ₹[unit_price]
# Subtotal : ₹[subtotal]
# GST (18%): ₹[gst]
# TOTAL    : ₹[total]
# ─────────────────────────────────

# YOUR CODE HERE
