import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

DATA_FILE = "data/final_cleaned_dataset.csv"
MODEL_FILE = "models/model.pkl"
SCALER_FILE = "models/scaler.pkl"

FEATURE_COLS = [
    "social_energy","talkativeness","party_liking","leadership",
    "empathy","emotional_stability","curiosity","risk_taking",
    "stress_handling","adventurousness","travel_desire",
    "work_style_collaborative","decision_speed","sports_interest",
    "reading_habit"
]

TARGET_COLS = ["personality_type_Extrovert", "personality_type_Introvert"]

def get_target_label(row):
    if row["personality_type_Extrovert"] == 1:
        return 0   # Extrovert
    elif row["personality_type_Introvert"] == 1:
        return 1   # Introvert
    else:
        return 2   # Ambivert

def train():
    # Load dataset
    data = pd.read_csv(DATA_FILE)

    # Features & target
    X = data[FEATURE_COLS]
    y = data.apply(get_target_label, axis=1)

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # RandomForest Model
    model = RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        class_weight="balanced"
    )
    
    # Print class balance for debugging
    # print("Class balance:")
    # print(y.value_counts())
    # print()
    
    # Debugging: print feature stats
    # print("Feature means in dataset:", X.mean().values)
    # print("Feature mins in dataset:", X.min().values)
    # print("Feature max in dataset:", X.max().values)


    # Train model
    model.fit(X_scaled, y)

    # Save model + scaler
    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)

    with open(SCALER_FILE, "wb") as f:
        pickle.dump(scaler, f)

    print("Model and scaler trained + saved successfully!")

if __name__ == "__main__":
    train()
