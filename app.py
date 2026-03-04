from flask import Flask, render_template, request
from gtts import gTTS
from nlp_utils import basic_nlp_processing
from symptom_extractor import load_symptoms, extract_symptoms
from disease_predictor import predict_disease
from genai_explainer import generate_explanation_and_prevention
from wellness_recommender import get_personalized_recommendations
import os

app = Flask(__name__)

SYMPTOMS_DICT = load_symptoms(file_path='data/symptoms_multilang.txt')

@app.route('/', methods=['GET', 'POST'])
def index():
    processed_text = ''
    extracted_symptoms = []
    predicted_disease = ''
    risk_factors = ''
    explanation = ''
    prevention = ''
    wellness_recommendation = ''
    symptom_audio = disease_audio = risk_audio = explanation_audio = preventive_audio = wellness_audio = None

    if request.method == 'POST':
        input_mode = request.form['input_mode']
        lang_choice = request.form['language']

        if input_mode == 'text':
            user_input = request.form.get('user_input', '').strip()
        else:
            user_input = request.form.get('speech_input', '').strip()

        if not user_input:
            user_input = "No input provided."

        processed_text = basic_nlp_processing(user_input)

        symptoms_list = SYMPTOMS_DICT.get(lang_choice, [])
        extracted_symptoms = extract_symptoms(processed_text, symptoms_list)

        prediction = predict_disease(extracted_symptoms)
        predicted_disease = prediction['disease']
        risk_factors = prediction['risk_factors']

        explanation, prevention = generate_explanation_and_prevention(predicted_disease)

        wellness_recommendation = get_personalized_recommendations(extracted_symptoms, predicted_disease)

        # Generate audio files for all outputs
        tts_symptom = gTTS(text=", ".join(extracted_symptoms) if extracted_symptoms else "No symptoms detected.", lang=lang_choice)
        tts_symptom.save('static/symptom_audio.mp3')
        symptom_audio = 'static/symptom_audio.mp3'

        tts_disease = gTTS(text=predicted_disease, lang=lang_choice)
        tts_disease.save('static/disease_audio.mp3')
        disease_audio = 'static/disease_audio.mp3'

        tts_risk = gTTS(text=risk_factors, lang=lang_choice)
        tts_risk.save('static/risk_audio.mp3')
        risk_audio = 'static/risk_audio.mp3'

        tts_explanation = gTTS(text=explanation, lang=lang_choice)
        tts_explanation.save('static/explanation_audio.mp3')
        explanation_audio = 'static/explanation_audio.mp3'

        tts_preventive = gTTS(text=prevention, lang=lang_choice)
        tts_preventive.save('static/preventive_audio.mp3')
        preventive_audio = 'static/preventive_audio.mp3'

        tts_wellness = gTTS(text=wellness_recommendation, lang=lang_choice)
        tts_wellness.save('static/wellness_audio.mp3')
        wellness_audio = 'static/wellness_audio.mp3'

    return render_template('index.html',
                           processed_text=processed_text,
                           extracted_symptoms=extracted_symptoms,
                           predicted_disease=predicted_disease,
                           risk_factors=risk_factors,
                           explanation=explanation,
                           prevention=prevention,
                           wellness_recommendation=wellness_recommendation,
                           symptom_audio=symptom_audio,
                           disease_audio=disease_audio,
                           risk_audio=risk_audio,
                           explanation_audio=explanation_audio,
                           preventive_audio=preventive_audio,
                           wellness_audio=wellness_audio)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

