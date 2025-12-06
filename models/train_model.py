import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

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
    print("\n=== Training Model ===")

    data = pd.read_csv(DATA_FILE)

    X = data[FEATURE_COLS]
    y = data.apply(get_target_label, axis=1)

    # Train-test split (20% test set)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Fit scaler only on training data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Random Forest Model
    model = RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        class_weight="balanced"
    )

    model.fit(X_train_scaled, y_train)

    # Print class balance for debugging
    # print("Class balance:")
    # print(y.value_counts())
    # print()
    
    # Debugging: print feature stats
    # print("Feature means in dataset:", X.mean().values)
    # print("Feature mins in dataset:", X.min().values)
    # print("Feature max in dataset:", X.max().values)

    # ---- ACCURACY RESULTS ----
    train_preds = model.predict(X_train_scaled)
    test_preds = model.predict(X_test_scaled)

    train_acc = accuracy_score(y_train, train_preds)
    test_acc = accuracy_score(y_test, test_preds)

    print("\n=== Model Performance ===")
    print(f"Training Accuracy: {train_acc:.4f}")
    print(f"Test Accuracy:      {test_acc:.4f}")

    # Save model + scaler
    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)

    with open(SCALER_FILE, "wb") as f:
        pickle.dump(scaler, f)

    print("\nModel and scaler trained + saved successfully!")

if __name__ == "__main__":
    train()
