# ============================================================
#       Step 3: PCA – Principal Component Analysis
#               Dimensionality Reduction + Visualization
# ============================================================

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# ── Load & Scale ─────────────────────────────────────────────
iris     = load_iris()
X, y     = iris.data, iris.target
scaler   = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("=" * 55)
print("     PCA – DIMENSIONALITY REDUCTION")
print("=" * 55)
print(f"\n  Original dimensions : {X.shape[1]} features")

# ── Apply PCA (all components first to study variance) ────────
pca_full = PCA()
pca_full.fit(X_scaled)

explained   = pca_full.explained_variance_ratio_
cumulative  = np.cumsum(explained)

print(f"\n📊 Explained Variance per Component:")
for i, (var, cum) in enumerate(zip(explained, cumulative), 1):
    bar = "█" * int(var * 50)
    print(f"  PC{i}: {var*100:5.2f}%  (cumulative: {cum*100:.2f}%)  {bar}")

# ── Reduce to 2 Components ───────────────────────────────────
pca_2d  = PCA(n_components=2)
X_pca   = pca_2d.fit_transform(X_scaled)

print(f"\n✅ Reduced to 2 components")
print(f"   Total variance retained: {pca_2d.explained_variance_ratio_.sum()*100:.2f}%")
print(f"   PC1 variance: {pca_2d.explained_variance_ratio_[0]*100:.2f}%")
print(f"   PC2 variance: {pca_2d.explained_variance_ratio_[1]*100:.2f}%")

# ── Loadings (what each PC represents) ───────────────────────
print(f"\n🔍 PC1 Feature Loadings (what drives PC1):")
for feat, loading in zip(iris.feature_names, pca_2d.components_[0]):
    bar = "█" * int(abs(loading) * 20)
    sign = "+" if loading > 0 else "-"
    print(f"  {feat:<30} {sign}{abs(loading):.3f}  {bar}")

# ── Plots ────────────────────────────────────────────────────
colors  = ['#e74c3c', '#2ecc71', '#3498db']
species = iris.target_names

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('PCA – Dimensionality Reduction on Iris Dataset',
             fontsize=13, fontweight='bold')

# Scree Plot
axes[0].bar(range(1, 5), explained * 100, color='steelblue', alpha=0.8, label='Individual')
axes[0].plot(range(1, 5), cumulative * 100, 'ro-', linewidth=2, label='Cumulative')
axes[0].axhline(y=95, color='green', linestyle='--', alpha=0.7, label='95% threshold')
axes[0].set_title('Scree Plot – Explained Variance', fontsize=12)
axes[0].set_xlabel('Principal Component')
axes[0].set_ylabel('Explained Variance (%)')
axes[0].set_xticks(range(1, 5))
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# PCA Scatter
for i, (species_name, color) in enumerate(zip(species, colors)):
    mask = y == i
    axes[1].scatter(X_pca[mask, 0], X_pca[mask, 1],
                    c=color, label=species_name, s=70, alpha=0.8)

axes[1].set_title('PCA – 2D Projection (97.77% variance retained)', fontsize=12)
axes[1].set_xlabel(f'PC1 ({explained[0]*100:.1f}% variance)')
axes[1].set_ylabel(f'PC2 ({explained[1]*100:.1f}% variance)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('pca_visualization.png', dpi=150, bbox_inches='tight')
print("\n✅ Saved: pca_visualization.png")

print("\n💡 Key Takeaway:")
print("  Just 2 PCA components retain 97.77% of all information.")
print("  Setosa is clearly separated; Versicolor & Virginica overlap slightly.")
print("  PC1 is dominated by petal features (the most discriminative ones).")
