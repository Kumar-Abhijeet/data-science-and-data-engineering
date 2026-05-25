# Day 1 — Variables and Data Types

## 1. Concept Overview

In Python, a **variable** is a named container that holds a value.
A **data type** tells Python what kind of value is stored — a number, text, True/False, etc.

Think of variables like labelled boxes on a shelf in a warehouse.
The label is the variable name. The box holds the data. The type of box depends on what you put inside.

---

## 2. Why It Matters

Every program you write stores and manipulates data.
Before you can analyse sales figures, clean a dataset, or build a model — you need to understand how Python stores values.

**Business context:**  
A sales report stores revenue as numbers, product names as text, and "is_active" as True/False.
Python uses data types to handle all of these correctly.

---

## 3. Real Business Use Case

Imagine you are building a lead tracking system:

```
lead_name = "Priya Sharma"       # text (str)
lead_score = 87                  # whole number (int)
revenue_potential = 145000.50    # decimal number (float)
is_contacted = False             # yes/no (bool)
```

Every variable has a name, a value, and a type.
Python figures out the type automatically — this is called **dynamic typing**.

---

## 4. Step-by-Step Theory

### 4.1 Variables

A variable is created the moment you assign a value to it.

```python
name = "Abhijeet"    # creates a variable called 'name'
age = 28             # creates a variable called 'age'
```

**Rules for variable names:**
- Start with a letter or underscore (`_`), never a number
- No spaces — use underscores: `lead_score`, not `lead score`
- Case-sensitive: `Name` and `name` are different variables
- Cannot use Python keywords: `for`, `if`, `class`, `return`, etc.

**Naming convention used by professionals:**
```python
# snake_case — words separated by underscores (Python standard)
monthly_revenue = 50000
customer_name = "Rahul"

# UPPER_CASE — for constants (values that never change)
MAX_RETRIES = 3
TAX_RATE = 0.18
```

---

### 4.2 Core Data Types

| Type | Name | Example |
|------|------|---------|
| `int` | Integer | `age = 25` |
| `float` | Decimal | `salary = 75000.50` |
| `str` | String / Text | `name = "Priya"` |
| `bool` | Boolean (True/False) | `is_active = True` |
| `NoneType` | Null / Missing | `result = None` |

---

### 4.3 Checking the Type

```python
x = 42
print(type(x))        # <class 'int'>

y = 3.14
print(type(y))        # <class 'float'>

z = "hello"
print(type(z))        # <class 'str'>

flag = True
print(type(flag))     # <class 'bool'>
```

---

### 4.4 Type Conversion (Casting)

Sometimes you need to convert one type to another.

```python
# String to integer
age_str = "28"
age_int = int(age_str)      # 28

# Integer to float
price = float(100)          # 100.0

# Number to string (useful when printing)
salary = 75000
message = "Salary: " + str(salary)

# String to float
revenue = float("12500.75")  # 12500.75
```

> ⚠️ Common mistake: `int("hello")` raises a ValueError — you can only convert valid numeric strings.

---

### 4.5 Strings in Detail

Strings are sequences of characters wrapped in quotes.

```python
# Both work — use one style consistently
first_name = "Rahul"
last_name  = 'Kumar'

# Multi-line string
address = """
123 MG Road,
Bengaluru, Karnataka,
560001
"""

# f-strings — the modern way to insert variables into strings
name = "Priya"
score = 92
message = f"Hi {name}, your lead score is {score}."
print(message)  # Hi Priya, your lead score is 92.
```

**Useful string properties:**
```python
text = "  Hello, World!  "
print(len(text))            # length: 18
print(text.strip())         # removes spaces: "Hello, World!"
print(text.lower())         # "  hello, world!  "
print(text.upper())         # "  HELLO, WORLD!  "
print(text.replace("World", "Python"))
```

---

### 4.6 Getting Input from Users

```python
name = input("Enter your name: ")
print(f"Welcome, {name}!")

# input() always returns a string — convert when needed
age = int(input("Enter your age: "))
print(f"In 10 years you will be {age + 10}.")
```

---

## 5. Guided Coding

Open `practice.py` and type (don't copy-paste) each block. Observe the output.

```python
# --- Block 1: Variable assignment and printing ---
company = "TechCorp"
employees = 250
revenue = 4500000.75
is_profitable = True

print(company)
print(employees)
print(revenue)
print(is_profitable)

# --- Block 2: Types ---
print(type(company))
print(type(employees))
print(type(revenue))
print(type(is_profitable))

# --- Block 3: f-strings ---
print(f"{company} has {employees} employees and revenue of ₹{revenue:,.2f}")

# --- Block 4: Type conversion ---
user_input = "5000"
converted = int(user_input) * 2
print(f"Double the value: {converted}")
```

---

## 6. Practice Tasks

Try these yourself before looking at solutions:

1. Create variables to represent a product: `product_name`, `price`, `quantity`, `in_stock` (bool).
   Print a summary sentence using an f-string.

2. Ask the user for their name and age. Print:
   `"Hello [name]! You will retire in [65 - age] years."`

3. Given `price = "1299.99"`, convert it to a float and apply 18% GST. Print the final price.

4. Create a variable `full_name = "   Abhijeet Kumar   "` and print it with whitespace removed, in uppercase.

5. What happens if you do `int("12.5")`? Try it and explain the error.

---

## 7. Debugging Practice

Find and fix the errors in these code snippets:

```python
# Bug 1
1name = "Rahul"
print(1name)

# Bug 2
salary = "75000"
bonus = salary * 0.10
print(bonus)

# Bug 3
message = f"Revenue is {revenue}"
revenue = 500000

# Bug 4
print("Name: " + 42)
```

---

## 8. Interview Questions

1. What is the difference between `int` and `float`?
2. Is Python statically or dynamically typed? What does that mean?
3. What is the output of `type(True)`? Why?
4. What is the difference between `=` and `==` in Python?
5. What does `None` represent? Give a business example.
6. Can you use a number as a variable name? Why or why not?
7. What is an f-string and why do professionals prefer it over `+` string concatenation?
8. What happens when you do `int("hello")`?

---

## 9. Mini Project

**Business Problem:** Build a "Lead Profile Generator"

A sales team wants a quick tool that takes basic info about a lead and prints a formatted profile.

**Requirements:**
- Ask for: lead name, company, annual revenue, lead score (0–100), and whether they have been contacted (yes/no)
- Convert revenue to float, score to int, contacted to bool
- Print a formatted profile card like:

```
=============================
       LEAD PROFILE
=============================
Name    : Priya Sharma
Company : Innovate Solutions
Revenue : ₹12,50,000.00
Score   : 87 / 100
Status  : Contacted ✓
=============================
```

**Hint:** Use `input()`, type conversion, f-strings, and string formatting.

---

## 10. Next Step Roadmap

Once you complete this module:
→ Move to **Day 2 — Operators & Expressions** in `../02-operators-and-expressions/`

You will learn:
- Arithmetic operators (+, -, *, /, //, %, **)
- Comparison operators (==, !=, >, <, >=, <=)
- Logical operators (and, or, not)
- String operations and methods

These are the building blocks for writing conditional logic and calculations — essential for data analysis.
