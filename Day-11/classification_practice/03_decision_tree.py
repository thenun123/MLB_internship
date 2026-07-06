# ============================================================
#        Decision Tree Classifier – Iris Dataset
#        Bonus: Compare with Logistic Regression
# ============================================================

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report

# ── Load & Split ─────────────────────────────────────────────
iris    = load_iris()
X, y    = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ── Train Both Models ────────────────────────────────────────
lr_model = LogisticRegression(max_iter=200, random_state=42)
dt_model = DecisionTreeClassifier(max_depth=4, random_state=42)

lr_model.fit(X_train, y_train)
dt_model.fit(X_train, y_train)

# ── Predictions ──────────────────────────────────────────────
lr_pred = lr_model.predict(X_test)
dt_pred = dt_model.predict(X_test)

# ── Comparison ───────────────────────────────────────────────
print("=" * 55)
print("   MODEL COMPARISON: Logistic Regression vs Decision Tree")
print("=" * 55)
print(f"\n  {'Metric':<20} {'Logistic Reg':>15} {'Decision Tree':>15}")
print("  " + "-" * 52)

metrics = {
    "Accuracy" : (accuracy_score(y_test, lr_pred), accuracy_score(y_test, dt_pred)),
    "F1-Score" : (f1_score(y_test, lr_pred, average='weighted'),
                  f1_score(y_test, dt_pred, average='weighted')),
}

for metric, (lr_val, dt_val) in metrics.items():
    winner = "← Better" if lr_val > dt_val else ("← Better" if dt_val > lr_val else "Tie")
    winner_side = f"{'':>10} {winner}" if dt_val >= lr_val else f" {winner}"
    print(f"  {metric:<20} {lr_val*100:>14.2f}%  {dt_val*100:>13.2f}%")

print("\n--- Decision Tree – Classification Report ---")
print(classification_report(y_test, dt_pred, target_names=iris.target_names))

# ── Decision Tree Insights ───────────────────────────────────
print("--- Decision Tree Feature Importances ---")
for name, importance in zip(iris.feature_names, dt_model.feature_importances_):
    bar = "█" * int(importance * 40)
    print(f"  {name:<30} {importance:.4f}  {bar}")

print("\n✅ Observation:")
print("   Both models perform well on Iris. Decision Tree is more")
print("   interpretable but can overfit. Logistic Regression is")
print("   more robust and generalizes better on unseen data.")
