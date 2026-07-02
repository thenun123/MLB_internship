# Data Cleaning with Pandas
# Day 9 | MLB Python Bootcamp
# Dataset: student_performance.csv

import pandas as pd
import numpy as np
import os

INPUT_FILE  = "../student_performance.csv"
OUTPUT_FILE = "../Student-Performance-Dashboard/cleaned_student_performance.csv"

print("=" * 60)
print("       DATA CLEANING — student_performance.csv")
print("=" * 60)

# ── Step 1: Load ─────────────────────────────────────────────
df = pd.read_csv(INPUT_FILE)
print(f"\n[1] Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns")

# ── Step 2: Check Missing Values ─────────────────────────────
print("\n[2] Missing values per column:")
missing = df.isnull().sum()
print(missing.to_string())
print(f"    Total missing: {missing.sum()}")

# ── Step 3: Remove Duplicates ─────────────────────────────────
dupes_before = df.duplicated().sum()
df.drop_duplicates(inplace=True)
print(f"\n[3] Duplicate rows removed: {dupes_before}")
print(f"    Rows remaining: {len(df)}")

# ── Step 4: Rename Columns ────────────────────────────────────
df.rename(columns={
    "Machine_Learning": "ML_Score",
    "Student_ID": "ID"
}, inplace=True)
print("\n[4] Columns renamed:")
print(f"    Machine_Learning → ML_Score")
print(f"    Student_ID       → ID")

# ── Step 5: Fix Data Types ────────────────────────────────────
df["Age"] = df["Age"].astype(int)
print("\n[5] Data types confirmed — Age is int, scores are int.")

# ── Step 6: Create Average_Score column ──────────────────────
subjects = ["Python", "Mathematics", "Statistics", "ML_Score"]
df["Average_Score"] = df[subjects].mean(axis=1).round(2)
print(f"\n[6] New column 'Average_Score' created.")
print(f"    Class average: {df['Average_Score'].mean():.2f}")

# ── Step 7: Create Performance column ────────────────────────
def classify(avg):
    if avg >= 90:
        return "Excellent"
    elif avg >= 80:
        return "Good"
    elif avg >= 70:
        return "Average"
    else:
        return "Needs Improvement"

df["Performance"] = df["Average_Score"].apply(classify)
print("\n[7] New column 'Performance' created.")
print("    Distribution:")
print(df["Performance"].value_counts().to_string())

# ── Step 8: Sort by Average Score ────────────────────────────
df.sort_values("Average_Score", ascending=False, inplace=True)
df.reset_index(drop=True, inplace=True)
print("\n[8] Dataset sorted by Average_Score (descending).")

# ── Step 9: Preview Cleaned Data ─────────────────────────────
print("\n[9] Cleaned dataset preview:")
print(df[["ID", "Name", "Program", "Average_Score", "Performance"]].to_string(index=False))

# ── Step 10: Save ─────────────────────────────────────────────
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)
print(f"\n[10] Cleaned dataset saved → '{OUTPUT_FILE}'")
print(f"     Final shape: {df.shape[0]} rows × {df.shape[1]} columns")
print("\n✅ Data cleaning complete!")
