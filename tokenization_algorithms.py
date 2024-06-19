import pandas as pd
import spacy
from nltk.tokenize import WhitespaceTokenizer
import  re
def whitespaceTokenizationAlgorithm(text):
    tk = WhitespaceTokenizer()
    tokens  =  tk.tokenize(text)
    return  tokens


def punctuationTokenizationAlgorithm(text):
    pattern = r'\w+|[^\w\s]'
    tokens = re.findall(pattern, text)
    return tokens

def NER_Algorithm(text):
    nlp = spacy.load("en_core_web_sm")
    pd.set_option("display.max_rows", 200)
    doc = nlp(text)
    return  doc.ents
