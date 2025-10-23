import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

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

# ---------------------------------------------------------
# STEP 3: Detect and handle outliers using z-score
# ---------------------------------------------------------

print("\n=== STEP 3: Outlier Detection & Handling ===")

numeric_cols = data.select_dtypes(include=[np.number]).columns

# Calculate z-scores
z_scores = np.abs(stats.zscore(data[numeric_cols]))
outlier_threshold = 3  # Common threshold for z-score
outliers = (z_scores > outlier_threshold)

# Count outliers per row
outlier_ratio = outliers.sum(axis=1) / len(numeric_cols)

# Rule: if >50% outliers in a row → drop it
rows_to_drop = outlier_ratio > 0.5
print(f"Rows with >50% outliers: {rows_to_drop.sum()}")

data = data[~rows_to_drop].copy()

# Replace remaining outliers with mean (or median)
for col in numeric_cols:
    col_z = z_scores[:, list(numeric_cols).index(col)]
    mask = col_z > outlier_threshold
    if mask.sum() > 0:
        mean_val = data[col].mean()
        data.loc[mask, col] = mean_val

print("Outlier complete.")

# Save intermediate file
data.to_csv("processed_step3.csv", index=False)
print("Saved dataset after outlier handling to processed_step3.csv")

# Labels overlapping each other in boxplot -> solution - stacked hortizonal bar char or box plot for each column
# plt.boxplot(data[numeric_cols].values, labels=numeric_cols)
# plt.title("Boxplot after Outlier Handling")
# plt.show()

# ---------------------------------------------------------
# STEP 4: Remove duplicates and analyze correlations
# ---------------------------------------------------------

print("\n=== STEP 4: Duplicates & Correlation Analysis ===")

# Remove duplicate rows
duplicates = data.duplicated().sum()
print(f"Found {duplicates} duplicate rows.")
if duplicates > 0:
    data.drop_duplicates(inplace=True)
    print("Duplicates removed.")

# Correlation matrix
corr = data.corr(numeric_only=True)
print("\nCorrelation matrix calculated.")

# Optional: visualize correlation heatmap
plt.figure(figsize=(10, 8))
for col in corr.columns:
    plt.scatter(data.index, data[col], label=col, alpha=0.7)
plt.title("Feature Scatterplot")
plt.xlabel("Index")
plt.ylabel("Values")
plt.legend()
plt.tight_layout()
plt.savefig("scatterplot.png")
plt.close()
print("Saved correlation scatterplot to scatterplot.png")

# ---------------------------------------------------------
# STEP 5: PCA feature reduction
# ---------------------------------------------------------

print("\n=== STEP 5: PCA Feature Reduction ===")

# Run PCA keeping up to 21 components
pca = PCA(n_components=min(21, data.shape[1]))
reduced_data = pca.fit_transform(data)

print(f"PCA complete. Reduced to {reduced_data.shape[1]} components.")

# Create DataFrame for PCA results
pca_df = pd.DataFrame(reduced_data, columns=[f"PC{i+1}" for i in range(reduced_data.shape[1])])

# Save PCA result
pca_df.to_csv("processed_step5_pca.csv", index=False)
print("Saved PCA-reduced dataset → processed_step5_pca.csv")

# ---------------------------------------------------------
# STEP 6: Finalize cleaned dataset
# ---------------------------------------------------------
print("\n=== STEP 6: Finalizing Dataset ===")
final_path = "final_cleaned_dataset.csv"
pca_df.to_csv(final_path, index=False) # write the DataFrame into the final csv file excluding pandas row numbers
print(f"All preprocessing complete! Final dataset saved → {final_path}")