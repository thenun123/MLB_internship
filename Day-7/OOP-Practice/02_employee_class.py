# Practice: Employee Class
# Demonstrates: attributes, methods, constructor, business logic inside a class

class Employee:
    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def display_info(self):
        print(f"ID         : {self.employee_id}")
        print(f"Name       : {self.name}")
        print(f"Department : {self.department}")
        print(f"Salary     : ${self.salary:,.2f}")
        print("-" * 30)

    def give_raise(self, percent):
        increase = self.salary * (percent / 100)
        self.salary += increase
        print(f"{self.name} received a {percent}% raise (+${increase:,.2f}). "
              f"New salary: ${self.salary:,.2f}")

    def change_department(self, new_department):
        print(f"{self.name} moved from {self.department} to {new_department}")
        self.department = new_department


# Creating multiple Employee objects
emp1 = Employee("Fatima Khan", "E101", "Engineering", 80000)
emp2 = Employee("George Miller", "E102", "Marketing", 65000)
emp3 = Employee("Hannah Lee", "E103", "Engineering", 90000)

print("=== All Employees ===")
for emp in [emp1, emp2, emp3]:
    emp.display_info()

emp1.give_raise(10)
emp2.change_department("Sales")

print("\nUpdated records:")
emp1.display_info()
emp2.display_info()
