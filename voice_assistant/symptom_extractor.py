import re
import os

def load_symptoms(file_path='data/symptoms_multilang.txt'):
    # Get correct absolute path
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(BASE_DIR, file_path)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Symptoms file not found at: {full_path}")

    symptoms_dict = {'en': [], 'hi': [], 'te': []}

    with open(full_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            # Skip empty or invalid lines
            if not line or '|' not in line:
                continue

            try:
                lang, symptom = line.split('|', 1)
                lang = lang.strip()
                symptom = symptom.strip()

                if lang in symptoms_dict:
                    symptoms_dict[lang].append(symptom)
            except ValueError:
                continue  # skip malformed lines

    return symptoms_dict


def extract_symptoms(text, symptoms_list):
    if not text:
        return []

    text = text.lower()
    found_symptoms = []

    for symptom in symptoms_list:
        symptom_clean = symptom.lower().strip()

        # Match whole words (avoids partial match issues)
        pattern = r'\b' + re.escape(symptom_clean) + r'\b'

        if re.search(pattern, text):
            found_symptoms.append(symptom)

    return found_symptoms
