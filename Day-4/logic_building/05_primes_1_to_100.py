# Logic Building Problem 5: Find all prime numbers between 1 and 100
# Using the Sieve of Eratosthenes for efficiency

def sieve_of_eratosthenes(limit):
    """Find all primes up to limit using the Sieve of Eratosthenes."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    p = 2
    while p * p <= limit:
        if is_prime[p]:
            # Mark all multiples of p as not prime
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
        p += 1

    return [num for num in range(2, limit + 1) if is_prime[num]]


primes = sieve_of_eratosthenes(100)

print("All Prime Numbers between 1 and 100:")
print("=" * 50)

for i, prime in enumerate(primes, 1):
    print(f"{prime:4}", end="")
    if i % 10 == 0:
        print()

print()
print("=" * 50)
print(f"Total prime numbers between 1 and 100: {len(primes)}")
