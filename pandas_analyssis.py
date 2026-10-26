
import pandas as pd
import numpy as np

# Create data
data = {
    "Name": ["Rahul", "Amit", "Shubham", "Rohit"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 99, 76]
}

# Convert data into a DataFrame (table)
df = pd.DataFrame(data)

# Display the complete table
print("Student Data:")
print(df)

# Calculate average marks
print("\nAverage Marks:", np.mean(df["Marks"]))

# Display students who scored more than 80
print("\nStudents scoring above 80:")
print(df[df["Marks"] > 80])
