# Problem 3: Grade Calculator based on marks

marks = float(input("Enter your marks (0 - 100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")
elif marks >= 90:
    grade = "A+"
    remarks = "Outstanding!"
elif marks >= 80:
    grade = "A"
    remarks = "Excellent!"
elif marks >= 70:
    grade = "B"
    remarks = "Very Good!"
elif marks >= 60:
    grade = "C"
    remarks = "Good!"
elif marks >= 50:
    grade = "D"
    remarks = "Average. Keep working harder."
else:
    grade = "F"
    remarks = "Failed. Don't give up, try again!"

print(f"\n--- Grade Report ---")
print(f"Marks  : {marks}")
print(f"Grade  : {grade}")
print(f"Remarks: {remarks}")
