import nltk
from nltk.tokenize import word_tokenize 
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words=set(stopwords.words("english"))
text="This is a sample sentence showing off the stopword filtration."
words=word_tokenize (text)
filtered_words=[word for word in words if word.lower() not in stop_words]
print(filtered_words)