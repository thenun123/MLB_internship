"""
=============================================================
  Student Performance Analysis
  Day 8 Mini Project | MLB Python Bootcamp
=============================================================
  Uses: Pandas + NumPy
  Dataset: student_performance.csv (20 students)
  Output: student_performance_analyzed.csv
=============================================================
"""

import pandas as pd
import numpy as np

DATASET = "student_performance.csv"
OUTPUT  = "student_performance_analyzed.csv"
SUBJECTS = ["Python", "Mathematics", "Statistics", "Machine_Learning"]

# ─────────────────────────────────────────────
#  LOAD DATASET
# ─────────────────────────────────────────────

df = pd.read_csv(DATASET)

print("=" * 60)
print("   📊 STUDENT PERFORMANCE ANALYSIS REPORT")
print("=" * 60)

# ─────────────────────────────────────────────
#  1. BASIC INFO
# ─────────────────────────────────────────────

print("\n📋 DATASET OVERVIEW")
print("-" * 40)
print(f"  Total Students    : {len(df)}")
print(f"  Total Columns     : {len(df.columns)}")
print(f"  Columns           : {list(df.columns)}")
print(f"  Missing Values    : {df.isnull().sum().sum()}")
print(f"  Programs Offered  : {', '.join(df['Program'].unique())}")

print("\n  Students per Program:")
for prog, count in df["Program"].value_counts().items():
    print(f"    {prog}: {count} students")

# ─────────────────────────────────────────────
#  2. AVERAGE MARKS PER SUBJECT
# ─────────────────────────────────────────────

print("\n📚 AVERAGE MARKS PER SUBJECT")
print("-" * 40)
subject_means = df[SUBJECTS].mean().round(2)
for subject, avg in subject_means.items():
    bar = "█" * int(avg // 5)
    print(f"  {subject:<20}: {avg:>5}  {bar}")

overall_avg = subject_means.mean()
print(f"\n  Overall class average : {overall_avg:.2f}")

# ─────────────────────────────────────────────
#  3. ADD COMPUTED COLUMNS
# ─────────────────────────────────────────────

df["Total_Marks"]   = df[SUBJECTS].sum(axis=1)
df["Average_Marks"] = df[SUBJECTS].mean(axis=1).round(2)

def assign_grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 85: return "A"
    elif avg >= 80: return "A-"
    elif avg >= 75: return "B+"
    elif avg >= 70: return "B"
    elif avg >= 65: return "B-"
    elif avg >= 60: return "C"
    else: return "F"

df["Grade"]  = df["Average_Marks"].apply(assign_grade)
df["Status"] = df["Average_Marks"].apply(
    lambda x: "Pass" if x >= 60 else "Fail"
)

# ─────────────────────────────────────────────
#  4. TOP 5 PERFORMING STUDENTS
# ─────────────────────────────────────────────

print("\n🏆 TOP 5 PERFORMING STUDENTS")
print("-" * 40)
top5 = df.nlargest(5, "Average_Marks")[
    ["Student_ID", "Name", "Program", "Average_Marks", "Grade"]
].reset_index(drop=True)
top5.index += 1
print(top5.to_string())

# ─────────────────────────────────────────────
#  5. STUDENTS BELOW CLASS AVERAGE
# ─────────────────────────────────────────────

class_avg = df["Average_Marks"].mean()
below_avg = df[df["Average_Marks"] < class_avg][
    ["Student_ID", "Name", "Program", "Average_Marks", "Grade"]
].sort_values("Average_Marks")

print(f"\n⚠️  STUDENTS BELOW CLASS AVERAGE ({class_avg:.2f})")
print("-" * 40)
print(below_avg.to_string(index=False))
print(f"\n  Count: {len(below_avg)} out of {len(df)} students")

# ─────────────────────────────────────────────
#  6. SUBJECT-WISE INSIGHTS (NumPy)
# ─────────────────────────────────────────────

print("\n📈 SUBJECT-WISE INSIGHTS (NumPy)")
print("-" * 40)
for subj in SUBJECTS:
    arr = df[subj].to_numpy()
    print(f"  {subj:<20} | Mean: {np.mean(arr):.1f} | "
          f"Max: {np.max(arr)} | Min: {np.min(arr)} | "
          f"Std: {np.std(arr):.2f}")

# ─────────────────────────────────────────────
#  7. PROGRAM-WISE PERFORMANCE
# ─────────────────────────────────────────────

print("\n🏫 PROGRAM-WISE AVERAGE PERFORMANCE")
print("-" * 40)
prog_perf = df.groupby("Program")["Average_Marks"].mean().round(2).sort_values(ascending=False)
for prog, avg in prog_perf.items():
    print(f"  {prog}: {avg}")

# ─────────────────────────────────────────────
#  8. GRADE DISTRIBUTION
# ─────────────────────────────────────────────

print("\n🎓 GRADE DISTRIBUTION")
print("-" * 40)
grade_order = ["A+", "A", "A-", "B+", "B", "B-", "C", "F"]
grade_counts = df["Grade"].value_counts()
for grade in grade_order:
    if grade in grade_counts:
        count = grade_counts[grade]
        bar = "■" * count
        print(f"  {grade:>3}: {bar} ({count})")

pass_count = (df["Status"] == "Pass").sum()
print(f"\n  Pass: {pass_count}/{len(df)} students")

# ─────────────────────────────────────────────
#  9. ATTENDANCE ANALYSIS
# ─────────────────────────────────────────────

print("\n📅 ATTENDANCE ANALYSIS")
print("-" * 40)
print(f"  Average Attendance : {df['Attendance'].mean():.2f}%")
print(f"  Highest Attendance : {df['Attendance'].max()}% "
      f"({df.loc[df['Attendance'].idxmax(), 'Name']})")
print(f"  Lowest Attendance  : {df['Attendance'].min()}% "
      f"({df.loc[df['Attendance'].idxmin(), 'Name']})")

low_attendance = df[df["Attendance"] < 85][["Name", "Attendance"]]
if not low_attendance.empty:
    print(f"\n  Students with attendance < 85%:")
    for _, row in low_attendance.iterrows():
        print(f"    - {row['Name']} ({row['Attendance']}%)")

# ─────────────────────────────────────────────
#  10. SAVE ANALYZED DATASET
# ─────────────────────────────────────────────

df.to_csv(OUTPUT, index=False)
print(f"\n✅ Analyzed dataset saved to '{OUTPUT}'")
print(f"   New columns added: Total_Marks, Average_Marks, Grade, Status")

print("\n" + "=" * 60)
print("   Analysis Complete!")
print("=" * 60)
