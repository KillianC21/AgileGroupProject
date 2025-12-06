import numpy as np
import pickle
import pandas as pd

MODEL_FILE = "models/model.pkl"
SCALER_FILE = "models/scaler.pkl"

FEATURE_COLS = [
    "social_energy","talkativeness","party_liking","leadership",
    "empathy","emotional_stability","curiosity","risk_taking",
    "stress_handling","adventurousness","travel_desire",
    "work_style_collaborative","decision_speed","sports_interest",
    "reading_habit"
]

# min/max values from training data
TRAIN_MINS = np.array([
    -2.23182875, -2.22109292, -1.79330234, -2.7778684, -2.96949259,
    -2.99646292, -2.999315, -2.2839018, -2.99976975, -2.28463731,
    -2.85136788, -2.98849313, -2.83723128, -2.84337494, -2.73659601
])

TRAIN_MAXS = np.array([
    1.81927284, 1.79828992, 1.76479275, 1.83617292, 2.29125186,
    2.67470163, 2.26906164, 2.2730209, 2.69613255, 2.25403183,
    2.324529, 1.85106086, 2.30625122, 2.33346684, 1.86985163
])

LABELS = ["Extrovert", "Introvert", "Ambivert"]

def load_model_and_scaler() -> tuple:
    """Loads the trained model and scaler from disk.

    Returns:
        tuple: Tuple containing the model and scaler
    """
    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)

    with open(SCALER_FILE, "rb") as f:
        scaler = pickle.load(f)

    return model, scaler

def map_questionnaire_values(raw_scores: list) -> np.ndarray:
    """input scores are 1-10, map them to training data distribution

    Args:
        raw_scores (list): List of raw scores from 1 to 10

    Returns:
        np.ndarray: Mapped scores in the training data distribution range
    """
    raw_scores = np.array(raw_scores)
    normalized = (raw_scores - 1) / 9  # map to 0–1
    mapped = TRAIN_MINS + normalized * (TRAIN_MAXS - TRAIN_MINS)
    return mapped

def predict_personality(scores_15: list) -> str:
    """Predict personality type based on 15 questionnaire scores.

    Args:
        scores_15 (list): List of 15 raw scores from 1 to 10

    Returns:
        str: Predicted personality type ("Extrovert", "Introvert", "Ambivert")
    """
    model, scaler = load_model_and_scaler()

    # Map scores so they resemble training distribution
    mapped_scores = map_questionnaire_values(scores_15)

    df = pd.DataFrame([mapped_scores], columns=FEATURE_COLS)
    scaled = scaler.transform(df)

    prediction = model.predict(scaled)[0]
    return LABELS[prediction]
