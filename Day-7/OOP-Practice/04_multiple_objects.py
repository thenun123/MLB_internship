# Practice: Creating Multiple Objects from the Same Class
# Demonstrates: object independence, class vs instance behavior

class BankAccount:
    bank_name = "Python National Bank"  # class attribute (shared by all objects)
    total_accounts = 0  # tracks how many accounts have been created

    def __init__(self, owner, balance=0):
        self.owner = owner          # instance attribute (unique per object)
        self.balance = balance      # instance attribute
        BankAccount.total_accounts += 1
        self.account_number = f"ACC{BankAccount.total_accounts:04d}"

    def deposit(self, amount):
        self.balance += amount
        print(f"[{self.account_number}] {self.owner} deposited ${amount}. "
              f"New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"[{self.account_number}] Insufficient funds for {self.owner}.")
            return
        self.balance -= amount
        print(f"[{self.account_number}] {self.owner} withdrew ${amount}. "
              f"New balance: ${self.balance}")

    def display(self):
        print(f"Account  : {self.account_number}")
        print(f"Bank     : {self.bank_name}")
        print(f"Owner    : {self.owner}")
        print(f"Balance  : ${self.balance}")
        print("-" * 30)


# Creating multiple independent objects
acc1 = BankAccount("Alice Johnson", 1000)
acc2 = BankAccount("Bob Smith", 500)
acc3 = BankAccount("Charlie Brown")  # uses default balance

print("=== All Accounts ===")
for acc in [acc1, acc2, acc3]:
    acc.display()

# Each object maintains its own state
acc1.deposit(200)
acc2.withdraw(100)
acc3.deposit(50)

print(f"\nTotal accounts created (class-level data): {BankAccount.total_accounts}")
print(f"Shared bank name (class attribute): {BankAccount.bank_name}")

print("\n=== Final Balances ===")
for acc in [acc1, acc2, acc3]:
    acc.display()
