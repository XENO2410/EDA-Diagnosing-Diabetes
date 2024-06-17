import pandas as pd
import numpy as np

# Load the dataset from a CSV file
diabetes_data = pd.read_csv('diabetes.csv')

# Print the number of columns in the DataFrame
print("Number of columns:", len(diabetes_data.columns))

# Print the number of rows in the DataFrame
print("Number of rows:", len(diabetes_data))

# Print the number of missing values in each column
print("Missing values in each column:")
print(diabetes_data.isnull().sum())

# Print a concise summary of the DataFrame, including the data types and non-null values
print("\nDataFrame info before handling missing values:")
print(diabetes_data.info())

# Print summary statistics of the DataFrame
print("\nSummary statistics before handling missing values:")
print(diabetes_data.describe())

# Use .value_counts() to explore the values in each column
print("\nValue counts for each column:")
for column in diabetes_data.columns:
    print(f"\n{column}:")
    print(diabetes_data[column].value_counts())

# Investigate other outliers (values that might be easily overlooked)
# Here, I'm printing the rows where Glucose, BloodPressure, SkinThickness, Insulin, or BMI is 0
outliers = diabetes_data[(diabetes_data['Glucose'] == 0) |
                         (diabetes_data['BloodPressure'] == 0) |
                         (diabetes_data['SkinThickness'] == 0) |
                         (diabetes_data['Insulin'] == 0) |
                         (diabetes_data['BMI'] == 0)]
print("\nRows with outliers (0 values in specified columns):")
print(outliers)

# Replace 0 values in specified columns with the median of each column
columns_to_replace = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
for column in columns_to_replace:
    median_value = diabetes_data[column].median()
    diabetes_data[column] = diabetes_data[column].replace(0, median_value)

# Print the number of missing values in each column after the replacement
print("\nMissing values in each column after replacing zeros with median:")
print(diabetes_data.isnull().sum())

# Print the concise summary of the DataFrame again to see changes
print("\nDataFrame info after handling missing values:")
print(diabetes_data.info())

# Print the entire DataFrame (if necessary, you can comment this out to avoid large output)
# print(diabetes_data)

# Print the data types of each column
print("\nData types of each column:")
print(diabetes_data.dtypes)

# Print the concise summary of the DataFrame again to see changes
print("\nDataFrame info after handling missing values:")
print(diabetes_data.info())

# Print summary statistics after replacing zeros with median
print("\nSummary statistics after handling missing values:")
print(diabetes_data.describe())
