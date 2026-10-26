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
t_stat, p_value = stats.ttest_1samp(df["Marks"], 60)

print("Null Hypothesis (H0): Average marks = 60")
print("Alternative Hypothesis (H1): Average marks != 60")

print("\nT-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Decision: Reject H0")
    print("Conclusion: Average marks are significantly different from 60.")
else:
    print("Decision: Fail to reject H0")
    print("Conclusion: There is not enough evidence that average marks differ from 60.")
