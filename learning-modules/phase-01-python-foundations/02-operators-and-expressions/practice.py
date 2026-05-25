"""
Day 2 — Operators and Expressions
Practice File
"""

# ─── SECTION 1: Arithmetic Operators ────────────────────────────────────────

revenue = 500000
expenses = 320000

profit = revenue - expenses
profit_margin = (profit / revenue) * 100
tax = profit * 0.30
net_profit = profit - tax

print("--- P&L Summary ---")
print(f"Revenue       : ₹{revenue:,.0f}")
print(f"Expenses      : ₹{expenses:,.0f}")
print(f"Gross Profit  : ₹{profit:,.0f}")
print(f"Profit Margin : {profit_margin:.1f}%")
print(f"Tax (30%)     : ₹{tax:,.0f}")
print(f"Net Profit    : ₹{net_profit:,.0f}")

# Floor division and modulo
total_items = 157
items_per_box = 12
full_boxes = total_items // 12      # integer division — how many complete boxes
leftover = total_items % 12         # remainder — how many items are left over
print(f"\n{total_items} items → {full_boxes} full boxes + {leftover} leftover")

# Exponentiation
growth_rate = 1.08          # 8% annual growth
revenue_after_3_years = revenue * (growth_rate ** 3)
print(f"Revenue in 3 years (8% growth): ₹{revenue_after_3_years:,.0f}")


# ─── SECTION 2: Comparison Operators ────────────────────────────────────────

print("\n--- Comparisons ---")
lead_score = 72
threshold = 70

print(f"Score {lead_score} > threshold {threshold}: {lead_score > threshold}")
print(f"Score == 72: {lead_score == 72}")
print(f"Score != 80: {lead_score != 80}")
print(f"Score >= 70: {lead_score >= 70}")


# ─── SECTION 3: Logical Operators ───────────────────────────────────────────

print("\n--- Logical Operators ---")
is_verified = True
has_budget = True
is_decision_maker = False

# and: both must be True
qualified = is_verified and has_budget
print(f"Qualified (verified AND budget): {qualified}")

# or: at least one must be True
can_proceed = has_budget or is_decision_maker
print(f"Can proceed (budget OR decision maker): {can_proceed}")

# not: flips True to False
print(f"Not verified: {not is_verified}")

# Combined
hot_lead = is_verified and has_budget and lead_score >= 70
print(f"Hot lead: {hot_lead}")


# ─── SECTION 4: String Operators ────────────────────────────────────────────

print("\n--- String Operations ---")
first = "Data"
last = "Science"

# Concatenation
full = first + " " + last
print(full)

# Repetition
divider = "-" * 40
print(divider)

# Membership check
sentence = "Python is great for data analysis"
print(f"'data' in sentence: {'data' in sentence}")
print(f"'java' in sentence: {'java' in sentence}")


# ─── SECTION 5: Assignment Operators ────────────────────────────────────────

print("\n--- Running Total ---")
total_sales = 0
total_sales += 15000       # same as total_sales = total_sales + 15000
total_sales += 22000
total_sales += 8500
print(f"Total sales: ₹{total_sales:,.0f}")
