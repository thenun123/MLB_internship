# Pandas Practice 1: Load Dataset and Basic Exploration
# Demonstrates: read_csv, head(), tail(), info(), shape, columns

import pandas as pd

print("=" * 55)
print("       PANDAS: LOADING & EXPLORING A DATASET")
print("=" * 55)

# Load the dataset
df = pd.read_csv("../Student-Performance-Analysis/student_performance.csv")

# ── Basic Info ──────────────────────────────────
print(f"\nDataset shape: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Columns      : {list(df.columns)}")

print("\n--- First 5 rows (head) ---")
print(df.head())

print("\n--- Last 5 rows (tail) ---")
print(df.tail())

print("\n--- Dataset Info (dtypes, non-null counts) ---")
df.info()

print("\n--- Data types per column ---")
print(df.dtypes)
