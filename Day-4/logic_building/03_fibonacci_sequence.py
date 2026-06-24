# Logic Building Problem 3: Generate the Fibonacci sequence
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Each number = sum of the two numbers before it

n = int(input("How many terms of the Fibonacci sequence do you want? "))

if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("\nFibonacci Sequence:")
    print("0")
else:
    print(f"\nFibonacci Sequence (first {n} terms):")
    print("-" * 40)

    a, b = 0, 1
    sequence = []

    for i in range(n):
        sequence.append(a)
        a, b = b, a + b

    print(" -> ".join(str(x) for x in sequence))
    print("-" * 40)
    print(f"The {n}th term is: {sequence[-1]}")
