### We need to install one-time
#Run within R
#install.packages("tm")  # for text mining
#install.packages("RColorBrewer") # color palettes, needed for wordcloud
#install.packages("wordcloud") # word-cloud generator 

######### load libraries
library("tm")
library("RColorBrewer")
library("wordcloud")

######### a). download a CSV file one time

#We manually download the constitution.text file

######### b). pull in that US constitution file
path='/Users/user/Downloads/moreExamples/RWordCloud/'
file='constitution.txt'
filePath=paste0(path,file)

# read the entire text in
text = readLines(filePath)

######### c). remove stop words

#Convert to a Corpus object
text = Corpus(VectorSource(text))
# Remove stop words
text <- tm_map(text, removeWords, stopwords("english"))

#Create a 'count'/frequency of the various words for display
tdm <- TermDocumentMatrix(text)
m <- as.matrix(tdm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)
pal <- brewer.pal(8, "Dark2")

######### d). create a word cloud!

#create wordcloud
wordcloud(words = d$word, freq = d$freq, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

#png(paste0(path,"wordcloud.png"), width=1280,height=800)



### Diagnostics

### Check the length of stop words
#length(stopwords())
#174 stop words

#d
#shall  180, united   54, states,   38