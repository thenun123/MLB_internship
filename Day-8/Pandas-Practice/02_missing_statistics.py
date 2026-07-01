# Pandas Practice 2: Missing Values & Summary Statistics
# Demonstrates: isnull(), describe(), value_counts(), unique()

import pandas as pd

df = pd.read_csv("../Student-Performance-Analysis/student_performance.csv")

print("=" * 55)
print("     PANDAS: MISSING VALUES & STATISTICS")
print("=" * 55)

# ── Missing Values ──────────────────────────────
print("\n--- Missing Values per Column ---")
missing = df.isnull().sum()
print(missing)
print(f"\nTotal missing values: {missing.sum()}")
print(f"Dataset is complete : {missing.sum() == 0}")

# ── Summary Statistics ──────────────────────────
print("\n--- Summary Statistics (describe) ---")
print(df.describe().round(2))

# ── Categorical Column Insights ─────────────────
print("\n--- Program Distribution ---")
print(df["Program"].value_counts())

print("\n--- Unique Programs ---")
print(df["Program"].unique())

print("\n--- Age Distribution ---")
print(df["Age"].value_counts().sort_index())

# ── Per-column mean ──────────────────────────────
print("\n--- Average Score per Subject ---")
subjects = ["Python", "Mathematics", "Statistics", "Machine_Learning"]
for subj in subjects:
    print(f"  {subj:<20}: {df[subj].mean():.2f}")

print(f"  {'Attendance':<20}: {df['Attendance'].mean():.2f}")
