# Logic Building Problem 1: Reverse a number

num = int(input("Enter an integer: "))
original = num
reversed_num = 0

# Handle negative numbers
is_negative = num < 0
num = abs(num)

while num > 0:
    last_digit = num % 10
    reversed_num = reversed_num * 10 + last_digit
    num //= 10

if is_negative:
    reversed_num = -reversed_num

print(f"\nOriginal number : {original}")
print(f"Reversed number : {reversed_num}")
