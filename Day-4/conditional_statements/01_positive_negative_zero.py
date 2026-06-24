# Problem 1: Check whether a number is positive, negative, or zero

num = float(input("Enter a number: "))

if num > 0:
    print(f"{num} is a Positive number.")
elif num < 0:
    print(f"{num} is a Negative number.")
else:
    print("The number is Zero.")
