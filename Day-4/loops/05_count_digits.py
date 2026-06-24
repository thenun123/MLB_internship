# Problem 5 (Loops): Count the number of digits in a number

num = int(input("Enter an integer: "))
original = num
count = 0

# Handle negative numbers
num = abs(num)

# Special case: 0 has 1 digit
if num == 0:
    count = 1
else:
    while num > 0:
        num //= 10
        count += 1

print(f"\nThe number {original} has {count} digit(s).")
