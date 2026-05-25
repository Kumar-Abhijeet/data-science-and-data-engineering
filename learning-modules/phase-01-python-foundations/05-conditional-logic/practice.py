"""
Day 5 — Conditional Logic
Practice File
"""

# ─── SECTION 1: Basic if/elif/else ──────────────────────────────────────────

lead_score = 78

if lead_score >= 90:
    status = "Hot"
elif lead_score >= 70:
    status = "Warm"
elif lead_score >= 50:
    status = "Cold"
else:
    status = "Unqualified"

print(f"Score: {lead_score} → Status: {status}")


# ─── SECTION 2: Nested Conditions ────────────────────────────────────────────

revenue = 500000
is_decision_maker = True

if revenue >= 300000:
    if is_decision_maker:
        priority = "HIGH — pursue immediately"
    else:
        priority = "MEDIUM — find decision maker"
else:
    priority = "LOW — nurture for later"

print(f"\nRevenue: ₹{revenue:,.0f}, Decision Maker: {is_decision_maker}")
print(f"Priority: {priority}")


# ─── SECTION 3: Ternary (One-line) Condition ─────────────────────────────────

# condition_if_true if condition else condition_if_false
score = 82
label = "Pass" if score >= 60 else "Fail"
print(f"\nScore: {score} → {label}")

# Practical use: format output
is_profitable = True
icon = "✓ Profitable" if is_profitable else "✗ Loss"
print(icon)


# ─── SECTION 4: in Operator with Conditions ──────────────────────────────────

industry = "FinTech"
target_industries = ["FinTech", "HealthTech", "EdTech", "SaaS"]

if industry in target_industries:
    print(f"\n{industry} is a target industry — qualify the lead.")
else:
    print(f"\n{industry} is not a target — mark as low priority.")


# ─── SECTION 5: Real Business Logic ──────────────────────────────────────────

print("\n--- Loan Eligibility Check ---")

annual_income = 720000
credit_score = 720
employment_type = "Salaried"
loan_amount = 2500000

eligible = True
reasons = []

if annual_income < 300000:
    eligible = False
    reasons.append("Income below minimum ₹3,00,000")

if credit_score < 700:
    eligible = False
    reasons.append("Credit score below 700")

if employment_type not in ["Salaried", "Self-Employed"]:
    eligible = False
    reasons.append("Employment type not accepted")

if loan_amount > annual_income * 5:
    eligible = False
    reasons.append("Loan amount exceeds 5x annual income")

if eligible:
    print("✓ LOAN APPROVED")
else:
    print("✗ LOAN REJECTED")
    for reason in reasons:
        print(f"  - {reason}")
