# ============================================================
#   Classification with Logistic Regression – Iris Dataset
#   Topics: What is Classification, Logistic Regression,
#           Decision Boundaries, Evaluation
# ============================================================

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# ── What is Classification? ──────────────────────────────────
# Classification = predicting which CATEGORY/CLASS an input belongs to.
# Output is a discrete label (e.g., spam/not spam, cat/dog, flower species).
# Regression predicts a continuous value (e.g., price, temperature).

# ── 1. Load Iris Dataset ─────────────────────────────────────
iris = load_iris()
X, y = iris.data, iris.target

print("=" * 55)
print("      IRIS DATASET – LOGISTIC REGRESSION")
print("=" * 55)
print(f"  Samples  : {X.shape[0]}")
print(f"  Features : {X.shape[1]} → {list(iris.feature_names)}")
print(f"  Classes  : {list(iris.target_names)}")

# ── 2. Explore the Data ──────────────────────────────────────
print("\n--- Class Distribution ---")
for i, name in enumerate(iris.target_names):
    count = np.sum(y == i)
    print(f"  {name:15} : {count} samples")

# ── 3. Split ─────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ── 4. Train ─────────────────────────────────────────────────
model = LogisticRegression(max_iter=200, random_state=42)
model.fit(X_train, y_train)

# ── 5. Predict & Evaluate ────────────────────────────────────
y_pred = model.predict(X_test)
acc    = accuracy_score(y_test, y_pred)

print(f"\n  Test Accuracy : {acc * 100:.2f}%")
print("\n--- Classification Report ---")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# ── 6. Sample Predictions ────────────────────────────────────
print("--- Sample Predictions (first 10) ---")
print(f"  {'Actual':<20} {'Predicted':<20} {'Match'}")
print("  " + "-" * 45)
for actual, predicted in zip(y_test[:10], y_pred[:10]):
    match = "✅" if actual == predicted else "❌"
    print(f"  {iris.target_names[actual]:<20} {iris.target_names[predicted]:<20} {match}")
