# JSON Practice 2: Read data from a JSON file

import json
import os

def create_sample_json():
    """Creates a sample JSON file if it doesn't exist."""
    data = {
        "institution": "Python Learning Academy",
        "total_students": 4,
        "students": [
            {"id": "S001", "name": "Alice Johnson", "age": 20, "grade": "A", "gpa": 3.9},
            {"id": "S002", "name": "Bob Smith", "age": 21, "grade": "B", "gpa": 3.2},
            {"id": "S003", "name": "Charlie Brown", "age": 19, "grade": "A+", "gpa": 4.0},
            {"id": "S004", "name": "Diana Prince", "age": 22, "grade": "B+", "gpa": 3.5},
        ]
    }
    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)


def read_json_file(filename):
    try:
        # json.load() reads JSON file → Python dict
        with open(filename, "r") as file:
            data = json.load(file)

        print(f"Institution : {data['institution']}")
        print(f"Total Students: {data['total_students']}")
        print("\n" + "=" * 50)
        print(f"{'ID':<8} {'Name':<20} {'Age':<5} {'Grade':<8} {'GPA'}")
        print("=" * 50)

        for student in data["students"]:
            print(
                f"{student['id']:<8} "
                f"{student['name']:<20} "
                f"{student['age']:<5} "
                f"{student['grade']:<8} "
                f"{student['gpa']}"
            )

        print("=" * 50)

        # Find top student
        top = max(data["students"], key=lambda s: s["gpa"])
        print(f"\n🏆 Top Student: {top['name']} with GPA {top['gpa']}")

    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: '{filename}' contains invalid JSON.")


if not os.path.exists("students.json"):
    create_sample_json()

read_json_file("students.json")
