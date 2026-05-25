"""
Day 3 — Lists and Tuples
Practice File
"""

# ─── SECTION 1: Creating Lists ──────────────────────────────────────────────

# A list is an ordered, mutable (changeable) collection
monthly_sales = [45000, 52000, 38000, 61000, 55000, 47000]
product_names = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset"]
mixed = [1, "hello", 3.14, True, None]   # lists can hold mixed types

print("Sales:", monthly_sales)
print("Products:", product_names)


# ─── SECTION 2: Indexing and Slicing ────────────────────────────────────────

print("\n--- Indexing ---")
print(f"First month sales  : {monthly_sales[0]}")    # index starts at 0
print(f"Last month sales   : {monthly_sales[-1]}")   # negative = from end
print(f"Third product      : {product_names[2]}")

print("\n--- Slicing ---")
# [start:end] — end is NOT included
q1_sales = monthly_sales[0:3]      # Jan, Feb, Mar
q2_sales = monthly_sales[3:6]      # Apr, May, Jun
print(f"Q1: {q1_sales}")
print(f"Q2: {q2_sales}")
print(f"Last 3 months: {monthly_sales[-3:]}")


# ─── SECTION 3: List Methods ────────────────────────────────────────────────

print("\n--- List Methods ---")
leads = ["Priya", "Rahul", "Ankit"]

leads.append("Neha")              # add to end
print(f"After append: {leads}")

leads.insert(1, "Vijay")          # insert at specific position
print(f"After insert: {leads}")

leads.remove("Ankit")             # remove by value
print(f"After remove: {leads}")

popped = leads.pop()              # remove and return last item
print(f"Popped: {popped}, List now: {leads}")

leads.sort()                      # sort alphabetically
print(f"Sorted: {leads}")

print(f"Count of items: {len(leads)}")
print(f"Rahul at index: {leads.index('Rahul')}")


# ─── SECTION 4: List Aggregations ───────────────────────────────────────────

print("\n--- Aggregations ---")
print(f"Total sales : ₹{sum(monthly_sales):,.0f}")
print(f"Average     : ₹{sum(monthly_sales)/len(monthly_sales):,.0f}")
print(f"Best month  : ₹{max(monthly_sales):,.0f}")
print(f"Worst month : ₹{min(monthly_sales):,.0f}")


# ─── SECTION 5: List Comprehension ─────────────────────────────────────────

print("\n--- List Comprehension ---")
# Double each sales figure (simulating 2x growth scenario)
doubled = [s * 2 for s in monthly_sales]
print(f"Doubled: {doubled}")

# Filter: only months with sales above 50000
high_sales = [s for s in monthly_sales if s > 50000]
print(f"High-sales months: {high_sales}")


# ─── SECTION 6: Tuples ──────────────────────────────────────────────────────

print("\n--- Tuples ---")
# Tuples are like lists but IMMUTABLE (cannot be changed after creation)
# Use them for data that should not change: coordinates, config, database rows

company_info = ("TechCorp", "Bengaluru", 2015, "B2B SaaS")
print(f"Company  : {company_info[0]}")
print(f"City     : {company_info[1]}")
print(f"Founded  : {company_info[2]}")
print(f"Segment  : {company_info[3]}")

# Tuple unpacking
name, city, year, segment = company_info
print(f"\nUnpacked — {name} founded in {year} in {city}")

# Trying to modify a tuple raises TypeError:
# company_info[0] = "NewCorp"  # ← uncomment to see the error

# Tuples are faster and use less memory than lists
# Use lists for data that changes; tuples for fixed records
