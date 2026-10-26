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

confidence_interval = stats.t.interval(
    confidence=0.95,
    df=len(marks) - 1,
    loc=marks.mean(),
    scale=stats.sem(marks)
)

print("Mean Marks:", marks.mean())
print("95% Confidence Interval:", confidence_interval)

print("\nExplanation:")
print("We are 95% confident that the true population average marks lie within this interval.")
