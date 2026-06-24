# Problem 2 (Loops): Print all even numbers from 1 to 100

print("Even numbers from 1 to 100:")
print("-" * 50)

for i in range(2, 101, 2):
    print(f"{i:4}", end="")
    if i % 20 == 0:
        print()  # New line after every 10 even numbers

print()
print(f"\nTotal even numbers between 1 and 100: {len(range(2, 101, 2))}")
