import csv
from datetime import datetime
import os

PATIENT_FILE = "data/patients.csv"

HEADER = ["timestamp"] + [f"Q{i}" for i in range(1, 16)] + ["personality"]

def save_patient(scores, prediction):
    file_exists = os.path.exists(PATIENT_FILE) and os.path.getsize(PATIENT_FILE) > 0

    row = [datetime.now().isoformat()] + scores + [prediction]

    with open(PATIENT_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(HEADER)
        writer.writerow(row)
