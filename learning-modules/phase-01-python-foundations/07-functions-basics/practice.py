"""
Day 7 — Functions Basics
Practice File
"""

# ─── SECTION 1: Defining and Calling Functions ───────────────────────────────

# A function is a reusable block of code
# WHY: avoids repeating the same code, makes programs modular

def calculate_profit(revenue, expenses):
    """Calculate gross profit and profit margin."""
    profit = revenue - expenses
    margin = (profit / revenue) * 100
    return profit, margin         # returning multiple values as a tuple


profit, margin = calculate_profit(800000, 520000)
print(f"Profit: ₹{profit:,.0f}  |  Margin: {margin:.1f}%")


# ─── SECTION 2: Default Parameters ──────────────────────────────────────────

def apply_discount(price, discount_pct=10):
    """Apply a discount. Default discount is 10%."""
    discount = price * (discount_pct / 100)
    return price - discount


print(f"\nDefault 10% discount: ₹{apply_discount(1000):,.0f}")
print(f"Custom 25% discount : ₹{apply_discount(1000, 25):,.0f}")


# ─── SECTION 3: Keyword Arguments ────────────────────────────────────────────

def create_lead_summary(name, score, city="Unknown", status="Cold"):
    return f"{name} | {city} | Score: {score} | {status}"


print("\n" + create_lead_summary("Priya", 87, city="Mumbai", status="Hot"))
print(create_lead_summary(score=65, name="Rahul"))    # order doesn't matter


# ─── SECTION 4: Docstrings ───────────────────────────────────────────────────

def classify_lead(score):
    """
    Classify a lead based on their score.

    Args:
        score (int): Lead score between 0 and 100.

    Returns:
        str: Classification label — Hot, Warm, Cold, or Unqualified.
    """
    if score >= 85:
        return "Hot"
    elif score >= 70:
        return "Warm"
    elif score >= 50:
        return "Cold"
    return "Unqualified"


# Access the docstring
print(f"\n{classify_lead.__doc__}")
print(f"Score 90 → {classify_lead(90)}")
print(f"Score 72 → {classify_lead(72)}")
print(f"Score 40 → {classify_lead(40)}")


# ─── SECTION 5: Functions Calling Functions ──────────────────────────────────

def calculate_gst(amount, rate=18):
    return amount * (rate / 100)


def generate_invoice(item, price, qty):
    subtotal = price * qty
    gst = calculate_gst(subtotal)
    total = subtotal + gst
    return {
        "item": item,
        "subtotal": subtotal,
        "gst": gst,
        "total": total
    }


invoice = generate_invoice("Laptop", 65000, 3)
print("\n--- Invoice ---")
for key, value in invoice.items():
    if isinstance(value, (int, float)):
        print(f"  {key:<10}: ₹{value:,.2f}")
    else:
        print(f"  {key:<10}: {value}")


# ─── SECTION 6: Variable Scope ───────────────────────────────────────────────

# Variables inside a function are LOCAL — not accessible outside
company = "TechCorp"   # global variable

def show_info():
    department = "Sales"   # local variable
    print(f"{company} — {department}")   # can READ global inside function

show_info()
# print(department)   # ← would raise NameError — department is local
