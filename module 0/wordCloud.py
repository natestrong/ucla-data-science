### We need to install one-time
#Run on command line (Mac shell, or Command shell in Windows), i.e. conda install -c conda-forge wordcloud on shell from https://anaconda.org/conda-forge/wordcloud
#https://anaconda.org/conda-forge/wordcloud
#https://anaconda.org/anaconda/nltk
#https://anaconda.org/conda-forge/matplotlib

######### load libraries
# User the Python Standard Library os (we pull it in import os)
#https://docs.python.org/3/library/
# https://docs.python.org/3/library/os.html
import os
### We need to install one-time
from wordcloud import WordCloud
#import the nltk library (https://www.nltk.org/)
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
#to display/generate visualizations
import matplotlib.pyplot as plt

######### a). download a CSV file one time

#We manually download the constitution.text file

######### b). pull in that US constitution file
path='/Users/user/Downloads/moreExamples/pythonWordCloud/'
file='constitution.txt'
filePath=path+file
# read the entire text in
text = open(filePath).read()

######### c). remove stop words

#load stopwords, i.e. usually refer to the most common words (the, it, for, etc.)
nltk.download('stopwords')
stopWords = set(stopwords.words('english'))

#alternatively we could have used the STOPWORDS library that comes with
#identify stopwords from Word Cloud
#from wordcloud import WordCloud, STOPWORDS
#stopWordFromWordCloud = set(STOPWORDS)

#convert the text into tokens
nltk.download('punkt')

textBeforeFiltering = word_tokenize(text)
#remove stop words
textPostFiltering = [w for w in textBeforeFiltering if not w in stopWords] 


######### d). create a word cloud!

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display image
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


### Diagnostics

### Check the length of stop words
#len(stopWords)
#179 stop words

### Check the most frequent words
#wordcloud.words_
#'State': 1.0, 'United States': 0.8181818181818182, 'Law': 0.5151515151515151
