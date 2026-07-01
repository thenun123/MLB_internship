# NumPy Practice 3: Mathematical Functions
# Demonstrates: max, min, mean, sum, std, var, and axis-based operations

import numpy as np

print("=" * 50)
print("     NUMPY MATHEMATICAL FUNCTIONS")
print("=" * 50)

scores = np.array([85, 72, 90, 65, 78, 95, 55, 88, 73, 81])
print(f"\nStudent scores: {scores}")

# ── Aggregate Functions ─────────────────────────
print("\n--- Aggregate Statistics ---")
print(f"Maximum    : {np.max(scores)}")
print(f"Minimum    : {np.min(scores)}")
print(f"Sum        : {np.sum(scores)}")
print(f"Mean       : {np.mean(scores):.2f}")
print(f"Median     : {np.median(scores)}")
print(f"Std Dev    : {np.std(scores):.2f}")
print(f"Variance   : {np.var(scores):.2f}")

# ── Index of Max/Min ────────────────────────────
print(f"\nIndex of max: {np.argmax(scores)}  (score: {scores[np.argmax(scores)]})")
print(f"Index of min: {np.argmin(scores)}  (score: {scores[np.argmin(scores)]})")

# ── Sorting ─────────────────────────────────────
print(f"\nSorted ascending : {np.sort(scores)}")
print(f"Sorted descending: {np.sort(scores)[::-1]}")

# ── 2D Matrix Axis-based Operations ─────────────
print("\n--- 2D Matrix: Axis-based Operations ---")
marks = np.array([
    [85, 90, 78],   # Student 1: Python, Math, Stats
    [72, 65, 80],   # Student 2
    [90, 88, 92],   # Student 3
    [60, 70, 65],   # Student 4
])
print(f"Marks matrix (4 students x 3 subjects):\n{marks}")
print(f"\nSum per student  (axis=1): {np.sum(marks, axis=1)}")
print(f"Mean per student (axis=1): {np.mean(marks, axis=1).round(2)}")
print(f"Mean per subject (axis=0): {np.mean(marks, axis=0).round(2)}")
print(f"Top score per subject    : {np.max(marks, axis=0)}")

# ── Math Functions ──────────────────────────────
print("\n--- Universal Math Functions ---")
arr = np.array([1, 4, 9, 16, 25])
print(f"Array     : {arr}")
print(f"sqrt      : {np.sqrt(arr)}")
print(f"log       : {np.log(arr).round(3)}")
print(f"exp       : {np.exp([1, 2, 3]).round(3)}")
print(f"abs(-arr) : {np.abs(-arr)}")
