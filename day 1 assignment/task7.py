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
marks = df["Marks"]

print("Mean:", marks.mean())
print("Median:", marks.median())
print("Mode:", list(marks.mode()))
print("Variance:", marks.var())
print("Standard deviation:", marks.std())
print("Minimum:", marks.min())
print("Maximum:", marks.max())

Q1 = marks.quantile(0.25)
Q3 = marks.quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower limit:", lower_limit)
print("Upper limit:", upper_limit)

outliers = marks[
    (marks < lower_limit) | (marks > upper_limit)
]

print("Outliers:", list(outliers))

print("\nExplanation:")
print("Mean shows the average marks of the class.")
print("Median shows the middle value of the marks.")
print("Standard deviation shows how much marks vary from the mean.")
