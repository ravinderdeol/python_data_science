import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# load the data into a pandas dataframe from a text file separating the reviews and sentiments using the tab character
df = pd.read_csv("amazon_labelled.txt", names = ["review", "sentiment"], sep = "\t")

# split the data into two parts with one used to train the model and the other to test its accuracy
# extract the review and sentiment column from the dataframe as a numpy array
reviews = df["review"].values
sentiments = df["sentiment"].values

# reviews and sentiments passed to the function as numpy arrays obtained via the values property of the series objects extracted from the dataframe
# test size parameter controls how the dataset is split with 0.2 (20%) of the reviews randomly selected following the pareto principle and the remaining used in the training set
# random state parameter initializes the internal random number generator needed to randomly split the data
# experimenting with test size and random state will show different results due to random different sets of data being used
reviews_train, reviews_test, sentiments_train, sentiments_test = train_test_split(reviews, sentiments, test_size = 0.2, random_state = 500)

# training and testing models required a way to represent text numerically hence the bag of words model
# create a vectorizer object to convert the reviews into numerical feature vectors
vectorizer = CountVectorizer()

# build the vocabulary of tokens found in the reviews dataset containing all reviews using the fit method
vectorizer.fit(reviews)

# convert the training and test sets into feature vectors using the transform method
x_train = vectorizer.transform(reviews_train)
x_test = vectorizer.transform(reviews_test)

# we must train the scikit learn logistic regression classifier to predict the sentiment of reviews
# create a logistic regression classifier to train and evaluate the model
classifier = LogisticRegression()

# train the model on the training data using the fit method
classifier.fit(x_train, sentiments_train)

# a set of labelled data is required hence it is common to split labelled datasets into a training and test set 
# evaluate the model using the test set
accuracy = classifier.score(x_test, sentiments_test)

# accuracy equals 0.81 (81%) meaning the model is 81% accurate
print("accuracy: ", accuracy)

# it is possible to make predictions on new and unlabelled data now the model has been trained and tested
# create a list of new reviews to predict the sentiment for
new_reviews = ["old version of python useless", "very good effort, but not five stars", "clear and concise"]

# convert the new reviews into numerical feature vectors using the vectorizer object
x_new = vectorizer.transform(new_reviews)

# predict the class sentiments for the new reviews using the trained classifier
# prints [0 0 1] with 0 being negative and 1 being positive
print("new:", classifier.predict(x_new))

# notes
    # data used can be found at https://archive.ics.uci.edu/ml/datasets/sentiment+labelled+sentences
    # scitkit learn is a python package designed for machine learning
    # predictive data analysis is an area of machine learning that relies on classification and regression algorithms
    # classification and regression use past data to make predictions about new data
    # classification sorts data into categories while regression can output a continuous range of numerical values
    # it is common to only import the submodules you need from scikit learn
    # predictive models should be trained on large numbers of labelled samples to be accurate
    # use scikit learns count vectorizer function to create a bag of words matrix for text data
    # logistic regression is a basic yet popular algorithm for solving classification problems