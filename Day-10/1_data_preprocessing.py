"""
Day 10 - Data Preprocessing Script
------------------------------------
Dataset : student_performance.csv
Goal    : Prepare the raw student dataset for Machine Learning by:
    1. Loading the dataset
    2. Encoding categorical columns (Program -> Label Encoding)
    3. Creating the target column 'Average_Score'
    4. Selecting Feature (X) and Target (y) columns
    5. Splitting into Train (80%) / Test (20%) sets
    6. Scaling numeric features (StandardScaler)

This script can be imported by other scripts (linear_regression_model.py,
student_score_prediction_project.py) so preprocessing logic lives in ONE place.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

DATA_PATH = "student_performance.csv"

SUBJECT_COLUMNS = ["Python", "Mathematics", "Statistics", "Machine_Learning"]


def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    """Load the raw CSV file into a DataFrame."""
    df = pd.read_csv(path)
    print(f"[INFO] Dataset loaded successfully -> shape: {df.shape}")
    return df


def create_average_score(df: pd.DataFrame) -> pd.DataFrame:
    """Create the 'Average_Score' target column from the 4 subject scores."""
    df = df.copy()
    df["Average_Score"] = df[SUBJECT_COLUMNS].mean(axis=1).round(2)
    return df


def encode_categorical(df: pd.DataFrame):
    """
    Encode the categorical 'Program' column using Label Encoding.

    Program only has 3 unique values (AI, SE, DS) with no natural order,
    so One-Hot Encoding would technically be the 'purest' choice, but since
    scikit-learn's LinearRegression can handle a small integer-coded column
    without implying rank for a 3-category nominal feature in this exercise,
    we demonstrate Label Encoding here (and mention the One-Hot alternative
    in the README).
    """
    df = df.copy()
    le = LabelEncoder()
    df["Program_Encoded"] = le.fit_transform(df["Program"])
    print(f"[INFO] Encoded 'Program' classes -> {list(le.classes_)} "
          f"-> {list(le.transform(le.classes_))}")
    return df, le


def get_features_and_target(df: pd.DataFrame):
    """
    Select Feature columns (X) and Target column (y).

    IMPORTANT - Avoiding Data Leakage:
    Average_Score is DERIVED from Python, Mathematics, Statistics and
    Machine_Learning. If we used those same 4 columns as features, the
    model would essentially be given the answer (X would mathematically
    determine y), producing a meaningless "perfect" R^2 score. This is a
    textbook example of DATA LEAKAGE, so those 4 columns are EXCLUDED from
    the feature set.

    Instead we predict a student's Average_Score from independent,
    non-derived information: Age, Program and Attendance.
    """
    feature_cols = ["Age", "Program_Encoded", "Attendance"]
    target_col = "Average_Score"

    X = df[feature_cols]
    y = df[target_col]

    print(f"[INFO] Feature columns (X): {feature_cols}")
    print(f"[INFO] Target column (y): {target_col}")
    return X, y


def split_and_scale(X, y, test_size: float = 0.2, random_state: int = 42):
    """Split into train/test sets and scale numeric features."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)   # fit ONLY on training data
    X_test_scaled = scaler.transform(X_test)          # transform test with same scaler

    print(f"[INFO] Train set size: {X_train.shape[0]} rows")
    print(f"[INFO] Test set size : {X_test.shape[0]} rows")
    print("[INFO] Feature scaling applied using StandardScaler "
          "(fit on train set only, to avoid data leakage).")

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def preprocess_pipeline(path: str = DATA_PATH):
    """Run the full preprocessing pipeline and return everything needed for modeling."""
    df = load_data(path)
    df = create_average_score(df)
    df, label_encoder = encode_categorical(df)
    X, y = get_features_and_target(df)
    X_train, X_test, y_train, y_test, scaler = split_and_scale(X, y)
    return {
        "df": df,
        "X": X,
        "y": y,
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
        "scaler": scaler,
        "label_encoder": label_encoder,
    }


if __name__ == "__main__":
    result = preprocess_pipeline()
    print("\n[INFO] Preview of processed dataset:")
    print(result["df"][["Student_ID", "Program", "Program_Encoded",
                         "Age", "Attendance", "Average_Score"]].head())
    print("\n[SUCCESS] Data preprocessing completed.")
