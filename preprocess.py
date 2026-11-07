
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download stopwords
nltk.download("stopwords", quiet=True)

stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()


# Related expressions mapped to common concepts
SYNONYMS = {
    "financial aid": "scholarship",
    "financial assistance": "scholarship",
    "fee assistance": "scholarship",
    "accommodation": "hostel",
    "boarding facilities": "hostel",
    "campus recruitment": "placement",
    "career opportunities": "placement",
    "recruitment support": "placement",
    "job opportunities": "placement",
    "classes begin": "college start",
    "class timings": "college timings",
    "borrow books": "library books",
    "internship opportunities": "internship",
}


def preprocess_text(text):
    """
    Clean text, expand synonyms, remove stopwords
    and apply stemming for better FAQ matching.
    """

    text = text.lower()

    # Expand known synonyms
    for phrase, replacement in SYNONYMS.items():
        text = re.sub(
            r"\b" + re.escape(phrase) + r"\b",
            replacement,
            text
        )

    # Remove punctuation and special characters
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Tokenize
    words = text.split()

    # Remove stopwords and apply stemming
    words = [
        stemmer.stem(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)
