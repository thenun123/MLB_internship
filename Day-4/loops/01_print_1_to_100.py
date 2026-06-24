# Problem 1 (Loops): Print numbers from 1 to 100

print("Numbers from 1 to 100:")
print("-" * 50)

for i in range(1, 101):
    # Print 10 numbers per row for cleaner output
    print(f"{i:4}", end="")
    if i % 10 == 0:
        print()  # New line after every 10 numbers
