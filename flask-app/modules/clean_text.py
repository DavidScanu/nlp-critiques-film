import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer

def clean_text(text):

    # Standardize text
    text = text.replace(r"http\S+", "")
    text = text.replace(r"http", "")
    text = text.replace(r"@\S+", "")
    text = text.replace(r"[^A-Za-z0-9(),!?@\'\`\"\_\n]", " ")
    text = text.replace(r"@", "at")

    # Lower Casing
    text = text.lower()

    # accents ?

    # Tokenization
    words = nltk.word_tokenize(text) # list

    # Remove punctuation
    new_words = [word for word in words if word.isalnum()]

    # Stop Word Removal
    WordSet = []
    for word in new_words:
        if word not in set(stopwords.words("french")):
            WordSet.append(word)
    
    # Lemmatization
    lm = FrenchLefffLemmatizer()
    # WordSetLem = []
    # for word in WordSet:
    #     WordSetLem.append(lm.lemmatize(word))

    return ' '.join(WordSet) # return string for CountVectorizer