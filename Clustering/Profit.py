# Profit From Customers

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# Import Datasets
datasets = pd.read_csv("Mall_Customers.csv")
customers = datasets.iloc[:,[3,4]].values

# # build dendogram
# import scipy.cluster.hierarchy as sch
# dendrogram = sch.dendrogram(sch.linkage(customers,method='ward'))
# plt.plot(dendrogram)
# plt.title("Dendrogram")
# plt.show()

# Fitting Hierarchical Clustering
from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=5)
profit = cluster.fit_predict(customers)
pickle.dump(cluster,open("customer_profit.pk","wb"),protocol=2)

# # Visualisation
# plt.scatter(customers[profit == 0,0],customers[profit == 0,1],s=100,color="red",label="Carefull")
# plt.scatter(customers[profit == 1,0],customers[profit == 1,1],s=100,color="green",label="Average")
# plt.scatter(customers[profit == 2,0],customers[profit == 2,1],s=100,color="blue",label="Target")
# plt.scatter(customers[profit == 3,0],customers[profit == 3,1],s=100,color="orange",label="Careless")
# plt.scatter(customers[profit == 4,0],customers[profit == 4,1],s=100,color="yellow",label="NonProfitable")
# plt.title("Mall Customers Distribution")
# plt.xlabel("Annual Income")
# plt.ylabel("Spending Score")
# plt.legend()
# plt.show()