import pandas as pd

# =========================================================
# STEP 1: Load and Inspect Dataset
# =========================================================
print("=== STEP 1: Load and Inspect Dataset ===")

file_path = "personality_synthetic_dataset.csv"
data = pd.read_csv(file_path)

print(f"Data Loaded: {data.shape[0]} rows, {data.shape[1]} columns\n")
print("First 5 Rows:")
print(data.head(), "\n")

print("Data Types & Missing Values:")
print(data.info(), "\n")

print("Descriptive Statistics (Numerical):")
print(data.describe().T, "\n")

categorical_cols = data.select_dtypes(include=['object', 'category']).columns
if len(categorical_cols) > 0:
    print("Categorical Columns Detected:")
    for col in categorical_cols:
        print(f"\n{col} value counts:")
        print(data[col].value_counts())
else:
    print("No categorical columns found.")