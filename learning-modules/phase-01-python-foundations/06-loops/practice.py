"""
Day 6 — Loops
Practice File
"""

# ─── SECTION 1: for Loop ─────────────────────────────────────────────────────

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [65000, 1200, 2500, 18000]

print("--- Product Catalogue ---")
for product in products:
    print(f"  - {product}")


# ─── SECTION 2: range() ──────────────────────────────────────────────────────

print("\n--- Sales Report (12 months) ---")
for month in range(1, 13):
    print(f"  Month {month:02d}: processing...")


# ─── SECTION 3: enumerate() ──────────────────────────────────────────────────

print("\n--- Indexed List ---")
for idx, product in enumerate(products, start=1):
    print(f"  {idx}. {product}")


# ─── SECTION 4: zip() ────────────────────────────────────────────────────────

print("\n--- Product Prices ---")
for product, price in zip(products, prices):
    print(f"  {product:<12}: ₹{price:,.0f}")


# ─── SECTION 5: while Loop ───────────────────────────────────────────────────

print("\n--- Password Attempt Simulator ---")
correct_pin = "1234"
attempts = 0
max_attempts = 3

# In real code, you would use input() here
# For practice, we simulate with a list of guesses
guesses = ["0000", "1111", "1234"]

for guess in guesses:
    attempts += 1
    if guess == correct_pin:
        print(f"  Access granted on attempt {attempts}!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"  Wrong PIN. {remaining} attempt(s) left.")
        else:
            print("  Account locked.")
            break


# ─── SECTION 6: Loop with continue ───────────────────────────────────────────

print("\n--- Skip Low-Value Leads ---")
lead_scores = [45, 82, 30, 91, 68, 55, 77]

for score in lead_scores:
    if score < 70:
        continue                # skip low scores
    print(f"  Hot lead with score: {score}")


# ─── SECTION 7: List Comprehension vs Loop ───────────────────────────────────

# Traditional loop
monthly_sales = [45000, 52000, 38000, 61000, 55000, 47000]
above_average = []
average = sum(monthly_sales) / len(monthly_sales)

for s in monthly_sales:
    if s > average:
        above_average.append(s)

# Same as one line with list comprehension
above_average_v2 = [s for s in monthly_sales if s > average]

print(f"\nAverage sales    : ₹{average:,.0f}")
print(f"Above average    : {above_average}")
print(f"Same result (v2) : {above_average_v2}")


# ─── SECTION 8: Nested Loop ──────────────────────────────────────────────────

print("\n--- Sales Matrix ---")
regions = ["North", "South", "East"]
quarters = ["Q1", "Q2", "Q3", "Q4"]

for region in regions:
    row = f"  {region:<6} | "
    for q in quarters:
        row += f"{q} ✓  "
    print(row)
