# Practice: Car Class
# Demonstrates: multiple attributes, methods with state changes

class Car:
    def __init__(self, brand, model, year, fuel_capacity):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.current_fuel = 0
        self.mileage = 0
        self.is_running = False

    def display_info(self):
        status = "Running" if self.is_running else "Off"
        print(f"Car      : {self.year} {self.brand} {self.model}")
        print(f"Fuel     : {self.current_fuel}/{self.fuel_capacity} L")
        print(f"Mileage  : {self.mileage} km")
        print(f"Status   : {status}")
        print("-" * 30)

    def start_engine(self):
        if self.current_fuel <= 0:
            print(f"Cannot start {self.brand} {self.model}: No fuel!")
            return
        self.is_running = True
        print(f"{self.brand} {self.model} engine started.")

    def stop_engine(self):
        self.is_running = False
        print(f"{self.brand} {self.model} engine stopped.")

    def refuel(self, liters):
        self.current_fuel = min(self.current_fuel + liters, self.fuel_capacity)
        print(f"Refueled {self.brand} {self.model}. Current fuel: {self.current_fuel} L")

    def drive(self, km):
        if not self.is_running:
            print(f"Cannot drive: {self.brand} {self.model} engine is off.")
            return
        fuel_needed = km / 10  # assume 10 km per liter
        if fuel_needed > self.current_fuel:
            print(f"Not enough fuel to drive {km} km.")
            return
        self.current_fuel -= fuel_needed
        self.mileage += km
        print(f"Drove {km} km. Remaining fuel: {self.current_fuel:.1f} L")


# Creating multiple Car objects
car1 = Car("Toyota", "Corolla", 2022, 50)
car2 = Car("Honda", "Civic", 2023, 47)

print("=== Initial State ===")
car1.display_info()
car2.display_info()

car1.refuel(30)
car1.start_engine()
car1.drive(100)

car2.start_engine()  # should fail - no fuel

print("\n=== After Operations ===")
car1.display_info()
car2.display_info()
