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


# ============ TASK 1 ============



# Task 1: Grading function
# •	Write a function get_grade(marks) that returns "A" for 75 and above, "B" for 60 to 74, "C" for 40 to 59, and "F" below 40.
# •	Add a Grade column to df using apply().
# •	Show how many students got each grade using value_counts().
def get_grade(marks):
    if marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

# Add a Grade column using apply()
df["Grade"] = df["Marks"].apply(get_grade)

# Display the students with their marks and grades
print(df[["Student_ID", "Marks", "Grade"]])

# Count students in each grade
print(df["Grade"].value_counts())



# ============ TASK 2 ============



# Task 2: Comprehensions and lambda
# •	Using a list comprehension, create a list of marks of students whose attendance is below 75.
# •	Using filter() and a lambda, get all marks above 70.
# •	Using map() and a lambda, add 5 grace marks to every student's marks (the maximum must stay 100).

# Task 2: Comprehensions and Lambda

# 1. List comprehension: marks of students with attendance below 75
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


# 3. Map and lambda: add 5 grace marks, maximum 100
grace_marks = list(map(lambda x: min(x + 5, 100), df["Marks"]))
print("\nMarks after adding grace marks:")
print(grace_marks)


# ============ TASK 3 ============


# Task 3: Flexible functions 
# • Write a function summary(*values, round_to=2) that accepts any number of values and returns a dictionary with the count, minimum, maximum and average. 
# • Test it with summary(10, 20, 30) and with summary(*df["Marks"]).

def summary(*values, round_to=2):

    #handle empty input
    if len (values) == 0:
        return {"count": 0, "min": None, "max": None, "average": None}
    results = {
        "Count": len(values),
        "Min": min(values),
        "Max": max(values),
        "Average": round(sum(values) / len(values), round_to)
    }
    return results

#test 1 
print (summary(10, 20, 30))

#test 2
print(summary(*df["Marks"]))

# ============ TASK 4 ============


# Task 4: Safe file handling 
# • Save df to a file named students.csv using to_csv(index=False). 
# • Write a function load_data(filename) that reads a CSV file using try and except. If the file is not found, it should print a friendly message instead of crashing. 
# • Test it once with the correct file name and once with a wrong name. 

# 1. Save the DataFrame to a CSV file
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

# ============ TASK 5 ============


# Task 5: Grouping with Pandas 
# • Find the average Marks and average Study_Hours for each Branch using groupby(). 
# • Which branch has the highest average marks? 
# • Display the top 5 students by marks using sort_values(). 

# 1. Calculate average marks and study hours for each branch
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

# ============ TASK 6 ============


# Task 6: Fast calculations with NumPy
# Convert Marks column to NumPy array
# Calculate z-score of every student without loop
# Count students with z-score greater than 1

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

# ============ TASK 7 ============


# Task 7: Describing the marks
# Calculate mean, median, mode, variance, standard deviation,
# minimum, maximum, quartiles and outliers

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


# ============ TASK 8 ============


# Task 8: Correlation
# Find correlation of Marks with Study_Hours and Attendance

study_corr = df["Marks"].corr(df["Study_Hours"])
attendance_corr = df["Marks"].corr(df["Attendance"])

print("Correlation between Marks and Study Hours:", study_corr)
print("Correlation between Marks and Attendance:", attendance_corr)

if abs(study_corr) > abs(attendance_corr):
    print("\nStudy Hours has the stronger relationship with Marks.")
else:
    print("\nAttendance has the stronger relationship with Marks.")

print("Correlation is positive if both variables tend to increase together.")
print("Correlation does not prove causation because other factors may affect both variables.")

# ============ TASK 9 ============


# Task 9: Confidence interval
# Calculate 95% confidence interval for average marks

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

# ============ TASK 10 ============


# Task 10: Hypothesis test on one group
# Department claims that average marks are 60

# H0: Average marks are equal to 60
# H1: Average marks are not equal to 60

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

# ============ TASK 11 ============


# Task 11: Hypothesis test on two groups
# Compare marks of CSE and ECE students

# H0: Average marks of CSE and ECE are equal
# H1: Average marks of CSE and ECE are different

cse_marks = df[df["Branch"] == "CSE"]["Marks"]
ece_marks = df[df["Branch"] == "ECE"]["Marks"]

print("CSE Students:", len(cse_marks))
print("ECE Students:", len(ece_marks))

print("CSE Average Marks:", cse_marks.mean())
print("ECE Average Marks:", ece_marks.mean())

t_stat, p_value = stats.ttest_ind(
    cse_marks,
    ece_marks,
    equal_var=False
)

print("\nT-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Decision: Reject H0")
    print("Conclusion: There is a significant difference between the two groups.")
else:
    print("Decision: Fail to reject H0")
    print("Conclusion: There is not enough evidence of a significant difference.")

# ============ TASK 12 ============


# Task 12: Summary
# Summarise the analysis in 4 to 5 lines

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