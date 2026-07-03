"""
Day 10 - Mini Project: Student Score Prediction System
===========================================================
A simple end-to-end Machine Learning application that:
    1. Loads the student_performance.csv dataset
    2. Preprocesses the data (encoding, feature/target split, scaling)
    3. Trains a Linear Regression model
    4. Predicts student Average_Score values
    5. Displays model evaluation metrics (MAE, MSE, R^2)
    6. Prints a comparison table of Actual vs Predicted scores
    7. Visualizes Actual vs Predicted values with a scatter plot

Run with:  python 3_student_score_prediction_project.py
"""

import os
from importlib import import_module

import matplotlib
matplotlib.use("Agg")  # safe for headless/script execution
import matplotlib.pyplot as plt

preprocessing = import_module("1_data_preprocessing")
lr_model = import_module("2_linear_regression_model")

OUTPUT_DIR = "outputs"


def plot_actual_vs_predicted(y_test, y_pred, save_path: str):
    """Scatter plot comparing Actual vs Predicted Average_Score."""
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, color="#4C72B0", s=90, edgecolor="black",
                alpha=0.8, label="Predictions")

    # Perfect prediction reference line (y = x)
    min_val = min(min(y_test), min(y_pred))
    max_val = max(max(y_test), max(y_pred))
    plt.plot([min_val, max_val], [min_val, max_val], color="red",
              linestyle="--", linewidth=2, label="Perfect Prediction Line")

    plt.title("Actual vs Predicted Average Score", fontsize=14, fontweight="bold")
    plt.xlabel("Actual Average Score")
    plt.ylabel("Predicted Average Score")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"[INFO] Scatter plot saved to '{save_path}'")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("=" * 60)
    print(" STUDENT SCORE PREDICTION SYSTEM")
    print("=" * 60)

    # 1 & 2: Load + preprocess
    print("\n--- Step 1 & 2: Load & Preprocess Data ---")
    data = preprocessing.preprocess_pipeline()

    # 3: Train model
    print("\n--- Step 3: Train Linear Regression Model ---")
    model = lr_model.train_model(data["X_train"], data["y_train"])

    # 4 & 5: Predict + evaluate
    print("\n--- Step 4 & 5: Predict & Evaluate ---")
    y_pred, metrics = lr_model.evaluate_model(model, data["X_test"], data["y_test"])

    # 6: Comparison table
    print("\n--- Step 6: Actual vs Predicted Comparison Table ---")
    table = lr_model.comparison_table(data["y_test"], y_pred)
    print(table.to_string(index=False))

    # Save comparison table to CSV as well, for the deliverables folder
    table_path = os.path.join(OUTPUT_DIR, "actual_vs_predicted.csv")
    table.to_csv(table_path, index=False)
    print(f"\n[INFO] Comparison table saved to '{table_path}'")

    # 7: Visualization
    print("\n--- Step 7: Visualize Results ---")
    plot_path = os.path.join(OUTPUT_DIR, "actual_vs_predicted_scatter.png")
    plot_actual_vs_predicted(data["y_test"], y_pred, plot_path)

    print("\n" + "=" * 60)
    print(" FINAL MODEL PERFORMANCE SUMMARY")
    print("=" * 60)
    print(f"  MAE : {metrics['MAE']:.3f}")
    print(f"  MSE : {metrics['MSE']:.3f}")
    print(f"  R^2 : {metrics['R2']:.3f}")
    print("=" * 60)
    print("\n[SUCCESS] Student Score Prediction System run completed.")


if __name__ == "__main__":
    main()
