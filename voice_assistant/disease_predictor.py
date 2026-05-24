import pandas as pd
import os

# Get absolute path of current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build correct path to dataset
DATA_PATH = os.path.join(BASE_DIR, 'data', 'disease_symptoms_risk.csv')

# Load dataset safely
try:
    disease_data = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    raise FileNotFoundError(f"Dataset not found at: {DATA_PATH}")

def predict_disease(extracted_symptoms):
    if not extracted_symptoms:
        return {'disease': 'Unknown', 'risk_factors': 'No symptoms provided'}

    extracted_set = set(symptom.lower().strip() for symptom in extracted_symptoms)

    best_match = None
    max_overlap = 0

    for _, row in disease_data.iterrows():
        # Handle missing values safely
        if pd.isna(row['symptoms']):
            continue

        disease_symptoms = set(
            s.strip().lower() for s in row['symptoms'].split(',')
        )

        overlap = len(extracted_set & disease_symptoms)

        if overlap > max_overlap:
            max_overlap = overlap
            best_match = row

    if best_match is not None and max_overlap > 0:
        return {
            'disease': best_match.get('disease', 'Unknown'),
            'risk_factors': best_match.get('risk_factors', 'N/A'),
            'match_score': max_overlap  # 🔥 added for debugging/improvement
        }
    else:
        return {
            'disease': 'Unknown',
            'risk_factors': 'N/A',
            'match_score': 0
        }
