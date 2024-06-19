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