"""
Day 12 — Exception Handling
Practice File: try/except/else/finally, custom exceptions
"""

# ─── SECTION 1: Why Exception Handling? ──────────────────────────────────────

# Without exception handling, your program crashes on any error.
# With it, you can catch errors gracefully and give useful messages.

# Example without handling (would crash):
# result = 10 / 0    # ZeroDivisionError

# With handling:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")


# ─── SECTION 2: Multiple Exceptions ──────────────────────────────────────────

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid types for division"


print(safe_divide(100, 4))
print(safe_divide(100, 0))
print(safe_divide("100", 5))


# ─── SECTION 3: else and finally ─────────────────────────────────────────────

# else: runs if no exception occurred
# finally: ALWAYS runs (for cleanup)

def load_lead_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"  Error: File '{filename}' not found.")
        return None
    except PermissionError:
        print(f"  Error: No permission to read '{filename}'.")
        return None
    else:
        print(f"  Successfully loaded {len(data)} characters.")
        return data
    finally:
        print("  File operation attempted.")    # always runs


print("\n--- File Loading ---")
load_lead_file("/tmp/leads.csv")               # likely exists from Day 11
load_lead_file("/tmp/nonexistent_file.csv")    # does not exist


# ─── SECTION 4: Custom Exceptions ────────────────────────────────────────────

class LeadValidationError(Exception):
    """Raised when lead data fails validation."""
    pass

class NegativeScoreError(LeadValidationError):
    """Raised when a lead score is negative."""
    pass

class ScoreRangeError(LeadValidationError):
    """Raised when a lead score is outside 0–100."""
    pass


def validate_lead(name, score, revenue):
    if not name or not name.strip():
        raise LeadValidationError("Lead name cannot be empty.")
    if score < 0:
        raise NegativeScoreError(f"Score cannot be negative: {score}")
    if score > 100:
        raise ScoreRangeError(f"Score must be 0–100, got {score}")
    if revenue < 0:
        raise LeadValidationError(f"Revenue cannot be negative: {revenue}")
    return True


print("\n--- Lead Validation ---")
test_cases = [
    ("Priya", 87, 1250000),
    ("", 75, 500000),
    ("Rahul", -5, 300000),
    ("Ankit", 150, 800000),
]

for name, score, revenue in test_cases:
    try:
        validate_lead(name, score, revenue)
        print(f"  ✓ Valid: {name}, score={score}")
    except NegativeScoreError as e:
        print(f"  ✗ NegativeScoreError: {e}")
    except ScoreRangeError as e:
        print(f"  ✗ ScoreRangeError: {e}")
    except LeadValidationError as e:
        print(f"  ✗ ValidationError: {e}")


# ─── SECTION 5: re-raising Exceptions ────────────────────────────────────────

def process_payment(amount):
    try:
        if amount <= 0:
            raise ValueError("Payment amount must be positive.")
        print(f"  Processing ₹{amount:,.0f}...")
        return True
    except ValueError as e:
        print(f"  Logging error: {e}")
        raise    # re-raise so caller can handle it too


print("\n--- Payment Processing ---")
try:
    process_payment(-500)
except ValueError:
    print("  Payment failed — rolling back transaction.")
