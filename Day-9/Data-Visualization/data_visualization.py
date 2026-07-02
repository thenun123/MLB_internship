# Data Visualization with Matplotlib & Seaborn
# Day 9 | MLB Python Bootcamp
# Generates: 5 charts saved as PNG files

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # non-interactive backend for saving files
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── Load cleaned dataset ──────────────────────────────────────
df = pd.read_csv("../Student-Performance-Dashboard/cleaned_student_performance.csv")
CHARTS_DIR = "../Charts"
os.makedirs(CHARTS_DIR, exist_ok=True)

# Style
sns.set_theme(style="whitegrid")
PALETTE = "Blues_d"

subjects = ["Python", "Mathematics", "Statistics", "ML_Score"]

print("Generating charts...")

# ────────────────────────────────────────────────────────────
# Chart 1: Bar Chart — Average Score per Student
# ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 6))

colors = []
for perf in df["Performance"]:
    if perf == "Excellent":   colors.append("#2ecc71")
    elif perf == "Good":      colors.append("#3498db")
    elif perf == "Average":   colors.append("#f39c12")
    else:                     colors.append("#e74c3c")

bars = ax.bar(df["Name"], df["Average_Score"], color=colors, edgecolor="white", linewidth=0.7)

# Value labels on bars
for bar, score in zip(bars, df["Average_Score"]):
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5, f"{score}", ha="center", va="bottom", fontsize=8)

ax.axhline(df["Average_Score"].mean(), color="red", linestyle="--", linewidth=1.5,
           label=f"Class Avg: {df['Average_Score'].mean():.2f}")

ax.set_title("Average Score per Student", fontsize=15, fontweight="bold", pad=15)
ax.set_xlabel("Student Name", fontsize=11)
ax.set_ylabel("Average Score", fontsize=11)
ax.set_ylim(0, 110)
ax.tick_params(axis="x", rotation=45)
ax.legend()

# Legend for colors
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor="#2ecc71", label="Excellent (≥90)"),
    Patch(facecolor="#3498db", label="Good (80-89)"),
    Patch(facecolor="#f39c12", label="Average (70-79)"),
    Patch(facecolor="#e74c3c", label="Needs Improvement (<70)"),
]
ax.legend(handles=legend_elements, loc="upper right", fontsize=8)

plt.tight_layout()
plt.savefig(f"{CHARTS_DIR}/01_bar_chart_avg_scores.png", dpi=150, bbox_inches="tight")
plt.close()
print("  ✅ Chart 1: Bar chart saved")

# ────────────────────────────────────────────────────────────
# Chart 2: Histogram — Distribution of Average Scores
# ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))

ax.hist(df["Average_Score"], bins=8, color="#3498db", edgecolor="white",
        linewidth=0.8, alpha=0.85)
ax.axvline(df["Average_Score"].mean(), color="red", linestyle="--", linewidth=2,
           label=f"Mean: {df['Average_Score'].mean():.2f}")
ax.axvline(df["Average_Score"].median(), color="orange", linestyle="--", linewidth=2,
           label=f"Median: {df['Average_Score'].median():.2f}")

ax.set_title("Distribution of Average Scores", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("Average Score", fontsize=11)
ax.set_ylabel("Number of Students", fontsize=11)
ax.legend()
plt.tight_layout()
plt.savefig(f"{CHARTS_DIR}/02_histogram_score_distribution.png", dpi=150, bbox_inches="tight")
plt.close()
print("  ✅ Chart 2: Histogram saved")

# ────────────────────────────────────────────────────────────
# Chart 3: Scatter Plot — Python vs Machine Learning
# ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 6))

program_colors = {"AI": "#e74c3c", "SE": "#2ecc71", "DS": "#3498db"}
for program, group in df.groupby("Program"):
    ax.scatter(group["Python"], group["ML_Score"],
               color=program_colors[program], label=program,
               s=100, edgecolors="white", linewidth=0.8, alpha=0.9)
    for _, row in group.iterrows():
        ax.annotate(row["Name"].split()[0],
                    (row["Python"], row["ML_Score"]),
                    textcoords="offset points", xytext=(6, 3), fontsize=7)

# Trend line
import numpy as np
m, b = np.polyfit(df["Python"], df["ML_Score"], 1)
x_line = np.linspace(df["Python"].min(), df["Python"].max(), 100)
ax.plot(x_line, m * x_line + b, color="gray", linestyle="--", linewidth=1.5,
        label="Trend line")

ax.set_title("Python Score vs Machine Learning Score", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("Python Score", fontsize=11)
ax.set_ylabel("Machine Learning Score", fontsize=11)
ax.legend()
plt.tight_layout()
plt.savefig(f"{CHARTS_DIR}/03_scatter_python_vs_ml.png", dpi=150, bbox_inches="tight")
plt.close()
print("  ✅ Chart 3: Scatter plot saved")

# ────────────────────────────────────────────────────────────
# Chart 4: Pie Chart — Performance Category Distribution
# ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 7))

perf_counts = df["Performance"].value_counts()
pie_colors  = ["#2ecc71", "#3498db", "#f39c12", "#e74c3c"]
explode     = [0.05] * len(perf_counts)

wedges, texts, autotexts = ax.pie(
    perf_counts.values,
    labels=perf_counts.index,
    autopct="%1.1f%%",
    colors=pie_colors[:len(perf_counts)],
    explode=explode,
    startangle=140,
    textprops={"fontsize": 11}
)
for at in autotexts:
    at.set_fontweight("bold")

ax.set_title("Student Performance Category Distribution\n(20 Students)",
             fontsize=14, fontweight="bold", pad=15)
plt.tight_layout()
plt.savefig(f"{CHARTS_DIR}/04_pie_performance_distribution.png", dpi=150, bbox_inches="tight")
plt.close()
print("  ✅ Chart 4: Pie chart saved")

# ────────────────────────────────────────────────────────────
# Chart 5: Box Plot — Spread of Marks per Subject
# ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 6))

subject_labels = ["Python", "Mathematics", "Statistics", "ML Score"]
data_to_plot   = [df["Python"], df["Mathematics"], df["Statistics"], df["ML_Score"]]

bp = ax.boxplot(data_to_plot, patch_artist=True, notch=False,
                medianprops=dict(color="black", linewidth=2))

box_colors = ["#3498db", "#e74c3c", "#2ecc71", "#9b59b6"]
for patch, color in zip(bp["boxes"], box_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax.set_xticks(range(1, 5))
ax.set_xticklabels(subject_labels, fontsize=11)
ax.set_title("Score Distribution per Subject (Box Plot)", fontsize=14,
             fontweight="bold", pad=12)
ax.set_ylabel("Score", fontsize=11)
ax.set_ylim(40, 110)

# Mean markers
for i, col in enumerate(["Python", "Mathematics", "Statistics", "ML_Score"], start=1):
    mean_val = df[col].mean()
    ax.plot(i, mean_val, "D", color="gold", markersize=8,
            markeredgecolor="black", markeredgewidth=0.8, label="Mean" if i == 1 else "")

ax.legend(["Mean"], loc="lower right")
plt.tight_layout()
plt.savefig(f"{CHARTS_DIR}/05_boxplot_subject_spread.png", dpi=150, bbox_inches="tight")
plt.close()
print("  ✅ Chart 5: Box plot saved")

print(f"\n✅ All 5 charts saved to '{CHARTS_DIR}/'")
