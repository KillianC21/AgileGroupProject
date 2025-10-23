import pandas as pd
from sklearn.preprocessing import StandardScaler

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

categoricalCols = data.select_dtypes(include=['object', 'category']).columns
if len(categoricalCols) > 0:
    print("Categorical Columns Detected:")
    for col in categoricalCols:
        print(f"\n{col} value counts:")
        print(data[col].value_counts())
else:
    print("No categorical columns found.")
    
# ---------------------------------------------------------
# STEP 2: Encode categorical variables and scale numeric ones
# ---------------------------------------------------------

print("\n=== STEP 2: Encoding & Scaling ===")

# Identify categorical and numeric columns
categoricalCols = data.select_dtypes(include=['object', 'category']).columns
numericCols = data.select_dtypes(include=['int64', 'float64']).columns

print(f"Categorical columns: {list(categoricalCols)}")
print(f"Numeric columns: {list(numericCols)}\n")

# One-hot encode categorical columns
if len(categoricalCols) > 0:
    data = pd.get_dummies(data, columns=categoricalCols, drop_first=True)
    print("One-hot encoding applied.")
else:
    print("No categorical columns to encode.")

# Standardize numeric columns
if len(numericCols) > 0:
    scaler = StandardScaler()
    data[numericCols] = scaler.fit_transform(data[numericCols])
    print("StandardScaler applied (mean=0, std=1).")
else:
    print("No numeric columns to scale.")

# Save intermediate result
data.to_csv("processedStep2.csv", index=False)
print("Saved processed data into processedStep2.csv")