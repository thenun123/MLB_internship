# NumPy Practice 4: Reshaping and Slicing Arrays
# Demonstrates: reshape(), flatten(), indexing, slicing, fancy indexing

import numpy as np

print("=" * 50)
print("     NUMPY RESHAPING & SLICING")
print("=" * 50)

# ── Reshaping ────────────────────────────────────
print("\n--- Reshaping ---")
arr = np.arange(1, 13)       # [1, 2, 3, ... 12]
print(f"Original (1D): {arr}  shape={arr.shape}")

reshaped_3x4 = arr.reshape(3, 4)
print(f"\nReshaped to (3, 4):\n{reshaped_3x4}")

reshaped_2x6 = arr.reshape(2, 6)
print(f"\nReshaped to (2, 6):\n{reshaped_2x6}")

reshaped_3d = arr.reshape(2, 2, 3)
print(f"\nReshaped to (2, 2, 3) — 3D:\n{reshaped_3d}")

flat = reshaped_3x4.flatten()
print(f"\nFlattened back to 1D: {flat}")

# ── 1D Slicing ────────────────────────────────────
print("\n--- 1D Array Slicing ---")
scores = np.array([55, 65, 72, 78, 81, 85, 88, 90, 92, 95])
print(f"scores = {scores}")
print(f"scores[2]      = {scores[2]}         (index 2)")
print(f"scores[-1]     = {scores[-1]}         (last element)")
print(f"scores[2:6]    = {scores[2:6]}    (index 2 to 5)")
print(f"scores[:4]     = {scores[:4]}  (first 4)")
print(f"scores[6:]     = {scores[6:]}  (from index 6 to end)")
print(f"scores[::2]    = {scores[::2]}  (every 2nd element)")
print(f"scores[::-1]   = {scores[::-1]}  (reversed)")

# ── 2D Array Indexing & Slicing ───────────────────
print("\n--- 2D Array Indexing & Slicing ---")
matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
print(f"Matrix:\n{matrix}")
print(f"\nmatrix[1, 2]     = {matrix[1, 2]}   (row 1, col 2)")
print(f"matrix[0]        = {matrix[0]}   (entire row 0)")
print(f"matrix[:, 1]     = {matrix[:, 1]}   (entire column 1)")
print(f"matrix[0:2, 1:3] =\n{matrix[0:2, 1:3]}  (sub-matrix rows 0-1, cols 1-2)")

# ── Fancy Indexing ───────────────────────────────
print("\n--- Fancy Indexing (Boolean mask) ---")
data = np.array([45, 72, 88, 33, 91, 60, 55, 79])
print(f"data                   = {data}")
passing = data[data >= 60]
print(f"Passing scores (≥60)   = {passing}")
top = data[data >= 80]
print(f"Top scores    (≥80)    = {top}")
