# JSON Practice 4: Add a new student to the JSON file

import json
import os

def create_sample_json():
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


def generate_next_id(students):
    """Auto-generate next student ID."""
    if not students:
        return "S001"
    last_id = max(int(s["id"][1:]) for s in students)
    return f"S{str(last_id + 1).zfill(3)}"


def add_student(filename, new_student):
    try:
        # Read existing data
        with open(filename, "r") as file:
            data = json.load(file)

        # Auto-assign ID
        new_student["id"] = generate_next_id(data["students"])

        # Check for duplicate name
        existing_names = [s["name"].lower() for s in data["students"]]
        if new_student["name"].lower() in existing_names:
            print(f"Warning: A student named '{new_student['name']}' already exists.")
            return

        # Add to list
        data["students"].append(new_student)
        data["total_students"] = len(data["students"])

        # Save back
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print(f"New student added successfully!")
        print(f"Assigned ID : {new_student['id']}")
        print(f"Name        : {new_student['name']}")
        print(f"Total students now: {data['total_students']}")

    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{filename}'.")


if not os.path.exists("students.json"):
    create_sample_json()

print("=" * 50)
print("       ADDING NEW STUDENT")
print("=" * 50)

add_student("students.json", {
    "name": "Ethan Hunt",
    "age": 23,
    "grade": "B+",
    "gpa": 3.6
})

print("\n--- Adding another student ---\n")

add_student("students.json", {
    "name": "Fatima Khan",
    "age": 20,
    "grade": "A",
    "gpa": 3.8
})
