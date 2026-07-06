# ============================================================
#         🌸  IRIS FLOWER CLASSIFICATION SYSTEM
#              Mini Project – Day 11
# ============================================================
# This system classifies Iris flowers into 3 species:
#   - Iris Setosa
#   - Iris Versicolor
#   - Iris Virginica
# Based on 4 features:
#   - Sepal Length, Sepal Width, Petal Length, Petal Width
# ============================================================

import numpy as np
import matplotlib
matplotlib.use('Agg')  # non-interactive backend for saving
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)

# ── STEP 1: Load & Explore ───────────────────────────────────
print("=" * 60)
print("       🌸  IRIS FLOWER CLASSIFICATION SYSTEM  🌸")
print("=" * 60)

iris    = load_iris()
X, y    = iris.data, iris.target
classes = iris.target_names
features = iris.feature_names

print(f"\n📊 Dataset Overview")
print(f"  Total Samples  : {X.shape[0]}")
print(f"  Features       : {X.shape[1]}")
print(f"  Classes        : {list(classes)}")

print(f"\n📐 Feature Statistics")
print(f"  {'Feature':<30} {'Min':>6} {'Max':>6} {'Mean':>7}")
print("  " + "-" * 52)
for i, feat in enumerate(features):
    print(f"  {feat:<30} {X[:,i].min():>6.2f} {X[:,i].max():>6.2f} {X[:,i].mean():>7.2f}")

print(f"\n📦 Class Distribution")
for i, name in enumerate(classes):
    print(f"  {name:<20} : {np.sum(y == i)} samples")

# ── STEP 2: Train/Test Split ─────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"\n✂️  Data Split: {X_train.shape[0]} train / {X_test.shape[0]} test")

# ── STEP 3: Train Models ─────────────────────────────────────
lr_model = LogisticRegression(max_iter=200, random_state=42)
dt_model = DecisionTreeClassifier(max_depth=4, random_state=42)

lr_model.fit(X_train, y_train)
dt_model.fit(X_train, y_train)

# ── STEP 4: Predictions ──────────────────────────────────────
lr_pred = lr_model.predict(X_test)
dt_pred = dt_model.predict(X_test)

# ── STEP 5: Evaluation Metrics ───────────────────────────────
def print_metrics(name, y_true, y_pred):
    acc  = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average='weighted')
    rec  = recall_score(y_true, y_pred, average='weighted')
    f1   = f1_score(y_true, y_pred, average='weighted')

    print(f"\n{'=' * 60}")
    print(f"  📈 {name} – Evaluation Metrics")
    print(f"{'=' * 60}")
    print(f"  Accuracy  : {acc  * 100:.2f}%")
    print(f"  Precision : {prec * 100:.2f}%")
    print(f"  Recall    : {rec  * 100:.2f}%")
    print(f"  F1-Score  : {f1   * 100:.2f}%")
    print(f"\n{classification_report(y_true, y_pred, target_names=classes)}")

print_metrics("Logistic Regression", y_test, lr_pred)
print_metrics("Decision Tree",       y_test, dt_pred)

# ── STEP 6: Sample Predictions ───────────────────────────────
print("=" * 60)
print("  🔍 Sample Predictions – Logistic Regression (first 15)")
print("=" * 60)
print(f"  {'#':<4} {'Actual':<20} {'Predicted':<20} {'Result'}")
print("  " + "-" * 52)
for i, (actual, predicted) in enumerate(zip(y_test[:15], lr_pred[:15]), 1):
    result = "✅ Correct" if actual == predicted else "❌ Wrong"
    print(f"  {i:<4} {classes[actual]:<20} {classes[predicted]:<20} {result}")

# ── STEP 7: Confusion Matrix Plot ────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Iris Flower Classification – Confusion Matrices", fontsize=14, fontweight='bold')

for ax, (name, pred) in zip(axes, [
    ("Logistic Regression", lr_pred),
    ("Decision Tree",       dt_pred)
]):
    cm = confusion_matrix(y_test, pred)
    sns.heatmap(
        cm, annot=True, fmt='d', cmap='Blues',
        xticklabels=classes, yticklabels=classes, ax=ax,
        linewidths=0.5, linecolor='gray'
    )
    ax.set_title(f"{name}\nAccuracy: {accuracy_score(y_test, pred)*100:.1f}%")
    ax.set_xlabel("Predicted Label")
    ax.set_ylabel("True Label")

plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=150, bbox_inches='tight')
print("\n✅ Confusion matrix saved as: confusion_matrix.png")

# ── STEP 8: Predict Custom Input ─────────────────────────────
print("\n" + "=" * 60)
print("  🌸 PREDICT A NEW IRIS FLOWER")
print("=" * 60)

# Example prediction
sample = np.array([[5.1, 3.5, 1.4, 0.2]])  # Known Setosa
prediction = lr_model.predict(sample)[0]
probability = lr_model.predict_proba(sample)[0]

print(f"  Input Features : Sepal=5.1x3.5  Petal=1.4x0.2")
print(f"  Predicted Class: 🌸 {classes[prediction].upper()}")
print(f"\n  Confidence Scores:")
for cls, prob in zip(classes, probability):
    bar = "█" * int(prob * 30)
    print(f"    {cls:<20} {prob*100:5.1f}%  {bar}")

print("\n" + "=" * 60)
print("  ✅ Classification System Complete!")
print("=" * 60)
