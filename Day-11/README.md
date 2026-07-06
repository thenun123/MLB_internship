# 📘 Day 11 – Model Evaluation & Classification

## 🗂️ Folder Structure

```
Day-11/
├── classification_practice/
│   ├── 01_model_evaluation.py          # Accuracy, Precision, Recall, F1, Confusion Matrix
│   ├── 02_classification_logistic_regression.py   # Logistic Regression on Iris
│   └── 03_decision_tree.py             # Decision Tree + Model Comparison
├── iris_classification_project/
│   ├── iris_classification_system.py   # Full Mini Project
│   └── confusion_matrix.png            # Saved Confusion Matrix
└── README.md
```

---

## 🤔 What is Classification?

Classification is a supervised machine learning task where the goal is to predict which **category (class)** an input belongs to. The output is a **discrete label**, not a number.

**Real-world examples:**
- Email → Spam or Not Spam
- Tumor → Malignant or Benign
- Flower → Setosa / Versicolor / Virginica

---

## 📊 Regression vs Classification

| Feature | Regression | Classification |
|---|---|---|
| Output | Continuous value (e.g., 45.5) | Discrete class (e.g., "Spam") |
| Example | Predict house price | Predict flower species |
| Algorithms | Linear Regression, SVR | Logistic Regression, Decision Tree |
| Metric | RMSE, MAE, R² | Accuracy, F1-Score, Precision, Recall |

---

## 📐 Evaluation Metrics

### Accuracy
The percentage of correct predictions out of all predictions.
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```
> ✅ Good when classes are balanced.

### Precision
Out of all predicted positives, how many were actually positive?
```
Precision = TP / (TP + FP)
```
> ✅ Important when False Positives are costly (e.g., spam filters).

### Recall (Sensitivity)
Out of all actual positives, how many did the model catch?
```
Recall = TP / (TP + FN)
```
> ✅ Important when False Negatives are costly (e.g., disease detection).

### F1-Score
The harmonic mean of Precision and Recall — best when you need balance between both.
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

### Confusion Matrix
A table showing the breakdown of correct and incorrect predictions per class.

```
                Predicted
              Pos     Neg
Actual  Pos |  TP  |  FN  |
        Neg |  FP  |  TN  |
```

---

## 🌸 Iris Classification – Model Performance

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | **96.67%** | 96.97% | 96.67% | 96.66% |
| Decision Tree | 93.33% | 93.33% | 93.33% | 93.33% |

### Observations
- **Logistic Regression outperformed Decision Tree** on the Iris dataset with 96.67% vs 93.33% accuracy.
- Both models achieved **100% accuracy on Setosa** — it is linearly separable from the other two species.
- The slight confusion occurred between **Versicolor and Virginica**, which have overlapping feature distributions.
- Logistic Regression generalizes better here because the Iris dataset is nearly linearly separable.
- Decision Tree is more interpretable — petal length and petal width were the most important features.

### Feature Importance (Decision Tree)
| Feature | Importance |
|---|---|
| petal length (cm) | Highest |
| petal width (cm) | High |
| sepal length (cm) | Low |
| sepal width (cm) | Lowest |

---

## 🧠 Key Concepts Understood

- **Overfitting** = model performs well on training data but poorly on test data (high variance)
- **Underfitting** = model performs poorly on both training and test data (high bias)
- **Stratified split** ensures each class is proportionally represented in train/test sets
- The **square root trick** for primes and **sieve** for batch prime finding are efficient approaches
- Always check **training vs testing accuracy gap** to diagnose overfitting

---

## 📅 Date
**June 25, 2026**

> *"Focus on understanding the metrics rather than just generating them."*
