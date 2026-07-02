"""
=============================================================
  Student Performance Dashboard
  Day 9 Mini Project | MLB Python Bootcamp
=============================================================
  Answers 6 key analytical questions using the cleaned
  dataset, then generates a summary chart dashboard.
=============================================================
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import os

CLEAN_CSV  = "cleaned_student_performance.csv"
CHARTS_DIR = "../Charts"
os.makedirs(CHARTS_DIR, exist_ok=True)

sns.set_theme(style="whitegrid")

# ── Load ──────────────────────────────────────────────────────
df = pd.read_csv(CLEAN_CSV)
subjects = ["Python", "Mathematics", "Statistics", "ML_Score"]

print("=" * 65)
print("   📊 STUDENT PERFORMANCE DASHBOARD")
print("=" * 65)

# ─────────────────────────────────────────────
# Q1: How many students are in the dataset?
# ─────────────────────────────────────────────
total_students = len(df)
print(f"\n❓ Q1: Total number of students")
print(f"   ➜  {total_students} students across 3 programs: "
      f"{', '.join(df['Program'].unique())}")
for prog, cnt in df["Program"].value_counts().items():
    print(f"      {prog}: {cnt} students")

# ─────────────────────────────────────────────
# Q2: Average score for each subject?
# ─────────────────────────────────────────────
print(f"\n❓ Q2: Average score per subject")
subject_avgs = df[subjects].mean().round(2)
for subj, avg in subject_avgs.items():
    bar = "█" * int(avg // 5)
    print(f"   {subj:<15}: {avg:>5}  {bar}")

# ─────────────────────────────────────────────
# Q3: Top 5 performing students?
# ─────────────────────────────────────────────
print(f"\n❓ Q3: Top 5 performing students")
top5 = df.nlargest(5, "Average_Score")[
    ["ID", "Name", "Program", "Average_Score", "Performance"]
].reset_index(drop=True)
top5.index += 1
print(top5.to_string())

# ─────────────────────────────────────────────
# Q4: Which students need improvement?
# ─────────────────────────────────────────────
print(f"\n❓ Q4: Students needing improvement (Average Score < 70)")
needs_imp = df[df["Performance"] == "Needs Improvement"][
    ["Name", "Program", "Average_Score"] + subjects
].reset_index(drop=True)
print(needs_imp.to_string(index=False))
print(f"   Count: {len(needs_imp)} students")

# ─────────────────────────────────────────────
# Q5: Which subject has the highest class average?
# ─────────────────────────────────────────────
best_subject = subject_avgs.idxmax()
print(f"\n❓ Q5: Subject with highest class average")
print(f"   ➜  {best_subject} ({subject_avgs[best_subject]})")
print(f"   Ranking:")
for rank, (subj, avg) in enumerate(subject_avgs.sort_values(ascending=False).items(), 1):
    print(f"   {rank}. {subj:<15}: {avg}")

# ─────────────────────────────────────────────
# Q6: Program-wise performance comparison
# ─────────────────────────────────────────────
print(f"\n❓ Q6: Program-wise average performance")
prog_perf = df.groupby("Program")["Average_Score"].mean().round(2).sort_values(ascending=False)
for prog, avg in prog_perf.items():
    print(f"   {prog}: {avg}")

# ─────────────────────────────────────────────
# DASHBOARD CHART: 2x3 Summary Figure
# ─────────────────────────────────────────────
print(f"\n📊 Generating dashboard summary chart...")

fig = plt.figure(figsize=(18, 12))
fig.suptitle("Student Performance Dashboard", fontsize=18,
             fontweight="bold", y=0.98)

# ── Panel 1: Top 5 Students (horizontal bar) ─
ax1 = fig.add_subplot(2, 3, 1)
colors_top5 = ["#2ecc71", "#27ae60", "#3498db", "#2980b9", "#9b59b6"]
ax1.barh(top5["Name"][::-1], top5["Average_Score"][::-1],
         color=colors_top5[::-1], edgecolor="white")
for i, (name, score) in enumerate(zip(top5["Name"][::-1], top5["Average_Score"][::-1])):
    ax1.text(score + 0.3, i, f"{score}", va="center", fontsize=8, fontweight="bold")
ax1.set_title("Top 5 Students", fontweight="bold")
ax1.set_xlabel("Average Score")
ax1.set_xlim(0, 110)

# ── Panel 2: Subject Averages (bar) ──────────
ax2 = fig.add_subplot(2, 3, 2)
subj_labels = ["Python", "Math", "Statistics", "ML"]
bars = ax2.bar(subj_labels, subject_avgs.values,
               color=["#e74c3c", "#3498db", "#2ecc71", "#9b59b6"],
               edgecolor="white")
for bar, val in zip(bars, subject_avgs.values):
    ax2.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 0.5, f"{val}", ha="center", fontsize=9, fontweight="bold")
ax2.set_title("Subject Averages", fontweight="bold")
ax2.set_ylabel("Average Score")
ax2.set_ylim(0, 105)

# ── Panel 3: Performance Distribution (pie) ──
ax3 = fig.add_subplot(2, 3, 3)
perf_counts = df["Performance"].value_counts()
pie_colors  = ["#2ecc71", "#3498db", "#f39c12", "#e74c3c"]
ax3.pie(perf_counts.values, labels=perf_counts.index,
        autopct="%1.0f%%", colors=pie_colors[:len(perf_counts)],
        startangle=140, textprops={"fontsize": 9})
ax3.set_title("Performance Distribution", fontweight="bold")

# ── Panel 4: Score distribution histogram ────
ax4 = fig.add_subplot(2, 3, 4)
ax4.hist(df["Average_Score"], bins=7, color="#3498db", edgecolor="white", alpha=0.85)
ax4.axvline(df["Average_Score"].mean(), color="red", linestyle="--",
            linewidth=1.5, label=f"Mean: {df['Average_Score'].mean():.1f}")
ax4.set_title("Score Distribution", fontweight="bold")
ax4.set_xlabel("Average Score")
ax4.set_ylabel("# Students")
ax4.legend(fontsize=8)

# ── Panel 5: Program-wise box plot ───────────
ax5 = fig.add_subplot(2, 3, 5)
prog_order = ["SE", "AI", "DS"]
prog_colors = {"SE": "#2ecc71", "AI": "#3498db", "DS": "#e74c3c"}
data_by_prog = [df[df["Program"] == p]["Average_Score"].values for p in prog_order]
bp = ax5.boxplot(data_by_prog, patch_artist=True,
                 medianprops=dict(color="black", linewidth=2))
for patch, prog in zip(bp["boxes"], prog_order):
    patch.set_facecolor(prog_colors[prog])
    patch.set_alpha(0.75)
ax5.set_xticks(range(1, 4))
ax5.set_xticklabels(prog_order)
ax5.set_title("Score Spread by Program", fontweight="bold")
ax5.set_ylabel("Average Score")

# ── Panel 6: Needs Improvement students ──────
ax6 = fig.add_subplot(2, 3, 6)
ni = df[df["Performance"] == "Needs Improvement"].sort_values("Average_Score")
bar_colors = ["#e74c3c"] * len(ni)
ax6.barh(ni["Name"], ni["Average_Score"], color=bar_colors, edgecolor="white")
for i, (name, score) in enumerate(zip(ni["Name"], ni["Average_Score"])):
    ax6.text(score + 0.3, i, f"{score}", va="center", fontsize=9, fontweight="bold")
ax6.axvline(70, color="black", linestyle="--", linewidth=1.2, label="Min threshold (70)")
ax6.set_title("Needs Improvement", fontweight="bold")
ax6.set_xlabel("Average Score")
ax6.set_xlim(0, 80)
ax6.legend(fontsize=8)

plt.tight_layout(rect=[0, 0, 1, 0.96])
dashboard_path = f"{CHARTS_DIR}/06_performance_dashboard.png"
plt.savefig(dashboard_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"   ✅ Dashboard saved → '{dashboard_path}'")

print("\n" + "=" * 65)
print("   Dashboard Complete!")
print("=" * 65)
