import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.decomposition import PCA

# Paths
PATIENT_FILE = "data/patients.csv"
MODEL_FILE = "models/model.pkl"
SCALER_FILE = "models/scaler.pkl"

# Trait columns (matches your mapping)
TRAIT_COLUMNS = [
    "social_energy","talkativeness","party_liking","leadership",
    "empathy","emotional_stability","curiosity","risk_taking",
    "stress_handling","adventurousness","travel_desire",
    "work_style_collaborative","decision_speed","sports_interest",
    "reading_habit"
]

PERSONALITY_LABELS = ["Extrovert", "Introvert", "Ambivert"]

def visualize_feature_importance() -> None:
    """Visualizes the importance of each feature in the personality prediction model.
    """
    try:
        with open(MODEL_FILE, "rb") as f:
            model = pickle.load(f)
    except:
        print("Model file not found. Train the model first.")
        return

    if not hasattr(model, "feature_importances_"):
        print("Model does not support feature_importances_.")
        return

    importances = model.feature_importances_
    sorted_idx = np.argsort(importances)[::-1]

    plt.figure(figsize=(10,6))
    plt.bar(range(len(TRAIT_COLUMNS)), importances[sorted_idx])
    plt.xticks(range(len(TRAIT_COLUMNS)), 
               [TRAIT_COLUMNS[i] for i in sorted_idx],
               rotation=45, ha="right")
    plt.ylabel("Importance Score")
    plt.title("Feature Importance in Personality Prediction")
    plt.tight_layout()
    plt.show()


def visualize_pca_clusters() -> None:
    """Visualizes PCA clusters of patient traits colored by personality type.
    """
    try:
        df = pd.read_csv(PATIENT_FILE)
    except:
        print("No patient data available.")
        return

    if df.shape[0] < 5:
        print("Not enough patients for PCA visualization.")
        return

    # Convert Q1…Q15 to trait names
    rename_map = {f"Q{i+1}": TRAIT_COLUMNS[i] for i in range(15)}
    df = df.rename(columns=rename_map)

    X = df[TRAIT_COLUMNS].values
    y = df["personality"].values

    pca = PCA(n_components=2)
    components = pca.fit_transform(X)

    plt.figure(figsize=(10,7))

    for label in np.unique(y):
        idx = (y == label)
        plt.scatter(components[idx,0], components[idx,1], label=label, s=70)

    plt.title("PCA Clusters of Patient Traits")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()


def visualize_trait_means() -> None:
    """Visualizes average trait scores by personality type.
    """
    try:
        df = pd.read_csv(PATIENT_FILE)
    except:
        print("No patient data available.")
        return

    rename_map = {f"Q{i+1}": TRAIT_COLUMNS[i] for i in range(15)}
    df = df.rename(columns=rename_map)

    groups = df.groupby("personality")[TRAIT_COLUMNS].mean().T

    plt.figure(figsize=(14,6))
    groups.plot(kind="bar", figsize=(14,6))
    plt.title("Average Trait Scores by Personality Type")
    plt.ylabel("Average Score")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
