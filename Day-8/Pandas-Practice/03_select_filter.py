# Pandas Practice 3: Selecting, Filtering & Sorting Data
# Demonstrates: loc, iloc, column selection, boolean filtering, sort_values

import pandas as pd

df = pd.read_csv("../Student-Performance-Analysis/student_performance.csv")

print("=" * 55)
print("     PANDAS: SELECTING & FILTERING DATA")
print("=" * 55)

# ── Selecting Columns ────────────────────────────
print("\n--- Single Column ---")
print(df["Name"].head())

print("\n--- Multiple Columns ---")
print(df[["Name", "Program", "Python"]].head())

# ── loc: label-based selection ───────────────────
print("\n--- loc: rows 0-3, specific columns ---")
print(df.loc[0:3, ["Name", "Python", "Mathematics"]])

# ── iloc: position-based selection ──────────────
print("\n--- iloc: first 3 rows, first 4 columns ---")
print(df.iloc[0:3, 0:4])

# ── Filtering ────────────────────────────────────
print("\n--- Students in AI program ---")
ai_students = df[df["Program"] == "AI"]
print(ai_students[["Name", "Program", "Python", "Machine_Learning"]])

print("\n--- Students scoring above 85 in Python ---")
high_python = df[df["Python"] > 85]
print(high_python[["Name", "Python"]])

print("\n--- Students in SE with Attendance >= 95 ---")
se_high_attend = df[(df["Program"] == "SE") & (df["Attendance"] >= 95)]
print(se_high_attend[["Name", "Program", "Attendance"]])

print("\n--- Students scoring below 65 in any subject ---")
subjects = ["Python", "Mathematics", "Statistics", "Machine_Learning"]
low_scorers = df[(df[subjects] < 65).any(axis=1)]
print(low_scorers[["Name"] + subjects])

# ── Sorting ──────────────────────────────────────
print("\n--- Top 5 by Python score ---")
print(df.sort_values("Python", ascending=False)[["Name", "Python"]].head())

print("\n--- Bottom 5 by Attendance ---")
print(df.sort_values("Attendance")[["Name", "Attendance"]].head())
