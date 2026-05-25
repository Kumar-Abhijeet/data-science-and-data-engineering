"""
Student Management System
Project 2 of Phase 1: Python Foundations

Build this yourself using the README hints.
"""
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "students.json")


class Student:
    """Represents a student record."""

    def __init__(self, roll, name, class_name, marks=None):
        self.roll = roll
        self.name = name
        self.class_name = class_name
        self.marks = marks or {}    # {"Math": 85, "Science": 72, ...}

    def average(self):
        """Calculate average marks."""
        # TODO: return average of self.marks values, or 0 if empty
        pass

    def grade(self):
        """Return letter grade based on average."""
        # TODO: implement the grade scale from README
        pass

    def is_pass(self):
        """Fail if any subject < 35 or average < 50."""
        # TODO: implement
        pass

    def to_dict(self):
        """Serialise to dictionary for JSON storage."""
        return {
            "roll": self.roll,
            "name": self.name,
            "class_name": self.class_name,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Student from a dictionary."""
        return cls(data["roll"], data["name"], data["class_name"], data["marks"])

    def report_card(self):
        """Return formatted report card string."""
        # TODO: build a multi-line string showing all subjects, marks, average, grade
        pass


# ─── Data Layer ───────────────────────────────────────────────────────────────

def load_students():
    """Load students from JSON. Returns dict keyed by roll."""
    # TODO: implement
    return {}


def save_students(students):
    """Save students dict to JSON."""
    # TODO: implement
    pass


# ─── Core Functions ───────────────────────────────────────────────────────────

def add_student(students):
    # TODO: implement
    pass


def update_marks(students):
    # TODO: implement
    pass


def view_all(students):
    # TODO: display table of all students with roll, name, class, avg, grade
    pass


def view_report(students):
    # TODO: ask for roll, print report card
    pass


def delete_student(students):
    # TODO: implement
    pass


# ─── Menu ─────────────────────────────────────────────────────────────────────

def main():
    students = load_students()

    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add student")
        print("2. Update marks")
        print("3. View all students")
        print("4. View report card")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Choice: ").strip()
        actions = {
            "1": lambda: add_student(students),
            "2": lambda: update_marks(students),
            "3": lambda: view_all(students),
            "4": lambda: view_report(students),
            "5": lambda: delete_student(students),
        }

        if choice == "6":
            print("Goodbye!")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
