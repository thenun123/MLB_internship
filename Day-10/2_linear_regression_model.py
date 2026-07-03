"""
Day 10 - Linear Regression Model Script
------------------------------------------
Uses the preprocessed data (see 1_data_preprocessing.py) to:
    1. Train a Linear Regression model (scikit-learn)
    2. Make predictions on the test set
    3. Compare Actual vs Predicted values
    4. Calculate MAE, MSE and R^2 Score
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from importlib import import_module

preprocessing = import_module("1_data_preprocessing")


def train_model(X_train, y_train) -> LinearRegression:
    """Train (fit) a Linear Regression model on the training data."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("[INFO] Linear Regression model trained.")
    print(f"[INFO] Model coefficients: {model.coef_}")
    print(f"[INFO] Model intercept  : {model.intercept_:.4f}")
    return model


def evaluate_model(model: LinearRegression, X_test, y_test):
    """Predict on the test set and compute evaluation metrics."""
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    metrics = {"MAE": mae, "MSE": mse, "R2": r2}

    print("\n[RESULTS] Model Evaluation Metrics")
    print(f"  Mean Absolute Error (MAE) : {mae:.3f}")
    print(f"  Mean Squared Error  (MSE) : {mse:.3f}")
    print(f"  R^2 Score                 : {r2:.3f}")

    return y_pred, metrics


def comparison_table(y_test, y_pred) -> pd.DataFrame:
    """Build a DataFrame comparing Actual vs Predicted Average_Score."""
    comparison = pd.DataFrame({
        "Actual": y_test.reset_index(drop=True),
        "Predicted": pd.Series(y_pred).round(2),
    })
    comparison["Difference"] = (comparison["Actual"] - comparison["Predicted"]).round(2)
    return comparison


if __name__ == "__main__":
    data = preprocessing.preprocess_pipeline()

    model = train_model(data["X_train"], data["y_train"])
    y_pred, metrics = evaluate_model(model, data["X_test"], data["y_test"])

    table = comparison_table(data["y_test"], y_pred)
    print("\n[RESULTS] Actual vs Predicted Average_Score:")
    print(table.to_string(index=False))

    print("\n[SUCCESS] Linear Regression model training & evaluation completed.")
