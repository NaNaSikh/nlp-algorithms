
import nltk
import spacy
import matplotlib.pyplot as plt
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
from time import time
from memory_profiler import memory_usage
import pandas as pd
import seaborn as sns

nltk.download('punkt')
nltk.download('wordnet')


text = gutenberg.raw('austen-emma.txt')[:5000]
sentences = sent_tokenize(text)


nlp = spacy.load('en_core_web_sm')

def lemmatize_with_spacy(text):
    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]
    return ' '.join(lemmas)

# Function to lemmatize text using WordNet and return a string
def lemmatize_with_wordnet(words):
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmas = [wordnet_lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmas)


def evaluate_lemmas(texts):
    results = []
    lemma_algorithms = {
        'WordNet': lemmatize_with_wordnet,
        'spaCy': lemmatize_with_spacy,
    }

    for name, lemmatizer in lemma_algorithms.items():
        start_time = time()
        if name == 'WordNet':
            lemmatized_texts = [lemmatizer(word_tokenize(text)) for text in texts]
        else:
            lemmatized_texts = [lemmatizer(text) for text in texts]
        end_time = time()
        duration = end_time - start_time
        all_lemmas = ' '.join(lemmatized_texts).split()
        unique_lemmas = len(set(all_lemmas))
        results.append((name, duration, unique_lemmas))
    return results


def getLemmasPlots():
    df = pd.DataFrame(evaluate_lemmas(sentences), columns=['Lemma', 'Time', 'Unique Lemmas'])
    return df