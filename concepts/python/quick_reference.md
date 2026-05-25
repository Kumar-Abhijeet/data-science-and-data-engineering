# Python Concepts — Quick Reference

## Data Types Cheat Sheet

| Type | Example | Mutable? | Use When |
|------|---------|----------|----------|
| `int` | `42` | No | Counts, IDs, indices |
| `float` | `3.14` | No | Prices, rates, measurements |
| `str` | `"hello"` | No | Text, names, labels |
| `bool` | `True` | No | Flags, conditions |
| `list` | `[1, 2, 3]` | Yes | Ordered, changeable collections |
| `tuple` | `(1, 2, 3)` | No | Fixed records, coordinates |
| `dict` | `{"a": 1}` | Yes | Key-value data (like a DB row) |
| `set` | `{1, 2, 3}` | Yes | Unique items, membership testing |
| `None` | `None` | — | Null / missing value |

---

## List vs Tuple vs Dict

```python
# Use LIST when order matters and data can change
monthly_sales = [45000, 52000, 38000]

# Use TUPLE when data is fixed / should not change
rgb_colour = (255, 128, 0)

# Use DICT when you have key-value pairs (like a record)
lead = {"name": "Priya", "score": 87, "status": "Hot"}
```

---

## Common String Methods

```python
s = "  Hello, World!  "
s.strip()            # "Hello, World!"
s.lower()            # "  hello, world!  "
s.upper()            # "  HELLO, WORLD!  "
s.title()            # "  Hello, World!  "
s.replace(",", "")   # "  Hello World!  "
s.split(", ")        # ["  Hello", "World!  "]
s.startswith("  H")  # True
"World" in s         # True
len(s)               # 18
f"Hi {s.strip()}"    # "Hi Hello, World!"
```

---

## f-string Format Specifiers

```python
x = 12345678.5
f"{x:,.2f}"     # "12,345,678.50"  — comma + 2 decimals
f"{x:.0f}"      # "12345679"       — no decimals
f"{x:e}"        # "1.234568e+07"   — scientific notation

pct = 0.8534
f"{pct:.1%}"    # "85.3%"

name = "Priya"
f"{name:>20}"   # "               Priya"  — right-align in 20 chars
f"{name:<20}"   # "Priya               "  — left-align
f"{name:^20}"   # "       Priya        "  — center
```

---

## Common Built-in Functions

```python
len([1, 2, 3])           # 3
sum([10, 20, 30])         # 60
max([10, 5, 20])          # 20
min([10, 5, 20])          # 5
sorted([3, 1, 2])         # [1, 2, 3]
sorted([3,1,2], reverse=True)   # [3, 2, 1]
enumerate(["a","b","c"])  # (0,'a'), (1,'b'), (2,'c')
zip([1,2], ["a","b"])     # (1,'a'), (2,'b')
range(1, 6)               # 1, 2, 3, 4, 5
type(42)                  # <class 'int'>
isinstance(42, int)       # True
```

---

## OOP Quick Reference

```python
class Animal:
    def __init__(self, name):   # constructor
        self.name = name        # instance attribute

    def speak(self):            # instance method
        return "..."

    @classmethod
    def from_string(cls, s):    # class method — alternative constructor
        return cls(s)

    @staticmethod
    def is_valid_name(n):       # static method — no self/cls
        return len(n) > 0

class Dog(Animal):              # inheritance
    def speak(self):            # override
        return f"{self.name} says Woof!"

    def fetch(self):
        return super().speak()  # call parent method
```

---

## Exception Handling Pattern

```python
try:
    result = risky_operation()
except SpecificError as e:
    handle_error(e)
except (TypeError, ValueError) as e:
    handle_type_or_value_error(e)
else:
    # runs only if NO exception occurred
    process(result)
finally:
    # ALWAYS runs — use for cleanup
    cleanup()
```
