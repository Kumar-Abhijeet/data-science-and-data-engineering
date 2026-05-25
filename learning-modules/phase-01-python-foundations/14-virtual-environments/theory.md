# Day 14 — Virtual Environments

## 1. What is a Virtual Environment?

A virtual environment is an isolated Python installation for your project.

Think of it like this:
- Your laptop has one "global" Python.
- Each project may need different library versions.
- A virtual environment creates a private Python + packages just for that project.

**Without virtual environments:** Installing a library for Project A might break Project B.  
**With virtual environments:** Each project has its own packages, versions, and Python.

---

## 2. Why Professionals Always Use Them

In a company:
- Project A uses `pandas 1.5` (legacy dashboard)
- Project B uses `pandas 2.0` (new ML pipeline)
- They cannot share the same Python installation

Virtual environments solve this.

---

## 3. Setting Up a Virtual Environment

### Step 1 — Create
```bash
# Inside your project folder
python -m venv venv
```
This creates a `venv/` folder containing a standalone Python installation.

### Step 2 — Activate
```bash
# Windows (Command Prompt)
venv\Scripts\activate

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```
You will see `(venv)` in your terminal prompt when active.

### Step 3 — Install packages
```bash
pip install pandas numpy matplotlib
```
These are installed only inside the virtual environment.

### Step 4 — Verify
```bash
pip list              # show installed packages
which python          # show which Python is being used (macOS/Linux)
where python          # show which Python is being used (Windows)
```

---

## 4. requirements.txt

This file lists all dependencies so others can recreate your environment.

### Create it
```bash
pip freeze > requirements.txt
```

### Recreate an environment from it
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Example requirements.txt
```
numpy==1.24.3
pandas==2.0.2
matplotlib==3.7.1
scikit-learn==1.3.0
```

---

## 5. .gitignore for Virtual Environments

**Never commit** the `venv/` folder to Git — it is large (100+ MB) and machine-specific.

Add this to `.gitignore`:
```
venv/
.venv/
env/
```

Commit only `requirements.txt`. Anyone can recreate the environment from it.

---

## 6. VS Code Integration

1. Open the Command Palette: `Ctrl+Shift+P`
2. Type `Python: Select Interpreter`
3. Choose the interpreter inside your `venv/` folder
4. VS Code will automatically activate the venv in the terminal

---

## 7. Practical Exercise

In your terminal, follow these steps exactly:

```bash
# Navigate to the phase-01 project folder
cd projects/phase-01-python/expense-tracker

# Create a virtual environment
python -m venv venv

# Activate it
source venv/bin/activate    # or venv\Scripts\activate on Windows

# Install dependencies
pip install rich            # a library for beautiful terminal output

# Check what is installed
pip list

# Export dependencies
pip freeze > requirements.txt

# Check the file
cat requirements.txt

# Deactivate when done
deactivate
```

---

## 8. Interview Questions

1. What is the difference between `pip install X` and adding X to `requirements.txt`?
2. Can two projects on the same machine use different versions of the same library?
3. What happens if you delete the `venv/` folder? How do you recreate it?
4. Why should `venv/` be in `.gitignore`?
5. What command shows all currently installed packages in the active environment?

---

## 9. Next Step

You have now completed all 14 modules of Phase 1 — Python Foundations.

→ Start the **Expense Tracker Project** in `../../projects/phase-01-python/expense-tracker/`  
→ Then move to **Phase 2 — Data Analysis** when your Phase 1 checklist is complete.
