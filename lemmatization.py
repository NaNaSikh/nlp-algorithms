import spacy
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')
nltk.download('wordnet')
nltk.download('omw-1.4')
def wordnet_lemmatization_function(text):
    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(text)
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in words]
    lemmatized_text = ' '.join(lemmatized_tokens)
    return lemmatized_text

def spacy_lemmatization_function(text):
    doc = nlp(text)
    lemmatized_tokens = [token.lemma_ for token in doc]
    lemmatized_text = ' '.join(lemmatized_tokens)
    return lemmatized_text