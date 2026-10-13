import pandas as po 
# load the dataset 
table = po.read_csv("students.csv")
# print(table)
# display the first 5 rows
print(table.head())
# print number of rows and column
print(table.shape)
# Select name and gpa 
print(table[["name", "GPA"]])
# find students with gpa >= 3.5
print(table[table["GPA"] >= 3.5][["name", "GPA"]])
# sort students by gpa 
print(table.sort_values(by = "GPA"))
# find the average GPA by major 
print(table.groupby("major")["GPA"].mean())

table2 = po.read_csv("scores.csv")
# check missing value 
print(table.isna().sum())
print(table2.isna().sum())
# fill or remove missing values appropriately
table_clean = table.dropna()
print(table_clean)    

table_filled = table.fillna(0)
print(table_filled)
# merge 2 datasets
combined_dataset = po.merge(table, table2, on = "student_id")
# calculate the avergae of students score
combined_dataset["average_score"] = combined_dataset[["python", "math", "database"]].mean(axis = 1)
print(combined_dataset[["student_id", "name", "average_score"]])
# find the top 5 students
top_5 = combined_dataset.sort_values(by = "average_score", ascending = False).head(5)
print(top_5)
# compute avg score by major 
print(combined_dataset.groupby("major")["average_score"].mean())