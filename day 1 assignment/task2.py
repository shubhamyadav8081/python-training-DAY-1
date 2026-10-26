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
low_attendance_marks = [
    marks for marks, attendance in zip(df["Marks"], df["Attendance"])
    if attendance < 75
]
print("Marks of students with attendance below 75:")
print(low_attendance_marks)

# 2. Filter and lambda: marks above 70
high_marks = list(filter(lambda x: x > 70, df["Marks"]))
print("\nMarks above 70:")
print(high_marks)
grace_marks = list(map(lambda x: min(x + 5, 100), df["Marks"]))
print("\nMarks after adding grace marks:")
print(grace_marks)

