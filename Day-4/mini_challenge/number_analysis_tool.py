# ============================================================
#           NUMBER ANALYSIS TOOL - Mini Challenge
# ============================================================
# This tool accepts a number and performs full analysis:
#   - Even or Odd
#   - Prime Check
#   - Digit Count
#   - Number Reversal
#   - Palindrome Check
# ============================================================


def is_even(n):
    return n % 2 == 0


def is_prime(n):
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


def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


def reverse_number(n):
    is_negative = n < 0
    n = abs(n)
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + (n % 10)
        n //= 10
    return -reversed_num if is_negative else reversed_num


def is_palindrome(n):
    return abs(n) == reverse_number(n)


# ─────────────────────────────────────────────
#                  MAIN PROGRAM
# ─────────────────────────────────────────────

print("=" * 50)
print("       🔢  NUMBER ANALYSIS TOOL  🔢")
print("=" * 50)

try:
    num = int(input("\nEnter an integer to analyze: "))
except ValueError:
    print("❌ Invalid input! Please enter a valid integer.")
    exit()

print("\n" + "=" * 50)
print(f"  Analysis Report for: {num}")
print("=" * 50)

# 1. Even or Odd
parity = "Even ✅" if is_even(num) else "Odd ✅"
print(f"\n  ▸ Even / Odd       : {parity}")

# 2. Prime Check
prime_status = "Yes ✅ (it's a prime!)" if is_prime(num) else "No ❌"
print(f"  ▸ Prime Number     : {prime_status}")

# 3. Digit Count
digits = count_digits(num)
print(f"  ▸ Number of Digits : {digits}")

# 4. Reversed Number
rev = reverse_number(num)
print(f"  ▸ Reversed Number  : {rev}")

# 5. Palindrome Check
palindrome_status = "Yes ✅ (reads same both ways!)" if is_palindrome(num) else "No ❌"
print(f"  ▸ Palindrome       : {palindrome_status}")

print("\n" + "=" * 50)
print("         ✅ Analysis Complete!")
print("=" * 50)
