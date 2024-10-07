from nltk.stem import PorterStemmer
ps=PorterStemmer()
words=["running","runner","ran","runs"]
Stemmed_words=[ps.stem(word) for word  in words]
print(Stemmed_words)