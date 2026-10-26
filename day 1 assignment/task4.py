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
df.to_csv("students.csv", index=False)
print("Data saved successfully!")

# 2. Function to load data safely
def load_data(filename):
    try:
        data = pd.read_csv(filename)
        print("File loaded successfully!")
        return data

    except FileNotFoundError:
        print("Error: File not found. Please check the filename.")
        return None

# 3. Test with the correct filename
data = load_data("students.csv")
print(data)

# 4. Test with an incorrect filename
data2 = load_data("wrong.csv")
