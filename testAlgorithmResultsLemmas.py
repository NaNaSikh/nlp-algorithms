
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

# Download the necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Load a sample text from the Gutenberg corpus
text = gutenberg.raw('austen-emma.txt')[:5000]  # Using the first 5000 characters for demonstration
sentences = sent_tokenize(text)

# Initialize spaCy
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

# Function to evaluate lemmatization algorithms
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




# Evaluate the lemmatizers
ans = evaluate_lemmas(sentences)

# Convert results to a pandas DataFrame


# Plotting the results
# plt.figure(figsize=(14, 6))
#
# # Plotting time taken
# plt.subplot(1, 2, 1)
# sns.barplot(x='Lemma', y='Time', data=df)
# plt.title('Time Taken by Different Lemmatization Algorithms')
# plt.ylabel('Time (seconds)')
#
# # Plotting number of unique lemmas
# plt.subplot(1, 2, 2)
# sns.barplot(x='Lemma', y='Unique Lemmas', data=df)
# plt.title('Number of Unique Lemmas Produced by Different Lemmatization Algorithms')
# plt.ylabel('Unique Lemmas')
#
# plt.tight_layout()
# plt.show()


def getLemmasPlots():
    df = pd.DataFrame(ans, columns=['Lemma', 'Time', 'Unique Lemmas'])
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Plotting time taken
    sns.barplot(x='Lemma', y='Time', data=df, ax=axs[0])
    axs[0].set_title('Time Taken by Different Lemmatization Algorithms')
    axs[0].set_ylabel('Time (seconds)')

    # Plotting number of unique lemmas
    sns.barplot(x='Lemma', y='Unique Lemmas', data=df, ax=axs[1])
    axs[1].set_title('Number of Unique Lemmas Produced by Different Lemmatization Algorithms')
    axs[1].set_ylabel('Unique Lemmas')

    fig.tight_layout()
    return fig