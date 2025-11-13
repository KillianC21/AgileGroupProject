import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# ============================================================
# STEP 6: Full PCA Loading Heatmap
# ============================================================

# Read eigenvectors (loadings) from CSV
loadings = pd.read_csv("pca_eigenvectors.csv", index_col=0)

# OPTIONAL: limit number of PCs shown
loadings = loadings.iloc[:, :29]
loadings = loadings.dropna()

plt.figure(figsize=(30, 18))
sns.heatmap(
    loadings,
    cmap="coolwarm",
    center=0,
    annot=True,           
    square=True,
    cbar=True
)

plt.title("PCA Eigenvector (Loading) Heatmap", fontsize=16)
plt.xlabel("Principal Components", fontsize=12)
plt.ylabel("Original Variables", fontsize=12)
plt.tight_layout()
plt.savefig("loading_heatmap_full.png", dpi=300)
