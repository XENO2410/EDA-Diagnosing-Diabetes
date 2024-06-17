# Diabetes Diagnostic Factors Analysis

## Project Overview

This project aims to explore and analyze a dataset from the National Institute of Diabetes and Digestive and Kidney Diseases. The dataset contains diagnostic factors that may affect the diabetes outcome of women patients. By using Exploratory Data Analysis (EDA) techniques, we will inspect, clean, and validate the data to gain insights into how these factors influence the likelihood of diabetes.

## Dataset Information

The dataset contains the following columns:

- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration at 2 hours in an oral glucose tolerance test
- **BloodPressure**: Diastolic blood pressure (mm Hg)
- **SkinThickness**: Triceps skinfold thickness (mm)
- **Insulin**: 2-Hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)^2)
- **DiabetesPedigreeFunction**: Diabetes pedigree function (a function that scores likelihood of diabetes based on family history)
- **Age**: Age (years)
- **Outcome**: Class variable (0 if non-diabetic, 1 if diabetic)

## Project Steps

1. **Loading the Dataset**:
   - The dataset is loaded using pandas' `read_csv` function.

2. **Initial Exploration**:
   - Determine the number of columns and rows.
   - Identify missing values in the dataset.
   - Get a concise summary of the dataset.
   - Obtain summary statistics.

3. **Value Counts and Outliers**:
   - Use `.value_counts()` to explore the distribution of values in each column.
   - Investigate potential outliers, specifically zero values in the `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, and `BMI` columns.

4. **Handling Missing Values**:
   - Replace zero values in the specified columns with the median of each column to better reflect realistic measurements.

5. **Rechecking Data**:
   - After handling missing values, recheck the dataset for any further anomalies.
   - Print the updated summary statistics and data types.
