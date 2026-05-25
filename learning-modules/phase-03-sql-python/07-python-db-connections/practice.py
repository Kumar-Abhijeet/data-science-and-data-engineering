"""
Python + SQL Connections
Day 7 of Phase 3 — Practice File

Topics:
- sqlite3 built-in module
- SQLAlchemy ORM basics
- pandas read_sql_query
"""
import sqlite3
import os

DB_PATH = "/tmp/crm_practice.db"


# ─── SECTION 1: sqlite3 — built-in Python module ─────────────────────────────

def setup_database():
    """Create and seed the practice database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.executescript("""
        DROP TABLE IF EXISTS leads;
        DROP TABLE IF EXISTS sales_reps;

        CREATE TABLE leads (
            id          INTEGER PRIMARY KEY,
            name        TEXT,
            company     TEXT,
            city        TEXT,
            score       INTEGER,
            revenue     REAL,
            status      TEXT,
            rep_id      INTEGER
        );

        CREATE TABLE sales_reps (
            id      INTEGER PRIMARY KEY,
            name    TEXT,
            region  TEXT
        );

        INSERT INTO sales_reps VALUES
            (1, 'Arun Sharma',  'West'),
            (2, 'Nisha Gupta',  'North'),
            (3, 'Kiran Patel',  'South');

        INSERT INTO leads VALUES
            (1, 'Priya Sharma', 'Innovate',   'Mumbai',     87, 1250000, 'Hot',  1),
            (2, 'Rahul Verma',  'DataDriven', 'Delhi',      65,  450000, 'Warm', 2),
            (3, 'Ankit Gupta',  'CloudBase',  'Pune',       92, 2100000, 'Hot',  1),
            (4, 'Sneha Patel',  'TechStart',  'Mumbai',     48,  180000, 'Cold', 3),
            (5, 'Vikram Singh', 'Enterprise', 'Bengaluru',  78,  850000, 'Warm', 2);
    """)

    conn.commit()
    conn.close()
    print(f"Database created: {DB_PATH}")


def basic_queries():
    """Demonstrate basic sqlite3 usage."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("\n--- All Leads ---")
    cursor.execute("SELECT id, name, score, status FROM leads ORDER BY score DESC")
    rows = cursor.fetchall()
    for row in rows:
        print(f"  {row[0]:<4} {row[1]:<20} {row[2]:<6} {row[3]}")

    print("\n--- Hot Leads ---")
    cursor.execute("SELECT name, revenue FROM leads WHERE status = ? ORDER BY revenue DESC", ("Hot",))
    for row in cursor.fetchall():
        print(f"  {row[0]:<20} ₹{row[1]:,.0f}")

    conn.close()


def dict_cursor():
    """Use sqlite3.Row for dict-like access."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # enables column-name access

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leads")
    rows = cursor.fetchall()

    print("\n--- Dict-style Access ---")
    for row in rows:
        print(f"  {row['name']:<20} Score: {row['score']}  Revenue: ₹{row['revenue']:,.0f}")

    conn.close()


def join_query():
    """JOIN leads with sales_reps."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = """
        SELECT
            l.name          AS lead_name,
            l.score,
            l.status,
            r.name          AS rep_name,
            r.region
        FROM leads l
        JOIN sales_reps r ON l.rep_id = r.id
        ORDER BY l.score DESC
    """
    cursor.execute(query)

    print("\n--- Leads with Rep ---")
    print(f"{'Lead':<20} {'Score':<6} {'Status':<10} {'Rep':<15} Region")
    print("-" * 65)
    for row in cursor.fetchall():
        print(f"{row['lead_name']:<20} {row['score']:<6} {row['status']:<10} {row['rep_name']:<15} {row['region']}")

    conn.close()


# ─── SECTION 2: pandas + SQL ─────────────────────────────────────────────────

def pandas_sql():
    """Use pandas to read SQL query results as DataFrames."""
    try:
        import pandas as pd
    except ImportError:
        print("\n[INFO] pandas not installed. Run: pip install pandas")
        print("       Install requirements: pip install -r requirements.txt")
        return None

    conn = sqlite3.connect(DB_PATH)

    # Read entire table
    df = pd.read_sql_query("SELECT * FROM leads", conn)
    print("\n--- DataFrame from SQL ---")
    print(df[["name", "score", "status", "revenue"]].to_string(index=False))

    # Aggregation query → DataFrame
    summary = pd.read_sql_query("""
        SELECT
            status,
            COUNT(*)    AS count,
            AVG(score)  AS avg_score,
            SUM(revenue) AS total_revenue
        FROM leads
        GROUP BY status
        ORDER BY total_revenue DESC
    """, conn)

    print("\n--- Pipeline Summary ---")
    print(summary.to_string(index=False))

    conn.close()
    return df


if __name__ == "__main__":
    setup_database()
    basic_queries()
    dict_cursor()
    join_query()
    pandas_sql()
