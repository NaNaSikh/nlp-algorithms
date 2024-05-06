import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer

nltk.download('punkt')


sentence = "The quick brown foxes were jumping over the lazy dogs."
words = word_tokenize(sentence)
def stemmingPoterAlgorithm():
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words


def stemmingSnowballAlgorithm():
    snow_stemmer = SnowballStemmer(language='english')
    stemmed_words = [snow_stemmer.stem(word) for word in words]
    return stemmed_words

print(stemmingSnowballAlgorithm())




