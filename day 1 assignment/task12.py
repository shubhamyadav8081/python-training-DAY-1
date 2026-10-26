import numpy as np
import pandas as pd
from scipy import stats

# Create the dataset once for all tasks
np.random.seed(42)
n = 40
df = pd.DataFrame({
    "Student_ID": range(1, n + 1),
    "Branch": np.random.choice(["CSE", "ECE", "ME", "CE"], n),
    "Study_Hours": np.round(np.random.uniform(1, 8, n), 1),
    "Attendance": np.random.randint(55, 100, n),
})
df["Marks"] = np.clip(
    np.round(30 + 5 * df["Study_Hours"] + 0.2 * df["Attendance"]
             + np.random.normal(0, 6, n)),
    0, 100
).astype(int)

print("Dataset preview:")
print(df.head())
print("The average marks of students are:", df["Marks"].mean())
print("The median marks of students are:", df["Marks"].median())

study_corr = df["Marks"].corr(df["Study_Hours"])
attendance_corr = df["Marks"].corr(df["Attendance"])

print("Correlation between Marks and Study Hours:", round(study_corr, 2))
print("Correlation between Marks and Attendance:", round(attendance_corr, 2))

if abs(study_corr) > abs(attendance_corr):
    print("Study Hours has a stronger relationship with Marks.")
else:
    print("Attendance has a stronger relationship with Marks.")

print("The analysis helps us understand student performance.")
print("Correlation shows a relationship but does not prove causation.")