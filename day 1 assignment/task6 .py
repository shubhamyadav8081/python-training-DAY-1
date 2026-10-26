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
marks_array = df["Marks"].to_numpy()

mean_marks = np.mean(marks_array)
std_marks = np.std(marks_array)

z_scores = (marks_array - mean_marks) / std_marks

print("Marks as NumPy array:")
print(marks_array)

print("\nZ-scores:")
print(np.round(z_scores, 2))

count = np.sum(z_scores > 1)

print("\nStudents with z-score greater than 1:", count)
