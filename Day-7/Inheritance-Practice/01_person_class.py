# Practice: Person Class (Base/Parent Class)
# This will be used as a parent for Student and Teacher classes

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


if __name__ == "__main__":
    p = Person("John Doe", 30, "john@example.com")
    p.display_info()
    p.greet()
