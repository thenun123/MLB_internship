# ============================================================
#         Model Evaluation – Accuracy, Precision, Recall,
#                     F1-Score & Confusion Matrix
# ============================================================

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)
import numpy as np

# ── 1. Load Dataset ──────────────────────────────────────────
data = load_breast_cancer()
X, y = data.data, data.target

print("=" * 55)
print("       BREAST CANCER DATASET – MODEL EVALUATION")
print("=" * 55)
print(f"  Total Samples  : {X.shape[0]}")
print(f"  Features       : {X.shape[1]}")
print(f"  Classes        : {list(data.target_names)}")
print("=" * 55)

# ── 2. Train/Test Split ──────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\n  Training samples : {X_train.shape[0]}")
print(f"  Testing samples  : {X_test.shape[0]}")

# ── 3. Train Logistic Regression ─────────────────────────────
model = LogisticRegression(max_iter=10000, random_state=42)
model.fit(X_train, y_train)

# ── 4. Predictions ───────────────────────────────────────────
y_pred = model.predict(X_test)

# ── 5. Evaluation Metrics ────────────────────────────────────
accuracy  = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall    = recall_score(y_test, y_pred)
f1        = f1_score(y_test, y_pred)
cm        = confusion_matrix(y_test, y_pred)

print("\n" + "=" * 55)
print("            EVALUATION METRICS")
print("=" * 55)
print(f"  Accuracy  : {accuracy  * 100:.2f}%")
print(f"  Precision : {precision * 100:.2f}%")
print(f"  Recall    : {recall    * 100:.2f}%")
print(f"  F1-Score  : {f1        * 100:.2f}%")

print("\n--- Confusion Matrix ---")
print(f"  TN={cm[0][0]}  FP={cm[0][1]}")
print(f"  FN={cm[1][0]}  TP={cm[1][1]}")

print("\n--- Full Classification Report ---")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# ── 6. Overfitting Check ─────────────────────────────────────
train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc  = accuracy_score(y_test,  y_pred)
gap       = train_acc - test_acc

print("=" * 55)
print("  OVERFITTING / UNDERFITTING CHECK")
print("=" * 55)
print(f"  Training Accuracy : {train_acc * 100:.2f}%")
print(f"  Testing  Accuracy : {test_acc  * 100:.2f}%")
print(f"  Gap               : {gap       * 100:.2f}%")

if gap > 0.10:
    print("  ⚠️  Model might be OVERFITTING.")
elif train_acc < 0.75:
    print("  ⚠️  Model might be UNDERFITTING.")
else:
    print("  ✅  Model is well-balanced.")
print("=" * 55)
