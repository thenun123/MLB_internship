# NumPy Practice 2: Arithmetic Operations on Arrays
# Demonstrates: element-wise ops, broadcasting, scalar ops

import numpy as np

print("=" * 50)
print("       NUMPY ARRAY OPERATIONS")
print("=" * 50)

a = np.array([10, 20, 30, 40, 50])
b = np.array([1, 2, 3, 4, 5])

print(f"\na = {a}")
print(f"b = {b}")

# ── Element-wise Operations ─────────────────────
print("\n--- Element-wise Arithmetic ---")
print(f"a + b  = {a + b}")
print(f"a - b  = {a - b}")
print(f"a * b  = {a * b}")
print(f"a / b  = {a / b}")
print(f"a // b = {a // b}   (floor division)")
print(f"a ** 2 = {a ** 2}   (power)")
print(f"a % 3  = {a % 3}    (modulo)")

# ── Scalar Operations (Broadcasting) ───────────
print("\n--- Scalar Broadcasting ---")
print(f"a + 100  = {a + 100}")
print(f"a * 0.5  = {a * 0.5}")

# ── 2D Matrix Operations ────────────────────────
print("\n--- 2D Matrix Operations ---")
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print(f"m1:\n{m1}")
print(f"m2:\n{m2}")
print(f"m1 + m2 (element-wise):\n{m1 + m2}")
print(f"m1 * m2 (element-wise):\n{m1 * m2}")
print(f"m1 @ m2 (matrix multiplication):\n{m1 @ m2}")
print(f"m1.T    (transpose):\n{m1.T}")

# ── Comparison Operations ───────────────────────
print("\n--- Comparison Operations ---")
print(f"a > 25     : {a > 25}")
print(f"a == 30    : {a == 30}")
print(f"Values > 25: {a[a > 25]}")   # Boolean indexing
