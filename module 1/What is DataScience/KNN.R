rm(list = ls())

####### Enviornment setup
library(class) #Has the knn function

####### Data pull
#Path
rootPathVar <- "/Users/ael-annan/Desktop/Storage/MveMveMve/UCLAInstructor/Summer2018-361188-Introduction to Data Science COM SCI X 450.1/Module 1/Module 1a/"
valentineTreats <- read.csv(paste(rootPathVar,"ValentinesTreats.csv",  sep=""), header = TRUE)

####### Data Inspection
#Inspect/characterize data
dim(valentineTreats)
summary(valentineTreats)

#Simplify data
columnVars <- c("saltyOrSweet", "x_sodiumLevel_.g.", "y_highFructoseCornSyrup_.g.")
valentineTreatsSubset <- valentineTreats[columnVars]

dim(valentineTreatsSubset)
summary(valentineTreatsSubset)

####### Get training/test data ready
train = head(valentineTreatsSubset, 6)
X_default_train = train[, -1]
y_default_train = train$saltyOrSweet

test = tail(valentineTreatsSubset, 3)
X_default_test = test[, -1]

####### Perform KNN algorithim using Euclidean distance
#https://cran.r-project.org/web/packages/class/class.pdf
result = (knn(train = X_default_train, 
         test = X_default_test, 
         cl = y_default_train, 
         k = 3))
