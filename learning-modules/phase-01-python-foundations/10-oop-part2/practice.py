"""
Day 10 — OOP Part 2: Inheritance, Encapsulation, Polymorphism
Practice File
"""

# ─── SECTION 1: Inheritance ───────────────────────────────────────────────────

# Inheritance lets a child class reuse and extend the parent class.
# WHY: avoids code duplication when objects share common behaviour.

class Employee:
    """Base class for all employees."""

    def __init__(self, name, emp_id, department, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.base_salary = base_salary

    def get_details(self):
        return f"[{self.emp_id}] {self.name} — {self.department}"

    def calculate_pay(self):
        """Override this in child classes for specific pay logic."""
        return self.base_salary

    def __str__(self):
        return f"Employee({self.name}, ₹{self.calculate_pay():,.0f}/month)"


class SalariedEmployee(Employee):
    """Full-time salaried employee with HRA and transport allowance."""

    HRA_RATE = 0.40        # 40% of base salary
    TRANSPORT = 3000

    def calculate_pay(self):
        hra = self.base_salary * self.HRA_RATE
        return self.base_salary + hra + self.TRANSPORT


class ContractEmployee(Employee):
    """Hourly contract employee."""

    def __init__(self, name, emp_id, department, hourly_rate, hours_worked):
        super().__init__(name, emp_id, department, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked


class SalesEmployee(SalariedEmployee):
    """Sales employee with additional commission."""

    def __init__(self, name, emp_id, base_salary, sales_achieved, commission_rate=0.05):
        super().__init__(name, emp_id, "Sales", base_salary)
        self.sales_achieved = sales_achieved
        self.commission_rate = commission_rate

    def calculate_pay(self):
        base_pay = super().calculate_pay()    # get parent's salary+HRA+transport
        commission = self.sales_achieved * self.commission_rate
        return base_pay + commission


# ─── SECTION 2: Using the Classes ─────────────────────────────────────────────

print("--- Payroll ---")
employees = [
    SalariedEmployee("Priya Sharma", "E001", "Engineering", 80000),
    ContractEmployee("Rahul Verma", "C001", "Design", 1500, 160),
    SalesEmployee("Ankit Gupta", "E002", 60000, sales_achieved=350000),
]

for emp in employees:
    print(f"{emp.get_details():<40}  Pay: ₹{emp.calculate_pay():>10,.2f}")


# ─── SECTION 3: isinstance() and type checking ───────────────────────────────

print("\n--- Type Checks ---")
for emp in employees:
    print(f"{emp.name:<15}: SalariedEmployee? {isinstance(emp, SalariedEmployee)}")


# ─── SECTION 4: Encapsulation ─────────────────────────────────────────────────

# Encapsulation = hiding internal data; exposing only what is needed
# Convention: prefix with _ for "internal", __ for "private"

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance    # double underscore = private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"  Deposited ₹{amount:,.0f}. New balance: ₹{self.__balance:,.0f}")
        else:
            print("  Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"  Withdrew ₹{amount:,.0f}. Remaining: ₹{self.__balance:,.0f}")
        else:
            print("  Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance


print("\n--- Bank Account ---")
acc = BankAccount("Priya", 50000)
acc.deposit(20000)
acc.withdraw(15000)
print(f"  Balance: ₹{acc.get_balance():,.0f}")
# acc.__balance  # ← raises AttributeError — truly private


# ─── SECTION 5: Polymorphism ──────────────────────────────────────────────────

# Polymorphism = same method name, different behaviour in each class

print("\n--- Polymorphism Demo ---")
class CSVExporter:
    def export(self, data):
        return f"Exporting {len(data)} rows to CSV..."

class JSONExporter:
    def export(self, data):
        return f"Serialising {len(data)} records to JSON..."

class ExcelExporter:
    def export(self, data):
        return f"Writing {len(data)} rows to Excel worksheet..."


data = [1, 2, 3, 4, 5]
exporters = [CSVExporter(), JSONExporter(), ExcelExporter()]
for exporter in exporters:
    print(f"  {exporter.__class__.__name__}: {exporter.export(data)}")
