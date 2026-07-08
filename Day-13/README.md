# 📘 Day 13 – Clustering & Dimensionality Reduction

## 🗂️ Folder Structure

```
Day-13/
├── dataset_exploration/
│   └── 01_explore_dataset.py           # head(), info(), describe(), correlations
├── kmeans_clustering/
│   ├── 02_kmeans_clustering.py         # Elbow Method + K-Means + Cluster viz
│   └── kmeans_clustering.png           # Elbow curve + cluster scatter plot
├── pca/
│   ├── 03_pca.py                       # PCA, Scree Plot, 2D projection
│   └── pca_visualization.png           # Scree plot + PCA scatter
├── mini_project/
│   ├── iris_clustering_pipeline.py     # Complete 7-step pipeline
│   └── iris_clustering_dashboard.png   # 6-panel visualization dashboard
└── README.md
```

---

## 🤔 What is Clustering?

Clustering is an **unsupervised learning** technique that groups similar data points together without using any labels. The algorithm discovers hidden structure in data on its own.

**Real-world examples:**
- Customer segmentation (group shoppers by behavior)
- Document grouping (cluster news articles by topic)
- Anomaly detection (find unusual patterns)
- Image compression (group similar pixel colors)

**K-Means** works by:
1. Randomly placing K centroids
2. Assigning each point to its nearest centroid
3. Recomputing centroids as the mean of assigned points
4. Repeating until centroids stop moving

---

## 🔬 What is PCA?

**Principal Component Analysis (PCA)** is a dimensionality reduction technique that transforms high-dimensional data into fewer dimensions while retaining as much information (variance) as possible.

**Why we need it:**
- Datasets with many features are hard to visualize and slow to train
- Many features may be correlated and carry redundant information
- PCA finds new axes (principal components) that capture the most variance

**How it works:**
1. Standardize the data
2. Compute the covariance matrix
3. Find eigenvectors (principal components) and eigenvalues (variance explained)
4. Project data onto the top K components

---

## 📐 How I Determined the Best Value of K

Two methods were used together:

### 1. Elbow Method
Plot inertia (WCSS – Within Cluster Sum of Squares) vs K. The point where the curve bends sharply (the "elbow") indicates the optimal K.

| K | Inertia  |
|---|----------|
| 1 | 597.35   |
| 2 | 222.36   |
| **3** | **139.82** ← Elbow |
| 4 | 114.09   |
| 5 | 90.93    |

### 2. Silhouette Score
Measures how similar a point is to its own cluster vs other clusters. Range: -1 to 1 (higher = better separation).

K=2 gave the highest silhouette (0.5818) but K=3 was chosen because it matches the known structure of the dataset and the elbow is clear at K=3.

---

## 📊 Results & Insights from Visualizations

### K-Means Clustering Results (K=3)
- **Inertia:** 139.82
- **Silhouette Score:** 0.4599
- **Adjusted Rand Index:** 0.6201 (0 = random, 1 = perfect)

### Cluster vs True Species
| Cluster | Setosa | Versicolor | Virginica |
|---------|--------|------------|-----------|
| 0       | 0      | 39         | 14        |
| 1       | 50     | 0          | 0         |
| 2       | 0      | 11         | 36        |

### PCA Results
| Component | Variance Explained | Cumulative |
|-----------|--------------------|------------|
| PC1       | 72.96%             | 72.96%     |
| PC2       | 22.85%             | 95.81%     |
| PC3       | 3.67%              | 99.48%     |
| PC4       | 0.52%              | 100.00%    |

---

## 💡 Key Observations

1. **Setosa is perfectly clustered** — All 50 Setosa flowers were correctly placed in a single cluster. It is linearly separable from the other two species using petal features alone.

2. **Versicolor and Virginica overlap** — 14 Virginica samples were placed in the Versicolor cluster and 11 Versicolor in the Virginica cluster. This biological overlap is a known property of the dataset.

3. **K-Means found the right structure without labels** — An ARI of 0.62 means K-Means recovered a significantly meaningful structure close to the real species groupings, purely from feature distances.

4. **PCA retained 95.81% of information in 2D** — We reduced 4 features down to 2 principal components with almost no information loss, making visualization intuitive.

5. **PC1 is driven by petal features** — Petal length and width have the highest loadings on PC1, confirming they are the most discriminative features in the dataset.

6. **Unsupervised vs Supervised** — Classification (Day 11) gave 96.67% accuracy using labels. K-Means clustering (no labels) gave an ARI of 0.62 — impressive for a completely label-free approach.

---

## 📅 Date
**July 2, 2026**

> *"Focus on understanding the concepts and interpreting the results rather than just generating the output."*
