"""
Day 8 — Functions Advanced
Practice File: *args, **kwargs, lambda, map, filter
"""

# ─── SECTION 1: *args — Variable Positional Arguments ───────────────────────

def total_sales(*amounts):
    """Accept any number of sales figures and return total."""
    return sum(amounts)


print(total_sales(10000, 25000))
print(total_sales(5000, 8000, 12000, 3000, 9500))


# ─── SECTION 2: **kwargs — Variable Keyword Arguments ───────────────────────

def create_report(**metrics):
    """Build a report dict from any keyword metrics."""
    print("\n--- Business Report ---")
    for metric, value in metrics.items():
        print(f"  {metric.replace('_', ' ').title():<20}: {value}")


create_report(
    revenue=850000,
    expenses=540000,
    leads_generated=142,
    deals_closed=28,
    churn_rate="4.2%"
)


# ─── SECTION 3: Combining *args and **kwargs ─────────────────────────────────

def log_event(event_type, *tags, **details):
    print(f"\nEvent: {event_type}")
    print(f"Tags : {tags}")
    print(f"Info : {details}")


log_event(
    "lead_converted",
    "hot-lead", "q3",
    lead_name="Priya",
    revenue=120000,
    rep="Vikram"
)


# ─── SECTION 4: Lambda Functions ─────────────────────────────────────────────

# A lambda is a small anonymous function — one line, one expression
# Syntax: lambda arguments: expression

double = lambda x: x * 2
add_gst = lambda price: price * 1.18
lead_label = lambda score: "Hot" if score >= 80 else "Warm" if score >= 60 else "Cold"

print(f"\n2x of 5000: {double(5000)}")
print(f"Price with GST: ₹{add_gst(1000):,.2f}")
print(f"Score 85: {lead_label(85)}")
print(f"Score 65: {lead_label(65)}")
print(f"Score 40: {lead_label(40)}")


# ─── SECTION 5: map() ────────────────────────────────────────────────────────

# map(function, iterable) — apply a function to every item in a list
prices = [1000, 2500, 850, 3200]
prices_with_gst = list(map(lambda p: round(p * 1.18, 2), prices))
print(f"\nOriginal  : {prices}")
print(f"With GST  : {prices_with_gst}")


# ─── SECTION 6: filter() ─────────────────────────────────────────────────────

# filter(function, iterable) — keep only items where the function returns True
lead_scores = [82, 45, 91, 63, 77, 38, 88, 55]
hot_leads = list(filter(lambda s: s >= 80, lead_scores))
print(f"\nAll scores : {lead_scores}")
print(f"Hot (>=80) : {hot_leads}")


# ─── SECTION 7: sorted() with key ────────────────────────────────────────────

employees = [
    {"name": "Rahul", "salary": 75000},
    {"name": "Priya", "salary": 92000},
    {"name": "Ankit", "salary": 68000},
]

by_salary = sorted(employees, key=lambda e: e["salary"], reverse=True)
print("\n--- Employees by Salary (desc) ---")
for emp in by_salary:
    print(f"  {emp['name']:<10}: ₹{emp['salary']:,.0f}")
