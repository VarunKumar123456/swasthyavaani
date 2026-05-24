import re
import nltk
nltk.download('punkt')

def basic_nlp_processing(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text
