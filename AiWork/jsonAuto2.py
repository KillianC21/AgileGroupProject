import pandas as pd
import json
import os

# Paths
csv_file = "personality_synthetic_dataset_cleaned.csv"
output_folder = "/Users/conor-a4/Desktop/College/Y3S1/Agile/Project"
os.makedirs(output_folder, exist_ok=True)
json_file = os.path.join(output_folder, "personality_input_output.json")

# Read CSV
df = pd.read_csv(csv_file)

# Convert each row to {"input": "...", "output": "..."}
records = []
# all except the personality_type column
feature_columns = df.columns.tolist()[1:]

for _, row in df.iterrows():
    # Create the "input" string
    input_str = "\n".join(
        [f"{col}: {row[col]:.2f}" for col in feature_columns])
    records.append({
        "input": input_str,
        "output": row["personality_type"]
    })

# Save as JSON
with open(json_file, "w") as f:
    json.dump(records, f, indent=4)

print(f"CSV converted to input/output JSON at {json_file}!")
