# Practice 2: Read and display file contents

def read_file_contents():
    filename = "students.txt"

    # First, create the file if it doesn't exist
    try:
        with open(filename, "r") as file:
            print(f"Reading contents of '{filename}':\n")
            print("-" * 30)
            contents = file.read()
            print(contents)
            print("-" * 30)

    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        print("Creating the file first...")

        with open(filename, "w") as file:
            file.write("=== Student List ===\n")
            file.write("Alice Johnson - Grade A\n")
            file.write("Bob Smith - Grade B\n")

        print("File created! Run the script again to read it.")


def read_line_by_line():
    filename = "students.txt"

    print("\nReading line by line:")
    print("-" * 30)

    try:
        with open(filename, "r") as file:
            for line_number, line in enumerate(file, start=1):
                print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


read_file_contents()
read_line_by_line()
