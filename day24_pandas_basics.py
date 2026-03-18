# Day 24: Pandas DataFrames
# loading data labels and creating Series and DataFrames

import pandas as pd

# creating pandas labels index series
data_list = [100, 200, 300]
labels = ['a', 'b', 'c']
series = pd.Series(data=data_list, index=labels)
print("Series:\n", series)

# loading DataFrame from dictionaries
student_dict = {
    "Name": ["Kartik", "Amit", "Sara"],
    "Age": [22, 23, 21],
    "Score": [95, 88, 92]
}
df = pd.DataFrame(student_dict)
print("\nDataFrame:\n", df)

# print columns
print("\nNames column:", df["Name"])

# matrix sizes and stats
print("\nShape:", df.shape)
print("\nDescription Stats:\n", df.describe())

# exercise 1: filtering rows
filtered_df = df[df["Age"] > 21]
print("\nFiltered (Age > 21):\n", filtered_df)

# challenge: adding binary passed column
df["Passed"] = df["Score"] >= 90
print("\nPassed column updated:\n", df)
