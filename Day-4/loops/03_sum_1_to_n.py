# Problem 3 (Loops): Calculate the sum of numbers from 1 to N

n = int(input("Enter a positive integer N: "))

if n < 1:
    print("Please enter a positive integer greater than 0.")
else:
    total = 0
    for i in range(1, n + 1):
        total += i

    print(f"\nSum of numbers from 1 to {n} = {total}")
    # Verify using formula
    formula_result = n * (n + 1) // 2
    print(f"Verified using formula n*(n+1)/2 = {formula_result}")
