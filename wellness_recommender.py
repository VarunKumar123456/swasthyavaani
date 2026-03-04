def get_personalized_recommendations(symptoms, disease):
    # Basic rule-based or RL approach (can be extended later)
    recommendations = []

    if 'fever' in symptoms or 'cough' in symptoms:
        recommendations.append("Stay hydrated by drinking plenty of fluids.")
        recommendations.append("Rest as much as possible.")
    if 'headache' in symptoms:
        recommendations.append("Maintain a light diet and reduce screen time.")
    if 'fatigue' in symptoms:
        recommendations.append("Ensure balanced nutrition and regular sleep schedule.")

    if not recommendations:
        recommendations.append("Maintain a balanced diet, regular exercise, and proper hydration.")

    return " | ".join(recommendations)
