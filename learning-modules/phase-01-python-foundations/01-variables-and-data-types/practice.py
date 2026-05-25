"""
Day 1 — Variables and Data Types
Practice File

Instructions:
- Type each block yourself (don't copy-paste).
- Run after each block to see the output.
- Read the comments carefully — they explain the WHY.
"""

# ─── SECTION 1: Creating Variables ──────────────────────────────────────────

# Python uses = to assign a value to a variable name
company_name = "DataCorp"
employee_count = 320
annual_revenue = 8750000.50
is_listed = True

print("--- Company Info ---")
print(company_name)
print(employee_count)
print(annual_revenue)
print(is_listed)


# ─── SECTION 2: Checking Data Types ─────────────────────────────────────────

# type() tells you what kind of data a variable holds
print("\n--- Data Types ---")
print(type(company_name))     # str
print(type(employee_count))   # int
print(type(annual_revenue))   # float
print(type(is_listed))        # bool


# ─── SECTION 3: f-Strings (the professional way to format output) ────────────

# f-strings let you embed variables directly inside a string
print("\n--- Formatted Output ---")
print(f"Company: {company_name}")
print(f"Employees: {employee_count}")
print(f"Revenue: ₹{annual_revenue:,.2f}")   # :,.2f formats as currency

# Expressions work inside f-strings too
tax = annual_revenue * 0.30
print(f"Estimated tax (30%): ₹{tax:,.2f}")


# ─── SECTION 4: Type Conversion ─────────────────────────────────────────────

print("\n--- Type Conversion ---")

# Input from users is ALWAYS a string — you must convert it
raw_score = "87"                   # pretend this came from input()
lead_score = int(raw_score)        # convert string → integer
print(f"Lead score: {lead_score}")
print(f"Type after conversion: {type(lead_score)}")

# String to float
raw_price = "1299.99"
price = float(raw_price)
price_with_gst = price * 1.18
print(f"Price with GST: ₹{price_with_gst:.2f}")

# Number to string (needed when joining with other text)
score = 95
label = "Score: " + str(score) + "/100"
print(label)


# ─── SECTION 5: String Methods ──────────────────────────────────────────────

print("\n--- String Methods ---")

raw_input = "   Priya Sharma   "
print(f"Original  : '{raw_input}'")
print(f"Stripped  : '{raw_input.strip()}'")
print(f"Uppercase : '{raw_input.strip().upper()}'")
print(f"Lowercase : '{raw_input.strip().lower()}'")
print(f"Length    : {len(raw_input.strip())}")

email = "priya.sharma@company.com"
print(f"Starts with 'priya': {email.startswith('priya')}")
print(f"Contains '@'       : {'@' in email}")
print(f"Domain             : {email.split('@')[1]}")


# ─── SECTION 6: None ─────────────────────────────────────────────────────────

# None means "no value yet" — common in data work for missing data
lead_phone = None
print(f"\nLead phone: {lead_phone}")
print(f"Is phone missing? {lead_phone is None}")


# ─── SECTION 7: Multiple Assignment ─────────────────────────────────────────

# Assign multiple variables on one line
x, y, z = 10, 20, 30
print(f"\nx={x}, y={y}, z={z}")

# Swap values — a Python trick
x, y = y, x
print(f"After swap: x={x}, y={y}")
