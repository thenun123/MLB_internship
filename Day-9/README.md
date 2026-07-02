# Day 9 - Data Cleaning & Visualization

## 📚 Topics Covered Today

### 1. Data Cleaning with Pandas
- Checking for and handling missing values (`isnull()`)
- Removing duplicate records (`drop_duplicates()`)
- Renaming columns (`rename()`)
- Confirming and converting data types (`astype()`)
- Creating new computed columns (`Average_Score`, `Performance`)
- Sorting and filtering data

### 2. Data Visualization
- Why visualization matters: finding patterns, distributions, and anomalies that raw numbers hide
- **Matplotlib**: low-level plotting library, full control over every chart element
- **Seaborn**: high-level statistical visualization built on top of Matplotlib
- Charts created: Bar, Histogram, Scatter, Pie, Box Plot, Dashboard

---

## 📁 Folder Structure

```
Day-9/
│
├── Data-Cleaning/
│   └── data_cleaning.py                     # Full cleaning pipeline
│
├── Data-Visualization/
│   └── data_visualization.py                # 5 individual charts
│
├── Student-Performance-Dashboard/
│   ├── performance_dashboard.py             # Mini Project dashboard
│   └── cleaned_student_performance.csv      # Processed dataset
│
├── Charts/
│   ├── 01_bar_chart_avg_scores.png
│   ├── 02_histogram_score_distribution.png
│   ├── 03_scatter_python_vs_ml.png
│   ├── 04_pie_performance_distribution.png
│   ├── 05_boxplot_subject_spread.png
│   └── 06_performance_dashboard.png         # Full summary dashboard
│
├── student_performance.csv                  # Original dataset
└── README.md
```

---

## 🧹 Data Cleaning Steps Performed

| Step | Action | Result |
|------|--------|--------|
| 1 | Checked for missing values | 0 missing values found — dataset is complete |
| 2 | Checked for duplicates | 0 duplicate rows found |
| 3 | Renamed columns | `Machine_Learning → ML_Score`, `Student_ID → ID` |
| 4 | Verified data types | Age confirmed as `int`, all scores as `int` |
| 5 | Created `Average_Score` | Row-wise mean across 4 subjects, rounded to 2 decimal places |
| 6 | Created `Performance` | Categorical label based on average score thresholds |
| 7 | Sorted dataset | Sorted by `Average_Score` descending for easier reading |
| 8 | Saved output | `cleaned_student_performance.csv` with 11 columns |

**Performance Categories:**
- **Excellent** → Average Score ≥ 90
- **Good** → 80–89
- **Average** → 70–79
- **Needs Improvement** → below 70

---

## 📊 Visualizations Created & Why

| Chart | Type | Purpose |
|-------|------|---------|
| Average Score per Student | Bar Chart | Compare individual student performance at a glance; colored by performance category |
| Score Distribution | Histogram | See whether scores are normally distributed or skewed; identify the most common score range |
| Python vs ML Score | Scatter Plot | Check if there is a correlation between Python and ML marks; grouped by program |
| Performance Categories | Pie Chart | Quickly show the proportion of students in each performance tier |
| Subject Score Spread | Box Plot | Compare variability, median, and outliers across all 4 subjects simultaneously |
| Summary Dashboard | 6-panel Figure | Combine all key findings into one shareable overview |

---

## 🔍 Three Key Insights from the Dataset

**1. SE students dramatically outperform other programs.**
Software Engineering students averaged 85.96, compared to AI (80.88) and DS (74.21). All 4 "Excellent" students and 4 of the top 5 overall were from SE. This could reflect better preparation, stronger fundamentals, or course alignment with the subjects assessed.

**2. Machine Learning is the highest-scoring subject, Python is the lowest.**
Average scores: ML (82.6) > Statistics (80.6) > Mathematics (79.5) > Python (78.9). This is somewhat surprising — students might find Python syntax and programming logic harder than conceptual ML topics, or they may already have exposure to ML theory before the course.

**3. Attendance and performance are closely correlated.**
Hassan Tariq, the lowest performer (58.75 average), also had the lowest attendance (75%). All 4 "Needs Improvement" students had attendance below 86%, while the top performers all had 94%+. This suggests that consistent attendance is a strong predictor of academic performance in this dataset.

---

## 🚧 Challenges Faced

- **Choosing the right chart type**: Picking a box plot over a grouped bar chart for subject comparison was a deliberate choice — box plots show median, spread, and outliers all at once, which a bar chart can't.
- **Matplotlib backend**: Running without a display (server/headless environment) requires `matplotlib.use("Agg")` before any other matplotlib imports, otherwise charts silently fail to save.
- **Color coding by performance**: Using conditional coloring in the bar chart required building a `colors` list by iterating over the `Performance` column instead of using a palette directly — took some trial and error.
- **Dashboard layout**: Using `fig.add_subplot(2, 3, N)` for a 2×3 grid and aligning `tight_layout` correctly to avoid overlapping titles required careful tuning of `rect` and `pad` parameters.

---

## ✅ What I Can Do Now

- Clean real-world datasets confidently (missing values, duplicates, type fixes, derived columns)
- Choose the right visualization for the question being asked
- Use Matplotlib for precise, fully customized charts
- Use Seaborn's `set_theme()` for clean, professional styling
- Present data analysis findings in a structured, readable dashboard
- Understand the end-to-end data preparation pipeline before building ML models

---

## 🛠️ How to Run

```bash
# Step 1: Clean the data
cd Data-Cleaning
python data_cleaning.py

# Step 2: Generate individual charts
cd ../Data-Visualization
python data_visualization.py

# Step 3: Run the full dashboard
cd ../Student-Performance-Dashboard
python performance_dashboard.py
```

Charts are saved to the `Charts/` folder as PNG files.

---

*Day 9 | MLB Python Bootcamp | Mian Azeem Naseer*
