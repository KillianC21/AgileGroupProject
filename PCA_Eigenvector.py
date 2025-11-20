import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Script to perform PCA on standardized numeric data and save eigenvectors

# ============================================================
# STEP 1: Load and Standardized Data
# ============================================================
data = pd.read_csv("personality_synthetic_dataset.csv")
X = data.select_dtypes(include=[np.number])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ============================================================
# STEP 2: Run PCA
# ============================================================
pca = PCA()
pca.fit(X_scaled)

# Eigenvalues and variance ratios
eigenvalues = pca.explained_variance_
variance_ratio = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(variance_ratio)

# ============================================================
# STEP 3: Eigenvector Table
# ============================================================
loadings = pd.DataFrame(
    pca.components_.T,
    index=X.columns,
    columns=[f"PC{i+1}" for i in range(pca.n_components_)]
)

print("\n=== Eigenvectors (Loadings) ===")
print(loadings.round(3))

# Save eigenvector table
loadings.to_csv("pca_eigenvectors.csv")
print("Saved eigenvector (loading) table to pca_eigenvectors.csv")
