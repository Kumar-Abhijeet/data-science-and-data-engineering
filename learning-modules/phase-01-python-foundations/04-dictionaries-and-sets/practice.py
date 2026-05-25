"""
Day 4 — Dictionaries and Sets
Practice File
"""

# ─── SECTION 1: Dictionaries ────────────────────────────────────────────────

# A dictionary stores data as key-value pairs
# Think of it like a database row or a JSON object

lead = {
    "name": "Priya Sharma",
    "company": "Innovate Solutions",
    "score": 87,
    "revenue": 1250000,
    "status": "Hot",
    "contacted": True
}

print("--- Lead Details ---")
print(f"Name    : {lead['name']}")
print(f"Score   : {lead['score']}")
print(f"Status  : {lead['status']}")

# Safe access with .get() — avoids KeyError if key does not exist
phone = lead.get("phone", "Not provided")
print(f"Phone   : {phone}")


# ─── SECTION 2: Modifying Dictionaries ──────────────────────────────────────

print("\n--- Modifying ---")
lead["score"] = 92                   # update existing key
lead["phone"] = "+91-9876543210"     # add new key
del lead["contacted"]                # delete a key

print(f"Updated score : {lead['score']}")
print(f"Phone added   : {lead['phone']}")
print(f"Keys now      : {list(lead.keys())}")


# ─── SECTION 3: Iterating Dictionaries ──────────────────────────────────────

print("\n--- Iterating ---")
for key, value in lead.items():
    print(f"  {key:<15}: {value}")


# ─── SECTION 4: Nested Dictionaries ─────────────────────────────────────────

print("\n--- Nested Dict (CRM record) ---")
crm = {
    "lead_001": {"name": "Priya", "score": 87, "city": "Mumbai"},
    "lead_002": {"name": "Rahul", "score": 65, "city": "Delhi"},
    "lead_003": {"name": "Ankit", "score": 91, "city": "Pune"},
}

for lead_id, details in crm.items():
    print(f"{lead_id}: {details['name']} ({details['city']}) — Score: {details['score']}")


# ─── SECTION 5: Dictionary Comprehension ────────────────────────────────────

print("\n--- Dict Comprehension ---")
# Only high-score leads (score >= 80)
hot_leads = {lid: info for lid, info in crm.items() if info["score"] >= 80}
for lid, info in hot_leads.items():
    print(f"Hot lead: {info['name']} — Score: {info['score']}")


# ─── SECTION 6: Sets ─────────────────────────────────────────────────────────

print("\n--- Sets ---")
# A set is an unordered collection of UNIQUE values
# Great for deduplication and membership testing

cities_visited = {"Mumbai", "Delhi", "Bangalore", "Mumbai", "Pune", "Delhi"}
print(f"Unique cities: {cities_visited}")    # duplicates removed automatically

skills_required = {"Python", "SQL", "Excel", "Power BI"}
skills_have = {"Python", "SQL", "Tableau", "Excel"}

print(f"\nRequired : {skills_required}")
print(f"I have   : {skills_have}")
print(f"I need   : {skills_required - skills_have}")          # difference
print(f"In both  : {skills_required & skills_have}")          # intersection
print(f"Combined : {skills_required | skills_have}")          # union
