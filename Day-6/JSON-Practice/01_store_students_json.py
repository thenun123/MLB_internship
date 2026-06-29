# JSON Practice 1: Store student information in a JSON file

import json

def store_students_to_json():
    students = [
        {
            "id": "S001",
            "name": "Alice Johnson",
            "age": 20,
            "grade": "A",
            "subjects": ["Math", "Physics", "CS"],
            "gpa": 3.9
        },
        {
            "id": "S002",
            "name": "Bob Smith",
            "age": 21,
            "grade": "B",
            "subjects": ["English", "History", "Art"],
            "gpa": 3.2
        },
        {
            "id": "S003",
            "name": "Charlie Brown",
            "age": 19,
            "grade": "A+",
            "subjects": ["Math", "Chemistry", "Biology"],
            "gpa": 4.0
        },
        {
            "id": "S004",
            "name": "Diana Prince",
            "age": 22,
            "grade": "B+",
            "subjects": ["CS", "Math", "Statistics"],
            "gpa": 3.5
        },
    ]

    data = {
        "institution": "Python Learning Academy",
        "total_students": len(students),
        "students": students
    }

    filename = "students.json"

    # json.dump() writes Python dict → JSON file
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Student data saved to '{filename}'")
    print(f"Total students stored: {len(students)}")
    print("\nJSON Preview (first student):")
    print(json.dumps(students[0], indent=4))


store_students_to_json()
