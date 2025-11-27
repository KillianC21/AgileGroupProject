import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import cross_val_score, KFold, ShuffleSplit, cross_validate

# Load CSV
data = pd.read_csv("final_cleaned_dataset.csv")

# Convert one-hot columns into a single 3-class target
def map_personality(row):
    if row["personality_type_Extrovert"] == 1:
        return 1
    elif row["personality_type_Introvert"] == 1:
        return 2
    else:
        return 3
    
data["Personality"] = data.apply(map_personality, axis=1)

# data.to_csv("final_cleaned_dataset_with_personality.csv", index=False)

# ======== USE ALL FEATURES EXCEPT THE TARGET AND ONE-HOT COLUMNS ========
X = data.drop(columns=["personality_type_Extrovert","personality_type_Introvert","Personality"])
Y = data["Personality"]

# ===== K-FOLD ON TRAINING SET =====
model = tree.DecisionTreeClassifier()

shuffle_split = ShuffleSplit(n_splits=10, test_size=0.2, random_state=42)

kFold = KFold(n_splits=5, shuffle=True, random_state=42)

results = cross_validate(model, X, Y, cv=shuffle_split, scoring="accuracy", return_train_score=True)

average = results['test_score'].mean()
print(f"Average: {average}")

# extract separate train and test scores
test_scores = results['test_score']

print("Test Scores for each fold: ", test_scores)