# ============================================================
#          BONUS CHALLENGE - Menu Driven Application
# ============================================================
# Features:
#   1. Check Prime Numbers
#   2. Generate Fibonacci Series
#   3. Check Palindromes
#   4. Generate Multiplication Tables
#   5. Exit
# ============================================================


def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def check_prime():
    print("\n--- 🔍 Prime Number Checker ---")
    try:
        num = int(input("Enter a positive integer: "))
        if is_prime(num):
            print(f"✅ {num} IS a Prime number.")
        else:
            print(f"❌ {num} is NOT a Prime number.")
            if num >= 2:
                factors = [i for i in range(2, num) if num % i == 0]
                print(f"   Factors: 1, {', '.join(map(str, factors))}, {num}")
    except ValueError:
        print("❌ Please enter a valid integer.")


def generate_fibonacci():
    print("\n--- 🌀 Fibonacci Series Generator ---")
    try:
        n = int(input("How many terms? "))
        if n <= 0:
            print("❌ Please enter a positive number.")
            return
        a, b = 0, 1
        series = []
        for _ in range(n):
            series.append(a)
            a, b = b, a + b
        print(f"\nFibonacci ({n} terms):")
        print(" -> ".join(map(str, series)))
    except ValueError:
        print("❌ Please enter a valid integer.")


def check_palindrome():
    print("\n--- 🔄 Palindrome Checker ---")
    try:
        num = int(input("Enter a positive integer: "))
        original = abs(num)
        temp = original
        reversed_num = 0
        while temp > 0:
            reversed_num = reversed_num * 10 + (temp % 10)
            temp //= 10
        if original == reversed_num:
            print(f"✅ {num} IS a Palindrome!")
        else:
            print(f"❌ {num} is NOT a Palindrome.")
            print(f"   Reversed: {reversed_num}")
    except ValueError:
        print("❌ Please enter a valid integer.")


def generate_multiplication_table():
    print("\n--- ✖️  Multiplication Table Generator ---")
    try:
        num = int(input("Enter a number: "))
        limit = int(input("Up to how many multiples? (default 10): ") or "10")
        print(f"\n  Multiplication Table of {num} (up to {limit})")
        print("  " + "-" * 25)
        for i in range(1, limit + 1):
            print(f"  {num} x {i:3} = {num * i:6}")
        print("  " + "-" * 25)
    except ValueError:
        print("❌ Please enter a valid integer.")


def display_menu():
    print("\n" + "=" * 45)
    print("      🧮  MATH TOOLKIT - MAIN MENU  🧮")
    print("=" * 45)
    print("  [1]  Check Prime Numbers")
    print("  [2]  Generate Fibonacci Series")
    print("  [3]  Check Palindromes")
    print("  [4]  Generate Multiplication Table")
    print("  [5]  Exit")
    print("=" * 45)


# ─────────────────────────────────────────────
#                  MAIN LOOP
# ─────────────────────────────────────────────

print("\nWelcome to the Math Toolkit! 🎉")

while True:
    display_menu()
    choice = input("\nEnter your choice (1-5): ").strip()

    if choice == "1":
        check_prime()
    elif choice == "2":
        generate_fibonacci()
    elif choice == "3":
        check_palindrome()
    elif choice == "4":
        generate_multiplication_table()
    elif choice == "5":
        print("\n👋 Thanks for using Math Toolkit. Goodbye!\n")
        break
    else:
        print("❌ Invalid choice. Please enter a number between 1 and 5.")

    input("\n⏎  Press Enter to return to the menu...")
