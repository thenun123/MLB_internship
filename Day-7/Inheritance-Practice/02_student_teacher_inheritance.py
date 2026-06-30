# Practice: Inheritance - Student and Teacher classes inheriting from Person
# Demonstrates: parent/child classes, method overriding, super(), accessing inherited members


class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"Name  : {self.name}")
        print(f"Age   : {self.age}")
        print(f"Email : {self.email}")

    def greet(self):
        print(f"Hello, my name is {self.name}.")


class Student(Person):
    def __init__(self, name, age, email, roll_no, grade):
        # super() calls the parent class's constructor to reuse its setup logic
        super().__init__(name, age, email)
        self.roll_no = roll_no
        self.grade = grade

    def display_info(self):
        # Method overriding: extending the parent's behavior with super()
        super().display_info()
        print(f"Roll No: {self.roll_no}")
        print(f"Grade  : {self.grade}")

    def greet(self):
        # Full override: completely different behavior than parent
        print(f"Hi! I'm {self.name}, a student with roll number {self.roll_no}.")

    def submit_assignment(self, subject):
        print(f"{self.name} submitted the {subject} assignment.")


class Teacher(Person):
    def __init__(self, name, age, email, subject, employee_id):
        super().__init__(name, age, email)
        self.subject = subject
        self.employee_id = employee_id

    def display_info(self):
        super().display_info()
        print(f"Subject     : {self.subject}")
        print(f"Employee ID : {self.employee_id}")

    def greet(self):
        print(f"Good day, I'm {self.name}, your {self.subject} teacher.")

    def grade_assignment(self, student_name):
        print(f"{self.name} graded {student_name}'s assignment.")


if __name__ == "__main__":
    print("=== Student Object ===")
    student = Student("Alice Johnson", 20, "alice@example.com", "S001", "A")
    student.display_info()
    student.greet()
    student.submit_assignment("Python Programming")

    print("\n=== Teacher Object ===")
    teacher = Teacher("Mr. Khan", 35, "khan@example.com", "Computer Science", "T101")
    teacher.display_info()
    teacher.greet()
    teacher.grade_assignment("Alice Johnson")

    print("\n=== Demonstrating Inherited Attributes ===")
    # Both Student and Teacher inherit 'name', 'age', 'email' from Person
    print(f"Student name (inherited attribute): {student.name}")
    print(f"Teacher email (inherited attribute): {teacher.email}")

    # isinstance() confirms the inheritance relationship
    print(f"\nIs student an instance of Person? {isinstance(student, Person)}")
    print(f"Is teacher an instance of Person? {isinstance(teacher, Person)}")
