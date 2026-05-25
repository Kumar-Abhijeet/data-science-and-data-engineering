"""
Day 13 — Modules and Packages
Practice File

A MODULE is a single Python file (.py) you can import.
A PACKAGE is a folder of modules with an __init__.py file.
"""
import math
import random
import datetime
import os
import sys

# ─── SECTION 1: Standard Library Modules ────────────────────────────────────

# math — mathematical functions
revenue = 1250000
print(f"Square root of revenue: {math.sqrt(revenue):,.2f}")
print(f"Ceil(4.3): {math.ceil(4.3)}")
print(f"Floor(4.9): {math.floor(4.9)}")
print(f"Pi: {math.pi:.6f}")


# random — random number generation
print("\n--- Random Sampling ---")
lead_scores = list(range(50, 100))
sample = random.sample(lead_scores, 5)       # pick 5 without replacement
print(f"Random lead scores: {sample}")
print(f"Random choice: {random.choice(['Hot', 'Warm', 'Cold'])}")


# datetime — date and time operations
print("\n--- DateTime ---")
today = datetime.date.today()
now = datetime.datetime.now()
print(f"Today  : {today}")
print(f"Now    : {now.strftime('%d %b %Y %H:%M')}")

# Calculate days since campaign start
campaign_start = datetime.date(2024, 1, 1)
days_running = (today - campaign_start).days
print(f"Campaign running for {days_running} days")


# os — file system operations
print("\n--- OS Module ---")
print(f"Current directory: {os.getcwd()}")
print(f"Path exists /tmp  : {os.path.exists('/tmp')}")

home = os.path.expanduser("~")
print(f"Home directory: {home}")


# ─── SECTION 2: from ... import ... ─────────────────────────────────────────

from math import sqrt, pi
from datetime import date, timedelta
from os.path import join, exists

print(f"\nsqrt(144) = {sqrt(144)}")
print(f"pi = {pi:.4f}")

# date arithmetic
tomorrow = date.today() + timedelta(days=1)
next_week = date.today() + timedelta(weeks=1)
print(f"Tomorrow  : {tomorrow}")
print(f"Next week : {next_week}")


# ─── SECTION 3: import as (alias) ────────────────────────────────────────────

# In data science, conventional aliases are used everywhere:
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

import datetime as dt
today2 = dt.date.today()
print(f"\nToday (aliased): {today2}")


# ─── SECTION 4: Creating Your Own Module ─────────────────────────────────────

# Save this as /tmp/lead_utils.py, then import it

module_code = '''
"""Utility functions for lead management."""

def classify_lead(score):
    if score >= 85:
        return "Hot"
    elif score >= 70:
        return "Warm"
    elif score >= 50:
        return "Cold"
    return "Unqualified"

def calculate_conversion_rate(converted, total):
    if total == 0:
        return 0.0
    return round((converted / total) * 100, 2)
'''

# Write the module to /tmp
with open("/tmp/lead_utils.py", "w") as f:
    f.write(module_code)

# Add /tmp to path so Python can find it
sys.path.insert(0, "/tmp")
import lead_utils

print("\n--- Using Custom Module ---")
print(lead_utils.classify_lead(88))
print(f"Conversion rate: {lead_utils.calculate_conversion_rate(28, 142)}%")
