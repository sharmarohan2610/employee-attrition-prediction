# -*- coding: utf-8 -*-
"""DataCleaning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o5BalTWsVGxbpDH6W9kHeg6JXHceDnUG
"""

# a. Introduction
print("Introduction: Analyzing the factors behind employee attrition")

# b. Data Cleaning/Preparation
# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Drop columns that won't be used for analysis
df.drop(['EmployeeNumber', 'EmployeeCount', 'Over18', 'StandardHours'], axis=1, inplace=True)

# Encode 'Attrition' column
df['Attrition'] = df['Attrition'].map({'No': 0, 'Yes': 1})

# Encode other categorical variables
categorical_columns = df.select_dtypes(include=['object']).columns
df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

# Check the first few rows of the dataframe
print(df.head())