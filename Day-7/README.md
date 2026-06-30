# Day 7 - Object-Oriented Programming (OOP) in Python

## 📚 Topics Covered Today

### 1. Object-Oriented Programming (OOP)
- What OOP is and why it's the foundation of most professional Python libraries (including ML/CV frameworks)
- Classes and Objects — blueprints vs. real instances
- Attributes (data) and Methods (behavior)
- Constructors using `__init__` to initialize object state
- Creating multiple independent objects from the same class
- The `self` keyword — how an object refers to itself

### 2. Inheritance & Encapsulation
- Why inheritance is used: avoiding code duplication, sharing common logic
- Parent (base) classes and Child (derived) classes
- Method overriding — child classes redefining parent behavior
- Using `super()` to call the parent class's methods/constructor
- Public vs Private attributes (`self.attr` vs `self.__attr`)
- Encapsulation — restricting direct access to internal data and exposing it safely through methods

---

## 📁 Folder Structure

```
Day-7/
│
├── OOP-Practice/
│   ├── 01_student_class.py         # Student class - attributes, methods, constructor
│   ├── 02_employee_class.py        # Employee class - business logic methods
│   ├── 03_car_class.py             # Car class - stateful object behavior
│   └── 04_multiple_objects.py      # Multiple independent objects + class attributes
│
├── Inheritance-Practice/
│   ├── 01_person_class.py                      # Base Person class
│   ├── 02_student_teacher_inheritance.py       # Student & Teacher inherit from Person
│   └── 03_encapsulation.py                     # Public vs private attributes
│
├── Library-Management-System/
│   ├── library_management.py       # Mini Project - Full OOP Library System
│   └── library_data.json           # Persistent JSON data file
│
└── README.md
```

---

## 🧠 What is Object-Oriented Programming?

OOP is a programming paradigm that organizes code around **objects** — self-contained units that bundle **data (attributes)** and **behavior (methods)** together. Instead of writing separate functions and variables scattered around, OOP lets us model real-world entities (like a `Student`, `Car`, or `Book`) as classes, then create multiple objects from them.

The four core pillars practiced today:
1. **Encapsulation** — bundling data and methods, restricting direct access to sensitive data
2. **Inheritance** — reusing code by letting one class inherit attributes/methods from another
3. **Abstraction** — hiding internal implementation details behind simple methods
4. **Polymorphism** — different classes (like `Book` and `DigitalBook`) responding differently to the same method call (`borrow()`, `return_book()`)

---

## 🏛️ Where Inheritance Was Used in the Project

In the **Library Management System**, inheritance was applied as follows:

- **`Book`** is the base class — it represents a standard physical book with attributes like `title`, `author`, `total_copies`, and `available_copies`, plus methods like `borrow()` and `return_book()`.
- **`DigitalBook`** inherits from `Book` using `class DigitalBook(Book):`. It reuses the constructor via `super().__init__(...)` but **overrides** the `borrow()` and `return_book()` methods, since digital books don't have a limited copy count — they can be "downloaded" infinitely instead of physically borrowed.

This demonstrates a real use case for inheritance: the `DigitalBook` shares 90% of its structure with `Book`, but customizes the parts that behave differently — avoiding duplicate code while still allowing specialized behavior (polymorphism).

Encapsulation was also reinforced separately in `03_encapsulation.py`, where a `BankAccount` class protects its `__balance` attribute using double-underscore name mangling, only allowing controlled access through `deposit()`, `withdraw()`, and `get_balance()` methods.

---

## 🚧 Challenges Faced

- **Choosing where to apply inheritance meaningfully**: Initially considered making `Library` inherit from something, but realized inheritance only makes sense for `Book` → `DigitalBook` since they share an "is-a" relationship. `Library` is better as a standalone class that *manages* `Book` objects (composition, not inheritance).
- **Keeping JSON serializable**: Python objects (like `Book` instances) can't be saved to JSON directly. Solved this by adding a `to_dict()` method on the `Book` class to convert objects into plain dictionaries before calling `json.dump()`.
- **Handling overridden methods safely**: When `DigitalBook.borrow()` overrides the parent's logic completely, I had to make sure overriding didn't break the polymorphic call from `Library.borrow_book()` — it works automatically because Python resolves the correct method based on the object's actual class.
- **Invalid user input**: Wrapped the menu loop in a `try/except` block and used dedicated input-validation helper functions (`input_positive_int`, `input_non_empty`) to gracefully handle bad input without crashing the program.

---

## ✅ What I Can Do Now

- Design programs using classes and objects instead of loose functions and variables
- Apply inheritance to reduce code duplication and model real-world relationships
- Use encapsulation to protect sensitive data with controlled access
- Override methods to customize behavior in child classes
- Build a structured, reusable, persistent console application using OOP + JSON
- Understand the programming style used in professional software development and AI/ML frameworks

---

## 🛠️ How to Run

### Practice Programs
```bash
cd OOP-Practice
python 01_student_class.py
python 02_employee_class.py
python 03_car_class.py
python 04_multiple_objects.py

cd ../Inheritance-Practice
python 01_person_class.py
python 02_student_teacher_inheritance.py
python 03_encapsulation.py
```

### Mini Project
```bash
cd Library-Management-System
python library_management.py
```

---

*Day 7 | MLB Python Bootcamp | Mian Azeem Naseer*
