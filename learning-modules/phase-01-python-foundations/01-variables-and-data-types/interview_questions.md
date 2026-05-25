# Day 1 — Variables and Data Types: Interview Questions

## Conceptual Questions

**Q1. What is the difference between `int` and `float`?**  
`int` stores whole numbers (e.g., 42, -10).  
`float` stores decimal numbers (e.g., 3.14, -0.5).  
Use `int` for counts, IDs, indices. Use `float` for measurements, prices, rates.

---

**Q2. Is Python statically or dynamically typed? What does that mean?**  
Python is **dynamically typed**. You do not declare a type when creating a variable.  
Python figures out the type at runtime based on the value assigned.  
`x = 5` makes x an int. `x = "hello"` makes x a str.  
Compare with Java (static typing) where you must write `int x = 5;`.

---

**Q3. What is the output of `type(True)`? Why?**  
Output: `<class 'bool'>`  
In Python, `bool` is a subclass of `int`. `True == 1` and `False == 0`.  
This means `True + True` evaluates to `2`.

---

**Q4. What is the difference between `=` and `==` in Python?**  
`=` is **assignment** — stores a value: `x = 5`  
`==` is **comparison** — checks equality: `x == 5` returns `True` or `False`  
Mixing them up is one of the most common beginner bugs.

---

**Q5. What does `None` represent? Give a business example.**  
`None` is Python's null value — it means "no value / missing / not set yet".  
Example: A lead in a CRM where the phone number field has not been filled in:  
`lead_phone = None`  
In data analysis, missing values in a DataFrame column often appear as `None` or `NaN`.

---

**Q6. What happens when you do `int("hello")`?**  
It raises a `ValueError: invalid literal for int() with base 10: 'hello'`  
`int()` can only convert strings that represent valid integers: `int("42")` → 42.

---

**Q7. What is an f-string and why do professionals prefer it?**  
An f-string (formatted string literal) is a way to embed variables inside a string.  
`f"Revenue: ₹{revenue:,.2f}"` is more readable and faster than:  
`"Revenue: ₹" + str(revenue)` or `"Revenue: ₹{}".format(revenue)`  
f-strings also support expressions and format specifiers directly.

---

**Q8. Can a Python variable name start with a number?**  
No. Variable names must start with a letter (a–z, A–Z) or underscore (_).  
`1name = "test"` raises a `SyntaxError`.  
`_name` and `name1` are both valid.

---

## Quick-Fire Questions (for mock interviews)

- What is the default type returned by `input()`? → `str`
- What does `len("hello")` return? → `5`
- Is `None` the same as `False`? → No, but both are falsy.
- What is the output of `type(1.0)`? → `<class 'float'>`
- How do you check if a variable is `None`? → `if x is None:`
