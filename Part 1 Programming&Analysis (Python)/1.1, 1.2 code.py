# Importing useful Libraries
import csv
import pandas as pd
import numpy as np

# Now i will upload and make a CSV dataset
data = [
    ['ID', 'Name', 'Date_of_Birth', 'Salary', 'Department'],
    [1, 'John Doe', '1985-10-12', 50000, 'Finance'],
    [2, 'Jane Smith', 'not_available', 62000, 'Marketing'],
    [3, 'Emily Jones', '1990-04-15', 70000, 'Engineering'],
    [4, 'Michael Brown', '1975-02-20', 45000, 'HR'],
    ['', 'Sarah Davis', '1988-08-25', '', 'Sales'],
    [6, 'Peter Pan', '1983-07-21', 55000, 'Finance'],
    [7, 'Lily Evans', '1985/10/25', 1200000, 'HR'],
    [8, 'Tom Riddle', '1982-11-30', 31000, 'Marketing'],
    [9, 'Bruce Wayne', '1978-03-10', 75000, 'Finance'],
    [10, 'Clark Kent', '1979-12-01', 90000, 'Engineering'],
    [11, 'Diana Prince', '1984-05-19', 'not_applicable', 'Sales'],
    [12, 'Barry Allen', '1977-02-30', 1000000, 'Engineering'],
    [13, 'Arthur Curry', '1983-10-10', 65000, 'not_specified'],
    [14, 'Hal Jordan', '', 72000, 'HR'],
    [15, 'Victor Stone', '1989-11-15', -45000, 'Marketing'],
    [16, 'Lois Lane', '1980-08-20', 58000, 'Finance'],
    [17, 'James Gordon', '1975-09-15', 52000, 'HR'],
    [18, 'Selina Kyle', '1985-06-07', 'not_available', 'Sales'],
    [19, 'Oliver Queen', '1982-09-20', 1200000, 'Engineering'],
    [20, 'Roy Harper', '1988-07-10', '', 'Marketing']
]

filename = 'dataset.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Dataset saved successfully as '{filename}'.")

df = pd.read_csv('dataset.csv')
print(df)

#Investigate the dataset
print('now i will Investigate the dataset to know well about it and understand')
print(df.info())

# After I saw the information, I found that there are columns in a wrong type. Let's correct it
#Convert 'ID' column to integer
df['ID'] = df['ID'].astype('Int64') 

#Convert 'Date_of_Birth' column to datetime and Standardizing date format in 'date_column' to YYYY-MM-DD
df['Date_of_Birth'] = pd.to_datetime(df['Date_of_Birth'], errors='coerce').dt.strftime('%Y-%m-%d')

#Convert 'Salary' column to numeric
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

print("now we will see what it goes")
print(df.info())

print("see some statistical info")
print(df.describe())

print("See the size of data")
print(df.shape)

print("Inspect for duplicates")
print(df.duplicated().sum())

print("See if it have Null values")
null_values = df.isnull().any()
print(null_values)

print("Inspect for NULL values")
print(df.isna().sum())

#I see that there are null values in the dataset, in ID, Data of Birth, and Salary columns. i will Handle missing values one by one with explanations.

#First let's solve the null values in salary column by Calculateing the mean
mean_salary = df['Salary'].mean()

#Fill null values in the 'Salary' column with the mean salary
df['Salary'].fillna(mean_salary, inplace=True)

print("The explaination : In the salary column, i see that the optimal way to handle the null values is that calculate the mean, not just drop them because the salary column will be important element in my analysis.")

#Now i handle null values in ID column
#Second i will solve the null values in ID column by searching in it
missing_id_rows = df[df['ID'].isnull()]

# Print the results
if missing_id_rows.empty:
  print("No missing values found in the 'ID' column.")
else:
  print("Rows with missing IDs:")
  print(missing_id_rows)

# Now we know which ID is missed it is 5 because its index was 4
df['ID'].fillna(5, inplace=True)

print("Explaination : in the ID column, we all know that the ID is a unique number for each, so I searched for the missing number, and it appears in index 4, so it will be number 5, because in Python the index starts from 0, so 4 in Python equals 5 in numbers.")

#Now i handle null values in date of birth column
# Now we will fill it with default number instead of drop it 
df['Date_of_Birth'].fillna('1900-01-01', inplace=True)

print(" Explaination : And in the data of birth column, I filled it with a default because I will use this column less in my analysis, and this is more effective than dropping it.")

print("So I handled missing values column by column because, in this case, I saw that every column needed a different approach. instead of dealing with the null values together.")

# check the df
print(df)

# I see negative values in salary and it's not logcally, so we solve this by using the absolute
df['Salary'] = df['Salary'].abs()

#Now i will search for outliers in my dataset to Identify using statistical method : interquartile range (IQR).
#Calculate the IQR boundaries
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]
print(outliers)

#I Will treat outliers now by applying the log transformation in numpy
# Apply log transformation to handle outliers
df['Salary'] = np.log1p(df['Salary'])

#check it again
outliers = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]
print(outliers)

print("Now I treated the outliers in my dataset successfully.")

# Investigate my department searching for an illogical data
df['Department'].value_counts()

# I See that there a row has no department and not specified. i will replace it with right deprtment by this way.
df = pd.DataFrame(df)

# Count current number of employees per department
department_counts = df['Department'].value_counts()

# Identify departments with less than 4 employees
departments_to_adjust = department_counts[department_counts < 4].index.tolist()

# Add an employee to each department with less than 4 employees
for department in departments_to_adjust:
    # Find the first employee with 'not_specified' department and change it
    idx = df[df['Department'] == 'not_specified'].index[0]
    df.at[idx, 'Department'] = department
    break

# Display the updated department counts
updated_department_counts = df['Department'].value_counts()
print(updated_department_counts)

print(df)

print('Now the data set is clean and preprocess well, ready for analysis')

print('After we cleaned the dataset, we will do some Aggregation and analysis to gain useful insights')

# Calculate the average salary per department
avg_salary_per_dept = df.groupby('Department')['Salary'].mean()
print("Average Salary per Department:")
print(avg_salary_per_dept)

# Find the top 3 highest paid employees
top_3_highest_paid = df.nlargest(3, 'Salary')
print("Top 3 Highest Paid Employees:")
print(top_3_highest_paid)

# Determine the number of employees in each department
num_employees_per_dept = df['Department'].value_counts()
print("Number of Employees in Each Department:")
print(num_employees_per_dept)

print('Now I\'ve done some analysis and aggregation to gain useful insight, we can use this insights for decision making for example.')

# Now I will save the cleaned dataset into another CSV to re-use it in Flask-APP.
df.to_csv('clean_dataset.csv', index=False)
print("Dataset saved successfully as clean_dataset.csv")

