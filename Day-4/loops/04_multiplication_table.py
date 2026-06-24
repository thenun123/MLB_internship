# Problem 4 (Loops): Print the multiplication table of a given number

num = int(input("Enter a number to print its multiplication table: "))

print(f"\n--- Multiplication Table of {num} ---")
print("-" * 30)

for i in range(1, 11):
    result = num * i
    print(f"  {num} x {i:2} = {result:4}")

print("-" * 30)
