# Car Evaluation

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder

# Import Datasets
datasets = pd.read_csv("car evaluation.csv")
X = datasets.iloc[:,0:6].values
y = datasets.iloc[:,6].values

# Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)

# prepare input data
def prepare_inputs(X_train, X_test):
	oe = OrdinalEncoder()
	oe.fit(X_train)
	X_train_enc = oe.transform(X_train)
	X_test_enc = oe.transform(X_test)
	return X_train_enc, X_test_enc

# prepare target
def prepare_targets(y_train, y_test):
	le = LabelEncoder()
	le.fit(y_train)
	y_train_enc = le.transform(y_train)
	y_test_enc = le.transform(y_test)
	return y_train_enc, y_test_enc

# prepare input data
X_train_enc, X_test_enc = prepare_inputs(X_train, X_test)
# prepare output data
y_train_enc, y_test_enc = prepare_targets(y_train, y_test)

# Fitting Decision Tree Model
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion="entropy")
classifier.fit(X_train_enc,y_train_enc)
# pickle.dump(classifier,open("car evaluation.pk","wb"),protocol=2)

# K-fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator=classifier, X=X_train_enc,y=y_train_enc,cv=10)
accuracie = accuracies.mean()

# Prediction
y_pred = classifier.predict(X_test_enc)

# Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test_enc, y_pred)

# for 0 and 1
# vhigh = 3
# high = 0
# med = 2
# low = 1

# for 2
# 3 = 1
# 2 = 0
# 4 = 2
# 5more = 3

# for 3
# more = 2
# 2 = 0
# 4 = 1

# for 4:
# small = 2
# big = 0
# med = 1
    
    
# for 5
# high = 0 
# med = 2
# low = 1

# for result
# unacc = 2
# acc = 0
# good = 1
# vgood = 3
