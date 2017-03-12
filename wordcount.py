# Read text file as a string sentence
sentences = ""
for line in open("./building_global_community.txt"):
    # delete the blank and line feed at the begining and end
    line = line.strip()
    # concatenate line text into string 'sentences'
    sentences = sentences + " " + line

# Normalize words ('Word' and 'word' are considered as the same word)
sentences = sentences.lower()

# Split sentences into words (use nltk word_tokenize from nltk)
import nltk
nltk.download('punkt')
from nltk import wordpunct_tokenize
words = wordpunct_tokenize(sentences)

# Filter out symbols (isalpha, isdigit, isalnum)
clean = [word for word in words if word.isalpha() == True or word.isdigit() == True or word.isalnum() == True]

# Filter out stopwords (stopwords from nltk)
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
clean = [word for word in clean if word not in stopwords]

# Count the occurance of words (Counter)
from collections import Counter
wordCounter = Counter(clean)
for word, count in wordCounter.most_common(20):
        print("%s: %d" % (word, count))
