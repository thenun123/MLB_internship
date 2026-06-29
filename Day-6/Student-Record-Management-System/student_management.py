"""
=============================================================
  Student Record Management System - Persistent Version
  Day 6 Mini Project | MLB Python Bootcamp
=============================================================
  Features:
    - Save & load records from JSON file
    - Add, update, search, delete students
    - Exception handling for invalid inputs
    - Auto ID generation
=============================================================
"""

import json
import os

DATA_FILE = "students_data.json"


# ─────────────────────────────────────────────
#  FILE OPERATIONS
# ─────────────────────────────────────────────

def load_records():
    """Load student records from JSON file. Returns empty list if file missing."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data.get("students", [])
    except (json.JSONDecodeError, KeyError):
        print("[Warning] Data file is corrupted. Starting fresh.")
        return []


def save_records(students):
    """Save all student records to JSON file."""
    data = {
        "institution": "Python Learning Academy",
        "total_students": len(students),
        "students": students
    }
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ─────────────────────────────────────────────
#  ID GENERATION
# ─────────────────────────────────────────────

def generate_id(students):
    if not students:
        return "S001"
    last_num = max(int(s["id"][1:]) for s in students)
    return f"S{str(last_num + 1).zfill(3)}"


# ─────────────────────────────────────────────
#  DISPLAY
# ─────────────────────────────────────────────

def display_all(students):
    if not students:
        print("\n  No student records found.")
        return

    print("\n" + "=" * 65)
    print(f"  {'ID':<8} {'Name':<20} {'Age':<5} {'Grade':<8} {'GPA':<6} {'Email'}")
    print("=" * 65)
    for s in students:
        contact = s.get("contact", {})
        email = contact.get("email", "N/A")
        print(
            f"  {s['id']:<8} {s['name']:<20} {s['age']:<5} "
            f"{s['grade']:<8} {s['gpa']:<6} {email}"
        )
    print("=" * 65)
    print(f"  Total Students: {len(students)}")


def display_student(s):
    contact = s.get("contact", {})
    subjects = ", ".join(s.get("subjects", []))
    print("\n" + "-" * 40)
    print(f"  ID       : {s['id']}")
    print(f"  Name     : {s['name']}")
    print(f"  Age      : {s['age']}")
    print(f"  Grade    : {s['grade']}")
    print(f"  GPA      : {s['gpa']}")
    print(f"  Subjects : {subjects if subjects else 'N/A'}")
    print(f"  Email    : {contact.get('email', 'N/A')}")
    print(f"  Phone    : {contact.get('phone', 'N/A')}")
    print("-" * 40)


# ─────────────────────────────────────────────
#  INPUT HELPERS
# ─────────────────────────────────────────────

def input_name():
    while True:
        name = input("  Enter name: ").strip()
        if len(name) >= 2:
            return name
        print("  [Error] Name must be at least 2 characters.")


def input_age():
    while True:
        try:
            age = int(input("  Enter age: ").strip())
            if 10 <= age <= 100:
                return age
            print("  [Error] Age must be between 10 and 100.")
        except ValueError:
            print("  [Error] Please enter a valid number.")


def input_gpa():
    while True:
        try:
            gpa = float(input("  Enter GPA (0.0 - 4.0): ").strip())
            if 0.0 <= gpa <= 4.0:
                return round(gpa, 2)
            print("  [Error] GPA must be between 0.0 and 4.0.")
        except ValueError:
            print("  [Error] Please enter a valid decimal number.")


def input_grade():
    valid_grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]
    while True:
        grade = input(f"  Enter grade {valid_grades}: ").strip().upper()
        if grade in valid_grades:
            return grade
        print(f"  [Error] Invalid grade. Choose from: {valid_grades}")


# ─────────────────────────────────────────────
#  CORE OPERATIONS
# ─────────────────────────────────────────────

def add_student(students):
    print("\n  ── Add New Student ──")
    name = input_name()

    # Duplicate check
    for s in students:
        if s["name"].lower() == name.lower():
            print(f"  [Warning] A student named '{name}' already exists (ID: {s['id']}).")
            return

    age = input_age()
    grade = input_grade()
    gpa = input_gpa()

    subjects_input = input("  Enter subjects (comma-separated, or press Enter to skip): ").strip()
    subjects = [sub.strip() for sub in subjects_input.split(",") if sub.strip()] if subjects_input else []

    email = input("  Enter email (or press Enter to skip): ").strip()
    phone = input("  Enter phone (or press Enter to skip): ").strip()

    new_student = {
        "id": generate_id(students),
        "name": name,
        "age": age,
        "grade": grade,
        "gpa": gpa,
        "subjects": subjects,
        "contact": {
            "email": email if email else "N/A",
            "phone": phone if phone else "N/A"
        }
    }

    students.append(new_student)
    save_records(students)
    print(f"\n  ✅ Student '{name}' added successfully with ID: {new_student['id']}")


def search_student(students):
    print("\n  ── Search Student ──")
    query = input("  Enter name or ID to search: ").strip().lower()

    results = [
        s for s in students
        if query in s["name"].lower() or query == s["id"].lower()
    ]

    if not results:
        print(f"  No student found matching '{query}'.")
    else:
        print(f"  Found {len(results)} result(s):")
        for s in results:
            display_student(s)


def update_student(students):
    print("\n  ── Update Student ──")
    student_id = input("  Enter Student ID to update: ").strip().upper()

    for s in students:
        if s["id"] == student_id:
            print(f"  Updating: {s['name']}")
            print("  (Press Enter to keep current value)\n")

            name = input(f"  New name [{s['name']}]: ").strip()
            if name:
                s["name"] = name

            age_input = input(f"  New age [{s['age']}]: ").strip()
            if age_input:
                try:
                    age = int(age_input)
                    if 10 <= age <= 100:
                        s["age"] = age
                    else:
                        print("  [Skipped] Invalid age range.")
                except ValueError:
                    print("  [Skipped] Invalid age input.")

            grade_input = input(f"  New grade [{s['grade']}]: ").strip().upper()
            valid_grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]
            if grade_input in valid_grades:
                s["grade"] = grade_input
            elif grade_input:
                print("  [Skipped] Invalid grade.")

            gpa_input = input(f"  New GPA [{s['gpa']}]: ").strip()
            if gpa_input:
                try:
                    gpa = float(gpa_input)
                    if 0.0 <= gpa <= 4.0:
                        s["gpa"] = round(gpa, 2)
                    else:
                        print("  [Skipped] GPA out of range.")
                except ValueError:
                    print("  [Skipped] Invalid GPA input.")

            save_records(students)
            print(f"\n  ✅ Student '{s['name']}' (ID: {student_id}) updated successfully.")
            return

    print(f"  [Error] No student found with ID '{student_id}'.")


def delete_student(students):
    print("\n  ── Delete Student ──")
    student_id = input("  Enter Student ID to delete: ").strip().upper()

    for i, s in enumerate(students):
        if s["id"] == student_id:
            confirm = input(f"  Are you sure you want to delete '{s['name']}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                removed = students.pop(i)
                save_records(students)
                print(f"\n  ✅ Student '{removed['name']}' (ID: {student_id}) deleted successfully.")
            else:
                print("  Deletion cancelled.")
            return

    print(f"  [Error] No student found with ID '{student_id}'.")


def show_statistics(students):
    if not students:
        print("\n  No data available for statistics.")
        return

    gpas = [s["gpa"] for s in students]
    avg_gpa = sum(gpas) / len(gpas)
    top = max(students, key=lambda s: s["gpa"])
    lowest = min(students, key=lambda s: s["gpa"])

    print("\n" + "=" * 40)
    print("        STATISTICS SUMMARY")
    print("=" * 40)
    print(f"  Total Students : {len(students)}")
    print(f"  Average GPA    : {avg_gpa:.2f}")
    print(f"  Highest GPA    : {top['gpa']} ({top['name']})")
    print(f"  Lowest GPA     : {lowest['gpa']} ({lowest['name']})")
    print("=" * 40)


# ─────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────

def main():
    print("\n" + "=" * 55)
    print("   🎓 Student Record Management System")
    print("      Persistent Version | Day 6 Project")
    print("=" * 55)

    # Auto-load on startup
    students = load_records()
    print(f"\n  ✅ Loaded {len(students)} student record(s) from '{DATA_FILE}'")

    while True:
        print("\n" + "-" * 40)
        print("  MENU")
        print("-" * 40)
        print("  1. View All Students")
        print("  2. Add Student")
        print("  3. Search Student")
        print("  4. Update Student")
        print("  5. Delete Student")
        print("  6. View Statistics")
        print("  7. Exit")
        print("-" * 40)

        choice = input("  Enter choice (1-7): ").strip()

        if choice == "1":
            display_all(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            show_statistics(students)
        elif choice == "7":
            print("\n  Goodbye! All records are saved. 👋\n")
            break
        else:
            print("  [Error] Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
