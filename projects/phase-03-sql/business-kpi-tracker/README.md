# Project — Business KPI Tracker (Portfolio)

**Phase:** SQL + Python  
**Skills:** SQLite, SQLAlchemy, pandas, Matplotlib, SQL aggregations, CTEs

---

## 📋 Project Overview

Build a Python + SQL powered Business KPI Tracker that:
- Creates and populates a SQLite database with sample business data
- Calculates KPIs using SQL queries
- Visualises KPIs using Python
- Generates a monthly report

---

## 🎯 Business KPIs to Track

| KPI | SQL Concept |
|-----|------------|
| Monthly Revenue | GROUP BY + SUM |
| MoM Growth % | Window function (LAG) |
| Top 10 Customers by Revenue | ORDER BY + LIMIT |
| Customer Acquisition by Month | GROUP BY DATE |
| Average Order Value | AVG |
| Churn Rate | Subquery |
| Sales by Region | JOIN + GROUP BY |
| Conversion Rate by Channel | CTE |

---

## 🗂️ Folder Structure

```text
business-kpi-tracker/
├── README.md
├── setup_db.py         ← creates and seeds the database
├── kpi_queries.py      ← all SQL queries as functions
├── dashboard.py        ← visualisations
├── report.py           ← generates PDF/text report
└── data/
    └── kpi_tracker.db  ← SQLite database
```

---

## ⚙️ Features to Build

- [ ] Schema: customers, orders, products, regions
- [ ] Seed script with realistic sample data (use `random` + `datetime`)
- [ ] KPI functions using `pd.read_sql_query()`
- [ ] Bar charts for revenue by month
- [ ] Line chart for MoM growth
- [ ] Table output for top customers
- [ ] Text-based summary report

---

## 💡 Schema Design

```sql
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    region TEXT,
    channel TEXT,        -- online, direct, partner
    created_date DATE
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    order_date DATE,
    amount REAL,
    status TEXT          -- completed, refunded, pending
);
```
