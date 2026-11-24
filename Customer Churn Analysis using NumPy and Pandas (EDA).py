import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("churn.csv")

# Display data
print(df.head())

# Remove duplicate values
df = df.drop_duplicates()

# Handle missing values
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].mean())

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Summary statistics
print("\nSummary:")
print(df.describe())

# Churn analysis
if "Churn" in df.columns:
    print("\nChurn Count:")
    print(df["Churn"].value_counts())

    df["Churn"].value_counts().plot(kind="bar")
    plt.title("Customer Churn Analysis")
    plt.xlabel("Churn")
    plt.ylabel("Customers")
    plt.show()

# Correlation
print("\nCorrelation:")
print(df.select_dtypes(include="number").corr())

print("EDA Completed")
