-- SQL Joins Practice
-- Topic: INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN

-- ─── Setup: Additional tables ─────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS sales_reps (
    id      INTEGER PRIMARY KEY,
    name    TEXT,
    region  TEXT,
    target  REAL
);

CREATE TABLE IF NOT EXISTS lead_assignments (
    lead_id     INTEGER,
    rep_id      INTEGER,
    assigned_at DATE
);

INSERT INTO sales_reps VALUES
(1, 'Arun Sharma',   'West',  5000000),
(2, 'Nisha Gupta',   'North', 4500000),
(3, 'Kiran Patel',   'South', 4000000),
(4, 'Manish Verma',  'East',  3500000);

INSERT INTO lead_assignments VALUES
(1, 1, '2024-01-16'),
(2, 2, '2024-01-23'),
(3, 1, '2024-02-02'),
(5, 3, '2024-02-21'),
(7, 1, '2024-03-11'),
(8, 3, '2024-03-19'),
(10, 2, '2024-04-03');
-- Note: leads 4, 6, 9 are unassigned


-- ─── INNER JOIN — only matching rows from both tables ─────────────────────────

-- Task: Show lead name + assigned rep name
SELECT
    l.name          AS lead_name,
    l.city,
    l.score,
    r.name          AS rep_name,
    r.region
FROM leads l
INNER JOIN lead_assignments la ON l.id = la.lead_id
INNER JOIN sales_reps r        ON la.rep_id = r.id
ORDER BY l.score DESC;


-- ─── LEFT JOIN — all leads, with rep info if assigned ────────────────────────

SELECT
    l.name          AS lead_name,
    l.status,
    r.name          AS rep_name,
    CASE WHEN r.name IS NULL THEN 'Unassigned' ELSE 'Assigned' END AS assignment_status
FROM leads l
LEFT JOIN lead_assignments la ON l.id = la.lead_id
LEFT JOIN sales_reps r        ON la.rep_id = r.id
ORDER BY l.name;


-- ─── Find unassigned leads (using LEFT JOIN + IS NULL) ────────────────────────

SELECT l.name, l.score, l.status
FROM leads l
LEFT JOIN lead_assignments la ON l.id = la.lead_id
WHERE la.lead_id IS NULL;


-- ─── Aggregation with JOIN ────────────────────────────────────────────────────

-- Task: Each rep — how many leads, total revenue, average score
SELECT
    r.name              AS rep_name,
    COUNT(l.id)         AS lead_count,
    SUM(l.revenue)      AS total_revenue,
    ROUND(AVG(l.score), 1) AS avg_score
FROM sales_reps r
LEFT JOIN lead_assignments la ON r.id = la.rep_id
LEFT JOIN leads l             ON la.lead_id = l.id
GROUP BY r.name
ORDER BY total_revenue DESC;
