# Logic Building Problem 4: Check whether a number is prime
# A prime number is only divisible by 1 and itself

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Check odd divisors up to square root of n (efficient approach)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


num = int(input("Enter a positive integer: "))

if is_prime(num):
    print(f"\n✅ {num} IS a Prime number.")
else:
    print(f"\n❌ {num} is NOT a Prime number.")
    if num >= 2:
        # Show factors
        factors = [i for i in range(2, num) if num % i == 0]
        print(f"   Factors of {num}: 1, {', '.join(map(str, factors))}, {num}")
