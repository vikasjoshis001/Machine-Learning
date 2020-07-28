#  Salary Predictor

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# Import Datasets
datasets = pd.read_csv("Salary_Data.csv")
experience = datasets.iloc[:,0].values.reshape(-1,1)
salary = datasets.iloc[:,1].values.reshape(-1,1)

# Train_Test_Split
from sklearn.model_selection import train_test_split
experience_train,experience_test,salary_train,salary_test = train_test_split(experience,salary,test_size=0.2,random_state=0)

# Fitting Linear Regression Model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(experience_train,salary_train)
pickle.dump(regressor,open("salary_predictor.pk","wb"),protocol=2)