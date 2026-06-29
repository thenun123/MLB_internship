# JSON Practice 3: Update an existing student's information

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


def update_student(filename, student_id, updated_fields):
    try:
        # Step 1: Read existing data
        with open(filename, "r") as file:
            data = json.load(file)

        # Step 2: Find the student
        found = False
        for student in data["students"]:
            if student["id"] == student_id:
                print(f"Found student: {student['name']}")
                print(f"Before update: {student}")

                # Step 3: Update fields
                student.update(updated_fields)

                print(f"After update : {student}")
                found = True
                break

        if not found:
            print(f"Student with ID '{student_id}' not found.")
            return

        # Step 4: Write back to file
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print(f"\nStudent '{student_id}' updated successfully in '{filename}'!")

    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{filename}'.")


if not os.path.exists("students.json"):
    create_sample_json()

print("=" * 50)
print("       UPDATING STUDENT RECORD")
print("=" * 50)

# Update Bob Smith's grade and GPA after re-exam
update_student(
    "students.json",
    "S002",
    {"grade": "A-", "gpa": 3.7}
)
