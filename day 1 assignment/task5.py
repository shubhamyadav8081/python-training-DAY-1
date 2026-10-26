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
branch_avg = df.groupby("Branch")[["Marks", "Study_Hours"]].mean()

print("Average marks and study hours by branch:")
print(branch_avg)

# 2. Find the branch with the highest average marks
highest_branch = branch_avg["Marks"].idxmax()

print("\nBranch with the highest average marks:", highest_branch)
print("Highest average marks:", branch_avg.loc[highest_branch, "Marks"])

# 3. Display the top 5 students by marks
top_5 = df.sort_values(by="Marks", ascending=False).head(5)

print("\nTop 5 students by marks:")
print(top_5[["Student_ID", "Branch", "Marks"]])