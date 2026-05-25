"""
Day 11 — File Handling
Practice File: read, write, append, CSV, JSON
"""
import csv
import json
import os

# ─── SECTION 1: Writing a Text File ──────────────────────────────────────────

report_path = "/tmp/sales_report.txt"

with open(report_path, "w") as f:
    f.write("=== Monthly Sales Report ===\n")
    f.write("Month     Sales\n")
    f.write("-" * 25 + "\n")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales  = [45000, 52000, 38000, 61000, 55000, 47000]
    for month, amount in zip(months, sales):
        f.write(f"{month:<10}{amount:>10,.0f}\n")

print(f"Report written to {report_path}")


# ─── SECTION 2: Reading a Text File ──────────────────────────────────────────

with open(report_path, "r") as f:
    content = f.read()
print("\n--- File Contents ---")
print(content)


# ─── SECTION 3: Appending to a File ──────────────────────────────────────────

with open(report_path, "a") as f:
    f.write("-" * 25 + "\n")
    f.write(f"{'Total':<10}{sum(sales):>10,.0f}\n")

print("Appended total to report.")


# ─── SECTION 4: Writing and Reading CSV ──────────────────────────────────────

csv_path = "/tmp/leads.csv"

leads = [
    {"name": "Priya Sharma", "score": 87, "status": "Hot",  "revenue": 1250000},
    {"name": "Rahul Verma",  "score": 65, "status": "Warm", "revenue":  450000},
    {"name": "Ankit Gupta",  "score": 92, "status": "Hot",  "revenue": 2100000},
]

# Write CSV
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score", "status", "revenue"])
    writer.writeheader()
    writer.writerows(leads)

print(f"\nCSV written to {csv_path}")

# Read CSV
print("\n--- Reading CSV ---")
with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['name']:<20} Score: {row['score']:<5} ₹{int(row['revenue']):,.0f}")


# ─── SECTION 5: Writing and Reading JSON ─────────────────────────────────────

json_path = "/tmp/config.json"

config = {
    "app_name": "LeadTracker",
    "version": "1.0.0",
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "leads_db"
    },
    "features": ["email_alerts", "csv_export", "dashboard"],
    "debug": False
}

# Write JSON
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)

print(f"\nJSON written to {json_path}")

# Read JSON
with open(json_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(f"\nApp     : {loaded['app_name']} v{loaded['version']}")
print(f"DB Host : {loaded['database']['host']}:{loaded['database']['port']}")
print(f"Features: {', '.join(loaded['features'])}")


# ─── SECTION 6: Checking File Existence ──────────────────────────────────────

for path in [report_path, csv_path, json_path]:
    exists = os.path.exists(path)
    size = os.path.getsize(path) if exists else 0
    print(f"  {path}: exists={exists}, size={size} bytes")
