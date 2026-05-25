"""
Day 1 — Variables and Data Types
Exercise Solutions

Note: Only look at these AFTER you have attempted the exercises yourself.
"""

# ─── Solution 1 ──────────────────────────────────────────────────────────────
product_name = "Wireless Mouse"
price = 1299.00
quantity = 45
is_available = True

availability = "Yes" if is_available else "No"

print(f"Product   : {product_name}")
print(f"Price     : ₹{price:,.2f}")
print(f"Quantity  : {quantity}")
print(f"Available : {availability}")


# ─── Solution 2 ──────────────────────────────────────────────────────────────
name = input("Enter your name: ")
age = int(input("Enter your age: "))
years_to_retire = 65 - age
print(f"Hello {name}! You will retire in {years_to_retire} years.")


# ─── Solution 3 ──────────────────────────────────────────────────────────────
text = "  data science  "
stripped = text.strip()

print(stripped)                          # "data science"
print(stripped.title())                  # "Data Science"
print(stripped.replace(" ", "-"))        # "data-science"
print(len(stripped))                     # 12


# ─── Solution 4 ──────────────────────────────────────────────────────────────
sales_str = "85000"
commission_rate_str = "0.12"

sales = float(sales_str)
commission_rate = float(commission_rate_str)

commission = sales * commission_rate
total_earnings = sales + commission

print(f"Total earnings: ₹{total_earnings:,.2f}")


# ─── Solution 5 — Debugging ───────────────────────────────────────────────────
# Fixed BUG 1: use a valid name starting with a letter
first_employee = "Ravi"
print(first_employee)

# Fixed BUG 2: convert string to int before subtraction
discount = 500          # removed quotes
final_price = 2000 - discount
print(final_price)

# Fixed BUG 3: define before use
total = 1000 + 500
print(f"Total: {total}")

# Fixed BUG 4: correct f-string syntax
name = "Kumar"
print(f"Hello, {name}, your score is 95")


# ─── Solution 6 — Invoice Generator ──────────────────────────────────────────
customer = input("Customer name: ")
product = input("Product name: ")
unit_price = float(input("Unit price (₹): "))
qty = int(input("Quantity: "))
gst_rate = float(input("GST rate (%): "))

subtotal = unit_price * qty
gst_amount = subtotal * (gst_rate / 100)
total = subtotal + gst_amount

line = "─" * 33
print(f"\n{line}")
print("         INVOICE")
print(line)
print(f"Customer : {customer}")
print(f"Product  : {product}")
print(f"Qty      : {qty} × ₹{unit_price:,.2f}")
print(f"Subtotal : ₹{subtotal:,.2f}")
print(f"GST ({gst_rate:.0f}%) : ₹{gst_amount:,.2f}")
print(f"TOTAL    : ₹{total:,.2f}")
print(line)
