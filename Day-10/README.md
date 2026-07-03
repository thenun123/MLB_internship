# Day 10 — Data Preprocessing & Your First Machine Learning Model

This folder contains all the deliverables for Day 10 of the MLB Internship:
Data Preprocessing and building a first Linear Regression model with
Scikit-learn, using the `student_performance.csv` dataset.

## 📁 Folder Structure

```
Day-10/
├── student_performance.csv                 # Raw dataset
├── 1_data_preprocessing.py                 # Data Preprocessing Script
├── 2_linear_regression_model.py            # Linear Regression Model Script
├── 3_student_score_prediction_project.py   # Mini Project (full pipeline + charts)
├── outputs/
│   ├── actual_vs_predicted_scatter.png     # Scatter plot: Actual vs Predicted
│   └── actual_vs_predicted.csv             # Comparison table (Actual/Predicted/Diff)
└── README.md
```

## ▶️ How to Run

```bash
pip install pandas scikit-learn matplotlib

python 1_data_preprocessing.py               # preprocessing only
python 2_linear_regression_model.py           # preprocessing + training + metrics
python 3_student_score_prediction_project.py  # full mini project + chart + CSV output
```

## 🗂️ Dataset

`student_performance.csv` contains 20 students with the columns:
`Student_ID, Name, Age, Program (AI/SE/DS), Python, Mathematics, Statistics,
Machine_Learning, Attendance`.

## 🔧 Data Preprocessing — What I Learned

- **Why preprocessing matters:** raw data almost never comes in a form a
  model can use directly. Text categories, unscaled numbers, and missing
  values can all break training or bias the model toward whichever feature
  happens to have the largest numeric range.
- **Features vs Target:** the *features (X)* are the inputs the model
  learns from; the *target (y)* is the value it's trying to predict. Here,
  `Average_Score` (the mean of the four subject scores) is the target.
- **Handling categorical data:** `Program` (AI / SE / DS) is text, so it
  was converted to numbers using **Label Encoding**. Since `Program` has
  only 3 unrelated categories, **One-Hot Encoding** would technically be
  the more "correct" choice for a nominal variable (it avoids implying a
  false order like AI < DS < SE) — I used Label Encoding here to keep the
  feature set small for this exercise, but noted the trade-off.
- **Feature Scaling:** `Age` and `Attendance` are on very different scales
  (20-23 vs. 75-100). I applied **`StandardScaler`** (standardization) so
  every feature contributes fairly to the model instead of the
  larger-magnitude column dominating.
- **Data Leakage — the key insight of the day:** `Average_Score` is
  literally calculated *from* the `Python`, `Mathematics`, `Statistics` and
  `Machine_Learning` columns. If those same columns were used as *features*,
  the model would basically be shown the answer before making its
  "prediction," giving an artificially perfect (and useless) result. I
  **excluded those 4 columns from X** and instead predicted `Average_Score`
  from independent information: `Age`, `Program`, and `Attendance`.

## 🧪 Train-Test Split — Why It's Important

Splitting the data into a **training set (80%)** and a **testing set (20%)**
lets the model learn patterns from one portion of the data and then be
evaluated on data it has **never seen before**. Without this split, a model
could simply "memorize" the training data and look perfect while actually
being unable to generalize to new students — this is called *overfitting*.
The test set acts as a fair, honest check on real-world performance.

## 📊 Evaluation Metrics Used

| Metric | What it means |
|---|---|
| **MAE** (Mean Absolute Error) | Average size of the prediction error, in the same units as the score. Easy to interpret. |
| **MSE** (Mean Squared Error) | Like MAE, but squares errors first — penalizes large mistakes more heavily. |
| **R² Score** | Proportion of variance in `Average_Score` explained by the model (1.0 = perfect, 0 = no better than guessing the mean). |

## 📈 Model Performance & Observations

On this run (20 students, 16 train / 4 test):

| Metric | Value |
|---|---|
| MAE | ≈ 2.53 |
| MSE | ≈ 13.46 |
| R² Score | ≈ 0.80 |

**Observations:**
- With an R² of ~0.80, `Age`, `Program`, and `Attendance` together explain a
  good portion of the variation in average scores — `Attendance` in
  particular has the largest coefficient, suggesting it's the strongest
  predictor of the three.
- The dataset is very small (only 20 rows → 4 test samples), so these
  metrics are illustrative rather than statistically robust. Results would
  likely shift with a different random train/test split or more data.
- Deliberately leaving the 4 subject-score columns out of the features
  (to avoid data leakage) made this a genuinely harder, more meaningful
  prediction problem than simply averaging numbers back together.

## 🖼️ Generated Chart

`outputs/actual_vs_predicted_scatter.png` — scatter plot of Actual vs.
Predicted `Average_Score` for the test set, with a red dashed "perfect
prediction" reference line (points closer to the line = better
predictions).

## 🎥 Screen Recording

*(Add the link to your screen recording here once uploaded, explaining the
preprocessing steps, model training, and results walkthrough.)*
