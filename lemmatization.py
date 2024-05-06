import spacy

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')
def lemmatiazation_function():

    text = "The quick brown foxes are jumping over the lazy dogs."

    doc = nlp(text)

    lemmatized_tokens = [token.lemma_ for token in doc]

    lemmatized_text = ' '.join(lemmatized_tokens)

    print("Original Text:", text)
    print("Lemmatized Text:", lemmatized_text)
    return lemmatized_text

lemmatiazation_function()