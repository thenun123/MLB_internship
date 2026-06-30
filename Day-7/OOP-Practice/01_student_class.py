# Practice: Student Class
# Demonstrates: classes, objects, attributes, methods, constructor, self

class Student:
    def __init__(self, name, age, roll_no, grade):
        # self refers to the current object being created
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.grade = grade

    def display_info(self):
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Grade   : {self.grade}")
        print("-" * 30)

    def update_grade(self, new_grade):
        old_grade = self.grade
        self.grade = new_grade
        print(f"{self.name}'s grade updated: {old_grade} -> {new_grade}")


# Creating multiple objects from the same class
student1 = Student("Alice Johnson", 20, "S001", "A")
student2 = Student("Bob Smith", 21, "S002", "B+")
student3 = Student("Charlie Brown", 19, "S003", "A+")

print("=== All Students ===")
for student in [student1, student2, student3]:
    student.display_info()

# Updating a single object doesn't affect the others
student2.update_grade("A-")
print("\nAfter update:")
student2.display_info()
