import re
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def basic_nlp_processing(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text
