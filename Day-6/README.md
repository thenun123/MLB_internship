# Day 6 - File Handling & JSON in Python

## 📚 Topics Covered Today

### 1. File Handling in Python
- Opening and closing files using `open()` and the `with` statement
- Reading files using `read()`, `readline()`, and `readlines()`
- Writing to files using `write()` with mode `"w"`
- Appending to files without overwriting using mode `"a"`
- File modes: `r` (read), `w` (write), `a` (append)
- Best practice: always use `with` to auto-close files

### 2. JSON in Python
- JSON (JavaScript Object Notation) as a lightweight data format
- Reading JSON files using `json.load()`
- Writing Python dictionaries to JSON using `json.dump()`
- Converting Python objects to JSON strings using `json.dumps()`
- Loading JSON strings into Python objects using `json.loads()`
- Using `indent=4` for pretty-printed, readable JSON output

---

## 📁 Folder Structure

```
Day-6/
│
├── File-Handling-Practice/
│   ├── 01_create_and_write_file.py     # Create a file and write data
│   ├── 02_read_file_contents.py        # Read and display file contents
│   ├── 03_append_to_file.py            # Append new data to a file
│   └── 04_count_lines.py               # Count lines, words, and characters
│
├── JSON-Practice/
│   ├── 01_store_students_json.py       # Store student data in a JSON file
│   ├── 02_read_json_file.py            # Read and display JSON data
│   ├── 03_update_student.py            # Update a student's record in JSON
│   └── 04_add_student.py               # Add a new student to JSON file
│
├── Student-Record-Management-System/
│   ├── student_management.py           # Mini Project - Full CRUD system
│   └── students_data.json              # Persistent JSON data file
│
└── README.md
```

---

## 🔗 How File Handling and JSON Work Together

File handling gives us the ability to **read and write data to disk**, while JSON provides a **structured format** for organizing that data. Together, they enable *data persistence* — the ability for a program to remember information between runs.

For example, in the Student Record Management System:
1. When the program **starts**, it reads `students_data.json` using `json.load()` → data is loaded into a Python list.
2. The user can **add, update, search, or delete** records in memory.
3. After every change, the updated list is written back to `students_data.json` using `json.dump()` → changes are permanently saved.

This pattern (load → modify → save) is the foundation of how many real-world applications manage their data.

---

## 🚧 Challenges Faced

- **FileNotFoundError handling**: The first time a program runs, the JSON file doesn't exist yet. Solved this by checking `os.path.exists()` before reading and creating the file if needed.
- **Data corruption guard**: Added a `try/except json.JSONDecodeError` block so the program doesn't crash if the JSON file gets corrupted.
- **Auto ID generation**: Used `max()` with a lambda to find the last assigned ID number and increment it automatically for new students.
- **Partial updates**: When updating a record, pressing Enter should keep the existing value. Solved this by only applying changes if the input is non-empty.

---

## ✅ What I Can Do Now

- Read and write text files confidently using Python
- Store structured data in JSON format
- Build programs that **persist data between sessions**
- Implement full **CRUD** (Create, Read, Update, Delete) with file-based storage
- Handle exceptions gracefully to prevent crashes on bad input

---

## 🛠️ How to Run

### Practice Programs
```bash
cd File-Handling-Practice
python 01_create_and_write_file.py
python 02_read_file_contents.py
python 03_append_to_file.py
python 04_count_lines.py

cd ../JSON-Practice
python 01_store_students_json.py
python 02_read_json_file.py
python 03_update_student.py
python 04_add_student.py
```

### Mini Project
```bash
cd Student-Record-Management-System
python student_management.py
```

---

*Day 6 | MLB Python Bootcamp | Mian Azeem Naseer*
