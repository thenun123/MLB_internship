# Practice 3: Append new data to an existing file

def append_to_file():
    filename = "students.txt"

    new_students = [
        "Fatima Khan - Grade A",
        "George Miller - Grade B+",
        "Hannah Lee - Grade A-",
    ]

    # Append mode ('a') adds to the end without erasing existing content
    with open(filename, "a") as file:
        file.write("\n=== Newly Added Students ===\n")
        for student in new_students:
            file.write(student + "\n")

    print(f"Successfully appended {len(new_students)} new students to '{filename}'")

    # Verify by reading the full file
    print("\nUpdated file contents:")
    print("-" * 30)
    with open(filename, "r") as file:
        print(file.read())


# Create the file first if it doesn't exist
import os
if not os.path.exists("students.txt"):
    with open("students.txt", "w") as f:
        f.write("=== Student List ===\n")
        f.write("Alice Johnson - Grade A\n")
        f.write("Bob Smith - Grade B\n")

append_to_file()
