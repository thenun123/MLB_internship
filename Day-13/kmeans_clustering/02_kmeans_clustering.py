# ============================================================
#       Step 2: K-Means Clustering + Elbow Method
# ============================================================

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ── Load & Scale ─────────────────────────────────────────────
iris    = load_iris()
X       = iris.data
scaler  = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("=" * 55)
print("     K-MEANS CLUSTERING – IRIS DATASET")
print("=" * 55)

# ── Elbow Method ─────────────────────────────────────────────
print("\n📐 Running Elbow Method (K = 1 to 10)...")
inertias = []
k_range  = range(1, 11)

for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)
    print(f"  K={k:2}  Inertia: {km.inertia_:.2f}")

# ── Plot Elbow Curve ─────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(k_range, inertias, 'bo-', linewidth=2, markersize=8)
axes[0].axvline(x=3, color='red', linestyle='--', alpha=0.7, label='Optimal K=3')
axes[0].set_title('Elbow Method – Optimal K', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Number of Clusters (K)')
axes[0].set_ylabel('Inertia (WCSS)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# ── Apply K-Means with K=3 ───────────────────────────────────
kmeans  = KMeans(n_clusters=3, random_state=42, n_init=10)
labels  = kmeans.fit_predict(X_scaled)
centers = kmeans.cluster_centers_

print(f"\n✅ K-Means applied with K=3")
print(f"   Inertia : {kmeans.inertia_:.2f}")
print(f"\n   Cluster Sizes:")
for i in range(3):
    count = np.sum(labels == i)
    print(f"     Cluster {i} : {count} samples")

# ── Scatter Plot: Clusters vs True Labels ────────────────────
colors  = ['#e74c3c', '#2ecc71', '#3498db']
markers = ['o', 's', '^']

for i in range(3):
    mask = labels == i
    axes[1].scatter(X[mask, 2], X[mask, 3],
                    c=colors[i], marker=markers[i],
                    label=f'Cluster {i}', s=70, alpha=0.8)

# Plot centroids (inverse transform for original scale)
centers_orig = scaler.inverse_transform(centers)
axes[1].scatter(centers_orig[:, 2], centers_orig[:, 3],
                c='black', marker='*', s=250, zorder=5, label='Centroids')

axes[1].set_title('K-Means Clusters (Petal Features)', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Petal Length (cm)')
axes[1].set_ylabel('Petal Width (cm)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('kmeans_clustering.png', dpi=150, bbox_inches='tight')
print("\n✅ Saved: kmeans_clustering.png")

# ── Cluster vs True Label Comparison ─────────────────────────
print("\n📊 Cluster vs Actual Species Mapping:")
import pandas as pd
df_check = pd.DataFrame({'cluster': labels, 'species': iris.target})
ct = pd.crosstab(df_check['cluster'], df_check['species'],
                 colnames=['Species'], rownames=['Cluster'])
ct.columns = iris.target_names
print(ct.to_string())
print("\n✅ Cluster 0 ≈ Setosa | Cluster 1 ≈ Virginica | Cluster 2 ≈ Versicolor")
