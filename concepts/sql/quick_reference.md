# SQL Quick Reference

## Basic Query Structure

```sql
SELECT column1, column2
FROM table_name
WHERE condition
GROUP BY column1
HAVING aggregate_condition
ORDER BY column1 DESC
LIMIT 10;
```

---

## Core Clauses

### WHERE — Filter rows
```sql
SELECT * FROM leads
WHERE score >= 80
  AND status = 'Hot'
  AND city IN ('Mumbai', 'Bengaluru');
```

### GROUP BY + Aggregate Functions
```sql
SELECT
    city,
    COUNT(*)           AS total_leads,
    AVG(score)         AS avg_score,
    SUM(revenue)       AS total_revenue,
    MAX(score)         AS top_score
FROM leads
GROUP BY city
HAVING COUNT(*) > 5
ORDER BY total_revenue DESC;
```

---

## JOIN Types

```sql
-- INNER JOIN: only matching rows from both tables
SELECT o.order_id, c.name
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id;

-- LEFT JOIN: all from left, matching from right (NULLs if no match)
SELECT c.name, o.order_id
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id;

-- RIGHT JOIN: all from right, matching from left
-- FULL OUTER JOIN: all rows from both (union of left + right)
```

---

## Common Table Expressions (CTEs)

```sql
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', order_date) AS month,
        SUM(amount) AS revenue
    FROM orders
    GROUP BY 1
)
SELECT
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) AS prev_month,
    revenue - LAG(revenue) OVER (ORDER BY month) AS mom_change
FROM monthly_revenue;
```

---

## Window Functions

```sql
SELECT
    name,
    department,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank,
    ROW_NUMBER() OVER (ORDER BY salary DESC)                   AS overall_rank,
    SUM(salary) OVER (PARTITION BY department)                 AS dept_total,
    LAG(salary, 1) OVER (ORDER BY hire_date)                   AS prev_salary,
    LEAD(salary, 1) OVER (ORDER BY hire_date)                  AS next_salary
FROM employees;
```

---

## Subqueries

```sql
-- Scalar subquery in SELECT
SELECT name, salary,
    (SELECT AVG(salary) FROM employees) AS company_avg
FROM employees;

-- Subquery in WHERE
SELECT * FROM leads
WHERE score > (SELECT AVG(score) FROM leads);

-- Subquery in FROM (derived table)
SELECT city, avg_score
FROM (
    SELECT city, AVG(score) AS avg_score
    FROM leads
    GROUP BY city
) AS city_stats
WHERE avg_score > 75;
```

---

## Python + SQLite

```python
import sqlite3

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

# Execute query
cursor.execute("SELECT * FROM leads WHERE score > ?", (80,))
rows = cursor.fetchall()

# Use pandas
import pandas as pd
df = pd.read_sql_query("SELECT * FROM leads", conn)

conn.close()
```
