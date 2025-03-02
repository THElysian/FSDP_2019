# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:34:56 2019

@author: Himanshu Rathore
"""

from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

# import dataset
iris = datasets.load_iris()

# Making Features
features = iris.data

# Performing Dimension Reduction
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)

# Finding no of clusters using Elbow Method
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_) 
#Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Fitting K-Means
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

# For interpreting clusters and add Group Column
iris["Group"] = pred_cluster

# Visualising the clusters
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Setosa')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Versicolor')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Virginica')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()