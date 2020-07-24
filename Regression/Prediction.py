#  Rank Predictor

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# Import Datasets
datasets = pd.read_csv("Rank_Predictor.csv")
percentile = datasets.iloc[:,0:4].values
rank = datasets.iloc[:,4].values

# Train_Test_Split
from sklearn.model_selection import train_test_split
percentile_train,percentile_test,rank_train,rank_test = train_test_split(percentile,rank,test_size=0.25,random_state=0)

# Fitting Regression Model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(percentile_train,rank_train)
# pickle.dump(regressor,open("rank_predictor.pk","wb"),protocol=2)

# K-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracie = cross_val_score(estimator=regressor, X=percentile_train,y=rank_train,cv=10)
result = accuracie.mean()

# Prediction
rank_pred = regressor.predict(percentile_test)

