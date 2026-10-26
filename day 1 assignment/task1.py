import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "student id": [1, 2, 3, 4, 5],
    "marks": [85, 65, 35, 95, 50]
})

def get_grade(marks):
    if marks >= 75:
        return 'A'
    elif marks >= 60:
        return 'B'
    elif marks >= 40:
        return 'C'
    else:
        return 'F'

print(get_grade(60))
print(get_grade(12))
print(get_grade(95))
print(get_grade(50))

df["grade"] = df["marks"].apply(get_grade)

print(df[["student id", "marks", "grade"]].head())

print(df["grade"].value_counts())