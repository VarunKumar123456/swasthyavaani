def generate_explanation_and_prevention(disease_name):
    # Mock simple static examples; in production, this would use a real GenAI model or API
    explanations = {
        'Flu': "Flu is a viral infection that causes fever, headache, and cough. It spreads easily from person to person.",
        'Migraine': "Migraine is a type of headache characterized by intense pain, often accompanied by nausea and light sensitivity.",
        'Common Cold': "Common cold is a mild viral infection causing cough, sore throat, and congestion.",
        'COVID-19': "COVID-19 is a contagious respiratory disease caused by the SARS-CoV-2 virus.",
        'Viral Infection': "Viral infections are caused by viruses attacking the body, leading to fever, body pain, and fatigue.",
        'Unknown': "Unable to provide explanation for unknown disease."
    }

    preventions = {
        'Flu': "Wash hands regularly, avoid close contact with infected people, get vaccinated annually.",
        'Migraine': "Manage stress, avoid trigger foods, maintain a regular sleep schedule.",
        'Common Cold': "Practice good hygiene, stay hydrated, and rest well.",
        'COVID-19': "Wear masks, maintain social distance, wash hands frequently, get vaccinated.",
        'Viral Infection': "Maintain hygiene, eat nutritious food, avoid sick people.",
        'Unknown': "Consult a medical professional for advice."
    }

    explanation = explanations.get(disease_name, "No explanation available.")
    prevention = preventions.get(disease_name, "No preventive measures available.")

    return explanation, prevention
