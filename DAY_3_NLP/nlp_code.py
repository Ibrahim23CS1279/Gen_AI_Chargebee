# TOKENIZATION
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")

text = "I'm not the danger, I'm in danger"
tokens = word_tokenize(text)
print("Tokens:", tokens)


# STOP WORDS
from nltk.corpus import stopwords

nltk.download("stopwords")

text = "I dont wanna live forever"
words = word_tokenize(text)

stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.lower() not in stop_words]

print("Original:", text)
print("Filtered:", " ".join(filtered_words))


# STEMMING
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["running", "runner", "easily", "fairly"]
stemmed_words = [stemmer.stem(word) for word in words]

print("Stemmed words:", stemmed_words)


# LEMMATIZATION
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

words = ["running", "runner", "easily", "fairly"]
lemmatized_words = [lemmatizer.lemmatize(word, pos=wordnet.VERB) for word in words]

print("Lemmatized words:", lemmatized_words)


# PARTS OF SPEECH TAGGING
from nltk import pos_tag

nltk.download("averaged_perceptron_tagger")

sentence = "The quick brown fox jumps over the lazy dog."
tokens = word_tokenize(sentence)

tagged = pos_tag(tokens)
print("POS Tags:", tagged)


# SYNTAX (Simple evaluation example)
exp = "5+3*3"
result = eval(exp)
print("Expression result:", result)


# LOWERCASING
text = "Hello World"
lowercase_text = text.lower()
print("Lowercase:", lowercase_text)


# REMOVE SPECIAL CHARACTERS
import re

def remove_special(text):
    return re.sub(r'[^A-Za-z0-9\s]', "", text)

text = "hello$$$^&*## world"
clean_text = remove_special(text)
print("No special chars:", clean_text)


# REMOVE PUNCTUATION
import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

text = "Hello, world! remove punctuation."
clean_text = remove_punctuation(text)
print("No punctuation:", clean_text)


# BAG OF WORDS
from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "I'm programming in Python",
    "Python is great for data science",
    "I love learning new programming languages"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names_out()

print("Feature Names:", feature_names)
print("Bag of Words:\n", X.toarray())


# N-GRAMS
def n_grams(text, n):
    words = text.split()
    return [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]

text = "I love programming in Python"
n = 2

print("N-grams:", n_grams(text, n))