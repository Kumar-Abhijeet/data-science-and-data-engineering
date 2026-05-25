-- SQL Basics — Day 1 Practice Queries
-- Database: SQLite (run via Python or DB Browser for SQLite)
-- Topic: SELECT, WHERE, ORDER BY, LIMIT, DISTINCT

-- ─── Setup: Create sample tables ─────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS leads (
    id          INTEGER PRIMARY KEY,
    name        TEXT    NOT NULL,
    company     TEXT,
    city        TEXT,
    score       INTEGER,
    revenue     REAL,
    status      TEXT,   -- Hot, Warm, Cold, Unqualified
    source      TEXT,   -- Website, Referral, Cold Call, Event
    created_at  DATE
);

INSERT INTO leads (name, company, city, score, revenue, status, source, created_at) VALUES
('Priya Sharma',    'Innovate Solutions', 'Mumbai',     87, 1250000, 'Hot',         'Referral',  '2024-01-15'),
('Rahul Verma',     'DataDriven Corp',   'Delhi',       65,  450000, 'Warm',        'Website',   '2024-01-22'),
('Ankit Gupta',     'CloudBase',          'Pune',       92, 2100000, 'Hot',         'Event',     '2024-02-01'),
('Sneha Patel',     'TechStart',          'Mumbai',     48,  180000, 'Cold',        'Cold Call', '2024-02-14'),
('Vikram Singh',    'Enterprise Ltd',     'Bengaluru',  78,  850000, 'Warm',        'Website',   '2024-02-20'),
('Deepa Nair',      'Analytics Co',       'Chennai',   55,  320000, 'Cold',        'Referral',  '2024-03-05'),
('Arjun Mehta',     'FinTech Pvt',        'Mumbai',    91, 1800000, 'Hot',         'Event',     '2024-03-10'),
('Kavitha Rao',     'HealthPlus',         'Hyderabad', 70,  620000, 'Warm',        'Website',   '2024-03-18'),
('Rajesh Kumar',    'LogiTech',           'Pune',       35,   95000, 'Unqualified', 'Cold Call', '2024-03-25'),
('Pooja Joshi',     'EduTech Ventures',   'Delhi',      83, 1100000, 'Hot',         'Referral',  '2024-04-02');


-- ─── QUERY 1: Select all columns ─────────────────────────────────────────────
-- Task: See all leads
SELECT * FROM leads;


-- ─── QUERY 2: Select specific columns ────────────────────────────────────────
-- Task: Show only name, city, score, and status
SELECT name, city, score, status
FROM leads;


-- ─── QUERY 3: WHERE — Filter rows ────────────────────────────────────────────
-- Task: Show only Hot leads
SELECT name, company, score, revenue
FROM leads
WHERE status = 'Hot';

-- Task: Leads with score above 75
SELECT name, score, status
FROM leads
WHERE score > 75;


-- ─── QUERY 4: Multiple conditions (AND / OR) ──────────────────────────────────
-- Task: Hot leads from Mumbai
SELECT name, city, score
FROM leads
WHERE status = 'Hot' AND city = 'Mumbai';

-- Task: Leads from Mumbai OR Delhi
SELECT name, city, score
FROM leads
WHERE city = 'Mumbai' OR city = 'Delhi';

-- Cleaner: use IN
SELECT name, city, score
FROM leads
WHERE city IN ('Mumbai', 'Delhi', 'Pune');


-- ─── QUERY 5: NOT and != ─────────────────────────────────────────────────────
-- Task: All leads who are NOT unqualified
SELECT name, score, status
FROM leads
WHERE status != 'Unqualified';

-- Same with NOT IN
SELECT name, score, status
FROM leads
WHERE status NOT IN ('Unqualified', 'Cold');


-- ─── QUERY 6: Ranges with BETWEEN ────────────────────────────────────────────
-- Task: Leads with score between 70 and 90
SELECT name, score
FROM leads
WHERE score BETWEEN 70 AND 90;


-- ─── QUERY 7: ORDER BY ───────────────────────────────────────────────────────
-- Task: Sort by score descending (highest first)
SELECT name, score, status
FROM leads
ORDER BY score DESC;

-- Task: Sort by city alphabetically, then score descending
SELECT name, city, score
FROM leads
ORDER BY city ASC, score DESC;


-- ─── QUERY 8: LIMIT ──────────────────────────────────────────────────────────
-- Task: Top 3 leads by score
SELECT name, score, revenue
FROM leads
ORDER BY score DESC
LIMIT 3;


-- ─── QUERY 9: DISTINCT ───────────────────────────────────────────────────────
-- Task: List unique cities where we have leads
SELECT DISTINCT city FROM leads ORDER BY city;

-- Task: Unique lead sources
SELECT DISTINCT source FROM leads;


-- ─── QUERY 10: LIKE — Pattern Matching ───────────────────────────────────────
-- Task: Leads whose name starts with 'P'
SELECT name FROM leads WHERE name LIKE 'P%';

-- Task: Leads whose company name contains 'Tech'
SELECT name, company FROM leads WHERE company LIKE '%Tech%';


-- ─── PRACTICE TASKS ──────────────────────────────────────────────────────────
-- Write your own queries for these:

-- 1. Show name, score, revenue for all Warm leads
-- 2. Show all leads from Bengaluru or Hyderabad
-- 3. Show top 5 leads by revenue
-- 4. List all unique statuses
-- 5. Show leads with revenue greater than 1,000,000
-- 6. Show leads that came from a Referral source
-- 7. Show the 3 leads with the lowest scores
-- 8. Find leads whose company name starts with 'Data'
