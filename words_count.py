import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

######## Section 1 # content.txt -> stemmed-content.txt

content = open("content.txt").read()
words = word_tokenize(content)

file = open("stemmed-content.txt","w")

for w in words:
    print(ps.stem(w), file = open("stemmed-content.txt","a"))

file.close()


######## Section 2 # stemmed-content.txt -> count-statistics.txt

stemmed = open("stemmed-content.txt").read().split()
UniqeWords = set(stemmed)

file = open("count-statistics.txt","w")

for w in UniqeWords:
    print(w+",", stemmed.count(w), file=open("count-statistics.txt", "a"))

file.close()

#########################
