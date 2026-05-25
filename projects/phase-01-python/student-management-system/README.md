# Project 2 — Student Management System

**Phase:** Python Foundations  
**Skills:** OOP, File Handling, Dictionaries, Lists, Functions

---

## 📋 Project Overview

Build a CLI Student Management System that:
- Adds, updates, and deletes student records
- Records marks for multiple subjects
- Calculates grade and GPA automatically
- Persists data in a JSON file
- Generates a student report card

---

## 🎯 Business Context

Educational institutions, coaching centres, and corporate L&D teams all track learner performance.
This system simulates the back end of a student information system (SIS).

---

## 🗂️ Folder Structure

```text
student-management-system/
├── README.md
├── student_manager.py      ← main application
├── models.py               ← Student class
└── data/
    └── students.json       ← persistent storage
```

---

## ⚙️ Features to Build

### Core
- [ ] Add student (name, roll number, class, subjects)
- [ ] Enter/update marks per subject
- [ ] Calculate average, grade (A/B/C/D/F), and pass/fail
- [ ] View all students as a table
- [ ] View individual report card
- [ ] Delete student record
- [ ] Persist data as JSON

### Grade Scale
| Marks | Grade |
|-------|-------|
| 90–100 | A+ |
| 80–89  | A  |
| 70–79  | B  |
| 60–69  | C  |
| 50–59  | D  |
| < 50   | F  |

---

## 💡 Hints

1. Create a `Student` class with attributes: `roll`, `name`, `class_name`, `marks` (dict).
2. Add a `calculate_grade(avg)` static method.
3. Store all students in a dict keyed by roll number.
4. Use `json.dump` / `json.load` for persistence.
5. Build each menu function separately and test before combining.
