import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    tokens = [token for token in tokens if token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    preprocessed_text = " ".join(tokens)
    return preprocessed_text

def preprocess_text_from_dict(text_dict):
    preprocessed_text_dict = {}
    for filename, text in text_dict.items():
        preprocessed_text_dict[filename] = preprocess_text(text)
    return preprocessed_text_dict