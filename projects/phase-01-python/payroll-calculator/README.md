# Project 3 — Payroll Calculator (Portfolio Project)

**Phase:** Python Foundations  
**Skills:** OOP with inheritance, File Handling, Calculations, Reporting

---

## 📋 Project Overview

Build an OOP-based Payroll Calculator that:
- Handles three employee types: Salaried, Contract, and Intern
- Calculates gross pay, tax (slab-based), PF, net pay
- Generates payslips (formatted and saved to file)
- Produces a monthly payroll summary report

---

## 🎯 Business Context

Every HR team runs monthly payroll. This project simulates the core calculation engine of an HRMS (Human Resource Management System) like SAP or Zoho Payroll.

---

## 💰 Payroll Logic

### Tax Slabs (Simplified)
| Annual Income | Tax Rate |
|---------------|---------|
| Up to ₹3,00,000 | 0% |
| ₹3,00,001 – ₹6,00,000 | 5% |
| ₹6,00,001 – ₹12,00,000 | 20% |
| Above ₹12,00,000 | 30% |

### Deductions
- PF (Provident Fund): 12% of basic salary
- Professional Tax: ₹200/month (salaried only)
- TDS: monthly tax deduction at source

### Allowances (Salaried)
- HRA: 40% of basic (non-metro) or 50% (metro)
- DA (Dearness Allowance): 17% of basic
- Transport Allowance: ₹3,200/month

---

## 🗂️ Structure

```text
payroll-calculator/
├── README.md
├── payroll.py          ← Employee classes and calculations
├── main.py             ← CLI menu
├── reports.py          ← Payslip and summary generation
└── data/
    ├── employees.json
    └── payslips/       ← generated payslip files
```

---

## ⚙️ Features to Build

- [ ] `Employee` base class with common attributes
- [ ] `SalariedEmployee`, `ContractEmployee`, `Intern` subclasses
- [ ] `calculate_gross()`, `calculate_tax()`, `calculate_net()` methods
- [ ] `generate_payslip()` → writes formatted .txt file
- [ ] Monthly payroll summary → total cost, headcount by type
- [ ] Load/save employee records from JSON

---

## 💡 This is a Portfolio Project

When complete, you should be able to:
- Explain the class hierarchy to an interviewer
- Demo the payslip generation
- Discuss what `super().__init__()` does
- Explain why you used OOP instead of plain functions
