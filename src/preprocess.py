import re
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www.\S+", "", text)                 # Remove URLs
    text = re.sub(r"[^a-z\s]", "", text)                        # Remove punctuation/numbers
    text = " ".join([word for word in text.split() if word not in STOPWORDS])
    return text
