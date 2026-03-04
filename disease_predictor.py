import pandas as pd

disease_data = pd.read_csv('data/disease_symptoms_risk.csv')

def predict_disease(extracted_symptoms):
    extracted_set = set(symptom.lower() for symptom in extracted_symptoms)
    best_match = None
    max_overlap = 0

    for _, row in disease_data.iterrows():
        disease_symptoms = set(s.strip().lower() for s in row['symptoms'].split(','))
        overlap = len(extracted_set & disease_symptoms)
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = row

    if best_match is not None and max_overlap > 0:
        return {'disease': best_match['disease'], 'risk_factors': best_match['risk_factors']}
    else:
        return {'disease': 'Unknown', 'risk_factors': 'N/A'}
