# Problem 5: Check whether a year is a leap year
# Logic: Divisible by 4 AND (not divisible by 100 OR divisible by 400)

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"\n{year} is a Leap Year. 🗓️")
else:
    print(f"\n{year} is NOT a Leap Year.")
