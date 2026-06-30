# Practice: Encapsulation - Public vs Private Attributes
# Demonstrates: access control, name mangling, getter/setter methods, benefits of encapsulation


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner             # public attribute - accessible from anywhere
        self.__balance = balance       # private attribute (double underscore = name mangling)
        self._account_type = "Savings" # protected attribute (single underscore = convention only)

    # Getter method - controlled, read-only access to private data
    def get_balance(self):
        return self.__balance

    # Setter method - controlled way to modify private data, with validation
    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Error: Insufficient funds.")
            return
        self.__balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.__balance}")


if __name__ == "__main__":
    account = BankAccount("Alice Johnson", 1000)

    print("=== Public attribute access ===")
    print(f"Owner: {account.owner}")  # Works fine - public

    print("\n=== Controlled access via methods ===")
    print(f"Balance: ${account.get_balance()}")
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(99999)  # Should fail gracefully

    print("\n=== Why encapsulation matters ===")
    try:
        # Trying to directly access the private attribute fails
        print(account.__balance)
    except AttributeError as e:
        print(f"AttributeError caught: {e}")
        print("This is expected! Private attributes can't be accessed directly.")

    print("\nHowever, Python doesn't enforce TRUE privacy - it uses 'name mangling'.")
    print("The private attribute is actually stored as: _BankAccount__balance")
    print(f"Accessing it the 'hacky' way (NOT recommended): {account._BankAccount__balance}")

    print("\n=== Benefits of Encapsulation ===")
    print("1. Prevents accidental/direct modification of sensitive data")
    print("2. Allows validation logic before changing internal state")
    print("3. Keeps implementation details hidden (abstraction)")
    print("4. Makes code easier to maintain and refactor safely")
