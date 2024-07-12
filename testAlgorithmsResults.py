from sklearn.datasets import fetch_20newsgroups
import nltk
import time
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer

nltk.download('punkt')

newsgroups_data = fetch_20newsgroups(subset='all')
texts = newsgroups_data.data[:1000]  # Limiting to 1000 texts for simplicity

tokenized_texts = [nltk.word_tokenize(text) for text in texts]

porter = PorterStemmer()
snowball = SnowballStemmer("english")
lancaster = LancasterStemmer()

def stem_words(stemmer, words):
    return [stemmer.stem(word) for word in words]

def evaluate_stemmers(texts):
    results = []
    stemmers = {
        'Porter': porter,
        'Snowball': snowball,
        'Lancaster': lancaster
    }

    for name, stemmer in stemmers.items():
        start_time = time.time()
        stemmed_texts = [stem_words(stemmer, text) for text in texts]
        end_time = time.time()
        duration = end_time - start_time
        all_stems = [stem for text in stemmed_texts for stem in text]
        unique_stems = len(set(all_stems))
        results.append((name, duration, unique_stems))

    return results
results = evaluate_stemmers(tokenized_texts)


def getStemmersPlots():
    results = evaluate_stemmers(tokenized_texts)
    df = pd.DataFrame(results, columns=['Stemmer', 'Time', 'Unique Stems'])
    return  df

