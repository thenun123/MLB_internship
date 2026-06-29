# Practice 1: Create a text file and write data into it

def create_and_write_file():
    filename = "students.txt"

    students = [
        "Alice Johnson - Grade A",
        "Bob Smith - Grade B",
        "Charlie Brown - Grade A+",
        "Diana Prince - Grade B+",
        "Ethan Hunt - Grade C",
    ]

    with open(filename, "w") as file:
        file.write("=== Student List ===\n")
        for student in students:
            file.write(student + "\n")

    print(f"File '{filename}' created successfully!")
    print(f"Total students written: {len(students)}")


create_and_write_file()
