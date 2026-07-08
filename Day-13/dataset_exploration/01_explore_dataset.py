# ============================================================
#       Step 1: Load & Explore – Iris Dataset
# ============================================================

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

# ── Load Dataset ─────────────────────────────────────────────
iris = load_iris()
df   = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

print("=" * 58)
print("          IRIS DATASET – EXPLORATION")
print("=" * 58)

# ── head() ───────────────────────────────────────────────────
print("\n📋 First 5 Rows (head):")
print(df.head().to_string())

# ── info() ───────────────────────────────────────────────────
print("\n📊 Dataset Info:")
print(f"  Shape        : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"  Features     : {list(iris.feature_names)}")
print(f"  Target       : 3 species (multiclass)")
print(f"  Missing vals : {df.isnull().sum().sum()}")

# ── describe() ───────────────────────────────────────────────
print("\n📐 Statistical Summary (describe):")
print(df.describe().round(2).to_string())

# ── Class Distribution ───────────────────────────────────────
print("\n🌸 Species Distribution:")
counts = df['species'].value_counts()
for species, count in counts.items():
    bar = "█" * int(count / 5)
    print(f"  {species:<15} : {count} samples  {bar}")

# ── Feature Correlation ──────────────────────────────────────
print("\n🔗 Feature Correlations (with petal length):")
corr = df[iris.feature_names].corr()['petal length (cm)'].drop('petal length (cm)')
for feat, val in corr.items():
    direction = "positive" if val > 0 else "negative"
    print(f"  {feat:<30} : {val:+.3f}  ({direction})")

print("\n✅ Key Observations:")
print("  - No missing values found.")
print("  - Petal features are highly correlated with each other.")
print("  - Setosa is clearly separable; Versicolor & Virginica overlap.")
