# -*- coding: utf-8 -*-
"""HypothesisTesting.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13WLwUXkoQRsNvn0ievFYvHy6faRlRWge
"""

# Hypothesis Testing
# List of categorical columns based on the dataset description
categorical_columns = [
    'BusinessTravel', 'Department', 'Education', 'EducationField', 'EnvironmentSatisfaction',
    'Gender', 'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction',
    'MaritalStatus', 'OverTime', 'PerformanceRating', 'RelationshipSatisfaction',
    'StockOptionLevel', 'WorkLifeBalance'
]

# Ensure 'Attrition' is in the categorical_columns list
categorical_columns = [col for col in categorical_columns if col in df.columns]

# Create a function to reverse one-hot encoding for chi-square tests
def reverse_one_hot_encoding(df, prefix):
    one_hot_columns = [col for col in df.columns if col.startswith(prefix)]
    return df[one_hot_columns].idxmax(axis=1).apply(lambda x: x.replace(prefix, '').strip())

# Dictionary to store results
results = {}

# Perform chi-square test for each categorical variable against 'Attrition'
for col in categorical_columns:
    if col in df.columns:
        print(f"Performing chi-square test for column: {col}")
        contingency_table = pd.crosstab(df['Attrition'], df[col])
        chi2, p, dof, expected = chi2_contingency(contingency_table)
        results[col] = {'chi2': chi2, 'p-value': p}
    else:
        # Handling one-hot encoded columns
        one_hot_df = reverse_one_hot_encoding(df, col)
        contingency_table = pd.crosstab(df['Attrition'], one_hot_df)
        chi2, p, dof, expected = chi2_contingency(contingency_table)
        results[col] = {'chi2': chi2, 'p-value': p}

# Print results
print("Chi-square test results:")
for col, result in results.items():
    print(f"Chi-square test between Attrition and {col}:")
    print(f"  Chi2 value: {result['chi2']:.2f}")
    print(f"  p-value: {result['p-value']:.4f}")
    if result['p-value'] < 0.05:
        print("  Result: Statistically significant (Reject null hypothesis)")
    else:
        print("  Result: Not statistically significant (Fail to reject null hypothesis)")
    print()