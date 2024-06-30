from sklearn.datasets import fetch_20newsgroups
import nltk
import time
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer

# Download the necessary NLTK data
nltk.download('punkt')

# Load the 20 Newsgroups dataset
newsgroups_data = fetch_20newsgroups(subset='all')
texts = newsgroups_data.data[:1000]  # Limiting to 1000 texts for simplicity

# Tokenize the texts
tokenized_texts = [nltk.word_tokenize(text) for text in texts]

# Initialize the stemmers
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

# Evaluate the stemmers
results = evaluate_stemmers(tokenized_texts)

# Convert results to a pandas DataFrame
df = pd.DataFrame(results, columns=['Stemmer', 'Time', 'Unique Stems'])

# Plotting the results
plt.figure(figsize=(14, 6))

# Plotting time taken
plt.subplot(1, 2, 1)
sns.barplot(x='Stemmer', y='Time', data=df)
plt.title('Time Taken by Different Stemmers')
plt.ylabel('Time (seconds)')

# Plotting number of unique stems
plt.subplot(1, 2, 2)
sns.barplot(x='Stemmer', y='Unique Stems', data=df)
plt.title('Number of Unique Stems Produced by Different Stemmers')
plt.ylabel('Unique Stems')

plt.tight_layout()
plt.show()
