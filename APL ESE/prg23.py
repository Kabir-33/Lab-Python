# 23 program for applying the stemming operation using NLTK

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Create a PorterStemmer object
ps = PorterStemmer()

# Sample text
text = "Cats running faster than dogs."

words = word_tokenize(text)

# Apply stemming to each word
stemmed_words = [ps.stem(word) for word in words]

print("Original words:", words)
print("Stemmed words:", stemmed_words)
