import re

def load_symptoms(file_path='data/symptoms_multilang.txt'):
    symptoms_dict = {'en': [], 'hi': [], 'te': []}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line or '|' not in line:
                continue
            lang, symptom = line.split('|', 1)
            symptoms_dict[lang].append(symptom)
    return symptoms_dict

def extract_symptoms(text, symptoms_list):
    text = text.lower()
    found_symptoms = []
    for symptom in symptoms_list:
        if re.search(re.escape(symptom.lower()), text):
            found_symptoms.append(symptom)
    return found_symptoms
