# NumPy Practice 1: Creating 1D and 2D Arrays
# Demonstrates: np.array(), np.zeros(), np.ones(), np.arange(), np.linspace()

import numpy as np

print("=" * 50)
print("       NUMPY ARRAY CREATION")
print("=" * 50)

# ── 1D Arrays ──────────────────────────────────
print("\n--- 1D Arrays ---")

arr1 = np.array([10, 20, 30, 40, 50])
print(f"From list          : {arr1}")
print(f"Shape              : {arr1.shape}")
print(f"Data type          : {arr1.dtype}")

zeros = np.zeros(5)
print(f"np.zeros(5)        : {zeros}")

ones = np.ones(5, dtype=int)
print(f"np.ones(5, int)    : {ones}")

arange = np.arange(1, 11, 2)   # start, stop, step
print(f"np.arange(1,11,2)  : {arange}")

linspace = np.linspace(0, 1, 5)  # 5 evenly spaced values from 0 to 1
print(f"np.linspace(0,1,5) : {linspace}")

# ── 2D Arrays ──────────────────────────────────
print("\n--- 2D Arrays (Matrices) ---")

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"3x3 matrix:\n{matrix}")
print(f"Shape  : {matrix.shape}")   # (rows, cols)
print(f"Dimensions: {matrix.ndim}")

zeros_2d = np.zeros((3, 4))
print(f"\nnp.zeros((3,4)):\n{zeros_2d}")

identity = np.eye(3)              # identity matrix
print(f"\nnp.eye(3) (identity):\n{identity}")

random_arr = np.random.randint(1, 100, size=(3, 3))
print(f"\nRandom 3x3 (integers 1-99):\n{random_arr}")
