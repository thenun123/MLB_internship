# Problem 4: Find the largest among three numbers

a = float(input("Enter first number : "))
b = float(input("Enter second number: "))
c = float(input("Enter third number : "))

if a >= b and a >= c:
    print(f"\nThe largest number is: {a}")
elif b >= a and b >= c:
    print(f"\nThe largest number is: {b}")
else:
    print(f"\nThe largest number is: {c}")
