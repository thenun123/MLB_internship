# Logic Building Problem 2: Check whether a number is a palindrome
# A palindrome number reads the same forward and backward (e.g., 121, 1331)

num = int(input("Enter a positive integer: "))
original = num
reversed_num = 0
temp = num

while temp > 0:
    last_digit = temp % 10
    reversed_num = reversed_num * 10 + last_digit
    temp //= 10

print(f"\nOriginal number : {original}")
print(f"Reversed number : {reversed_num}")

if original == reversed_num:
    print(f"✅ {original} IS a Palindrome!")
else:
    print(f"❌ {original} is NOT a Palindrome.")
