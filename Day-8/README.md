# Day 8 - NumPy & Pandas for Data Science

## 📚 Topics Covered Today

### 1. NumPy Fundamentals
- What NumPy is: a high-performance numerical computing library built on C arrays
- Creating arrays: `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`, `np.eye()`
- Array properties: `shape`, `ndim`, `dtype`
- Element-wise arithmetic (+, -, *, /) and scalar broadcasting
- Matrix multiplication with `@` and transpose with `.T`
- Aggregate functions: `max`, `min`, `mean`, `sum`, `std`, `var`, `median`
- Axis-based operations (across rows with `axis=1`, across columns with `axis=0`)
- Reshaping: `reshape()`, `flatten()`
- Indexing and slicing (1D and 2D), fancy/boolean indexing
- Universal math functions: `sqrt`, `log`, `exp`, `abs`

### 2. Pandas Basics
- Series and DataFrames — the two core data structures
- Loading CSV data with `pd.read_csv()`
- Exploring datasets: `head()`, `tail()`, `info()`, `describe()`, `shape`, `dtypes`
- Detecting missing values with `isnull().sum()`
- Selecting columns (single and multiple), using `loc` (label-based) and `iloc` (position-based)
- Filtering data with boolean conditions and `&`/`|` operators
- Sorting with `sort_values()`
- Grouping and aggregation with `groupby()`
- Adding computed columns to a DataFrame
- Saving results with `to_csv()`

---

## 📁 Folder Structure

```
Day-8/
│
├── NumPy-Practice/
│   ├── 01_create_arrays.py         # 1D and 2D array creation
│   ├── 02_array_operations.py      # Arithmetic, broadcasting, comparisons
│   ├── 03_math_functions.py        # max, min, mean, sum, std, axis ops
│   └── 04_reshape_slice.py         # Reshape, flatten, indexing, slicing
│
├── Pandas-Practice/
│   ├── 01_load_explore.py          # read_csv, head, tail, info, dtypes
│   ├── 02_missing_statistics.py    # isnull, describe, value_counts
│   └── 03_select_filter.py         # loc, iloc, boolean filtering, sort
│
├── Student-Performance-Analysis/
│   ├── student_analysis.py                  # Mini Project - full analysis
│   ├── student_performance.csv              # Original dataset
│   └── student_performance_analyzed.csv     # Processed output with new columns
│
└── README.md
```

---

## 🧠 What I Learned About NumPy

NumPy is the backbone of scientific computing in Python. Its core advantage over plain Python lists is that it stores data in contiguous memory blocks (like C arrays), which makes operations dramatically faster — especially on large datasets used in Machine Learning.

The most important insight was understanding **vectorized operations**: instead of looping over each element, NumPy applies operations to the entire array at once. For example, `arr * 2` multiplies every element without a single `for` loop. This is exactly how PyTorch and TensorFlow handle tensors under the hood — so understanding NumPy first makes understanding deep learning frameworks much easier.

**Broadcasting** was the trickiest concept: how NumPy automatically expands scalar or smaller-shaped arrays to match the shape of a larger one during operations, without actually copying data in memory.

---

## 🐼 What I Learned About Pandas

Pandas gives NumPy's raw arrays meaningful structure — column names, row labels, mixed data types, and a rich API for data manipulation. The workflow I practiced today is the standard starting point for every data science project:

1. **Load** → `pd.read_csv()`
2. **Inspect** → `head()`, `info()`, `describe()`
3. **Clean** → check `isnull()`, handle bad data
4. **Filter/Select** → `loc`, `iloc`, boolean masks
5. **Analyze** → `groupby()`, `mean()`, computed columns
6. **Save** → `to_csv()`

The key distinction that took time to click: `loc` uses **labels** (column names, index values), while `iloc` uses **integer positions** (like list indexing). Getting this wrong produces subtle bugs.

---

## 📊 Key Insights from the Dataset

The dataset contained 20 students from 3 programs (AI, SE, DS) with scores in Python, Mathematics, Statistics, and Machine Learning.

**Top findings:**

- **SE (Software Engineering) students outperformed all other programs** with an average of 85.96, compared to AI (80.88) and DS (74.21). SE had 4 of the top 5 performing students.
- **Laiba Khan (S018)** achieved the highest average of 97.25 across all subjects with perfect 100% attendance.
- **Hassan Tariq (S007)** is the only student who failed (average 58.75) and also had the lowest attendance (75%) — suggesting a clear correlation between attendance and performance.
- **Machine Learning** had the highest subject average (82.6), while Python had the lowest (78.9).
- **19 out of 20 students passed** (≥60 average). 10 students scored below the class average of 80.40.
- **5 students** had attendance below 85%, all of whom scored below the class average — reinforcing the attendance-performance link.

---

## 🚧 Challenges Faced

- **Axis confusion in NumPy**: `axis=0` operates *down the rows* (across all rows → result is per column), while `axis=1` operates *across columns* (→ result is per row). This is backwards from what feels intuitive at first. Drawing the shapes on paper helped solidify it.
- **Boolean indexing with multiple conditions**: In Pandas, `&` and `|` must be used instead of `and`/`or`, and each condition must be wrapped in parentheses `()`. Forgetting the parentheses gives a cryptic error.
- **`loc` vs `iloc` distinction**: At first I kept mixing them up. The rule that helped: "loc = labels, iloc = integers."
- **Adding computed columns cleanly**: Using `df[SUBJECTS].mean(axis=1)` computes the row-wise mean across only the subject columns without touching other columns — getting the axis direction right was key.

---

## ✅ What I Can Do Now

- Work confidently with NumPy arrays for numerical computation
- Load, explore, filter, and manipulate tabular datasets using Pandas
- Perform real data analysis: averages, distributions, groupby, ranking
- Add computed columns and derive insights from raw data
- Save processed datasets for downstream use
- Understand how data is structured before feeding it into ML models

---

## 🛠️ How to Run

### NumPy Practice
```bash
cd NumPy-Practice
python 01_create_arrays.py
python 02_array_operations.py
python 03_math_functions.py
python 04_reshape_slice.py
```

### Pandas Practice
```bash
cd Pandas-Practice
python 01_load_explore.py
python 02_missing_statistics.py
python 03_select_filter.py
```

### Mini Project
```bash
cd Student-Performance-Analysis
python student_analysis.py
```

---

*Day 8 | MLB Python Bootcamp | Mian Azeem Naseer*
