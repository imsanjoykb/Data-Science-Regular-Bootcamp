#!/usr/bin/env python
# coding: utf-8

# # Clustering Algorithm In Machine Learning

# 1. [What is Clustering?](#1)
# 1. [What is K-Means Algorithm?](#2)
# 1. [How does the K-Means Algorithm Work?](#3)
# 1. [How to choose the value of "K number of clusters" in K-means Clustering?](#4)
# 1. [Implementation with Code](#5)

# ### <span id="1"></span>  1. What is Clustering?

# #### Clustering is the process of dividing the entire data into groups (also known as clusters) based on the patterns in the data.
# 
# Let’s kick things off with a simple example. A bank wants to give credit card offers to its customers. Currently, they look at the details of each customer and based on this information, decide which offer should be given to which customer.
# 
# Now, the bank can potentially have millions of customers. Does it make sense to look at the details of each customer separately and then make a decision? Certainly not! It is a manual process and will take a huge amount of time.
# 
# So what can the bank do? One option is to segment its customers into different groups. For instance, the bank can group the customers based on their income:
# 
# <img src="https://cdn.analyticsvidhya.com/wp-content/uploads/2019/08/Screenshot-from-2019-08-07-15-19-27.png" class="center">
# 

# ### <span id="2"></span>  2. What is K-Means Algorithm?

# K-Means Clustering is an Unsupervised Learning algorithm, which groups the unlabeled dataset into different clusters. Here K defines the number of pre-defined clusters that need to be created in the process, as if K=2, there will be two clusters, and for K=3, there will be three clusters, and so on.
# 
# It is an iterative algorithm that divides the unlabeled dataset into k different clusters in such a way that each dataset belongs only one group that has similar properties.
# It allows us to cluster the data into different groups and a convenient way to discover the categories of groups in the unlabeled dataset on its own without the need for any training.
# 
# It is a centroid-based algorithm, where each cluster is associated with a centroid. The main aim of this algorithm is to minimize the sum of distances between the data point and their corresponding clusters.
# 
# <img src="https://static.javatpoint.com/tutorial/machine-learning/images/k-means-clustering-algorithm-in-machine-learning.png" class="center">

# ### <span id="3"></span>  3. How does the K-Means Algorithm Work?

# The working of the K-Means algorithm is explained in the below steps:
# 
# Step-1: Select the number K to decide the number of clusters.
# 
# Step-2: Select random K points or centroids. (It can be other from the input dataset).
# 
# Step-3: Assign each data point to their closest centroid, which will form the predefined K clusters.
# 
# Step-4: Calculate the variance and place a new centroid of each cluster.
# 
# Step-5: Repeat the third steps, which means reassign each datapoint to the new closest centroid of each cluster.
# 
# Step-6: If any reassignment occurs, then go to step-4 else go to FINISH.
# 
# Step-7: The model is ready.

# ### <span id="4"></span>  4. How to choose the value of "K number of clusters" in K-means Clustering?

# WCSS= ∑Pi in Cluster1 distance(Pi C1)2 +∑Pi in Cluster2distance(Pi C2)2+∑Pi in CLuster3 distance(Pi C3)2
# 
# To find the optimal value of clusters, the elbow method follows the below steps:
# 
# It executes the K-means clustering on a given dataset for different K values (ranges from 1-10).
# 
# For each value of K, calculates the WCSS value.
# 
# Plots a curve between calculated WCSS values and the number of clusters K.
# 
# The sharp point of bend or a point of the plot looks like an arm, then that point is considered as the best value of K.

# ### <span id="5"></span>  5. Implementation with Code

# #### Import Necessary Libraries

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
get_ipython().run_line_magic('matplotlib', 'inline')


# #### Import Dataset

# In[6]:


df = pd.read_csv('F:\Data Science\Datasets\mall customers.csv')
df


# In[7]:


#### Rename Columns
df.rename(columns={'Gender':'gender', 'Age':'age','Annual Income (k$)':'income','Spending Score (1-100)':'score'}, inplace=True)


# In[8]:


df


# In[9]:


df.shape


# #### Checking Null Value

# In[10]:


df.isnull().sum()


# In[11]:


df = df.drop('CustomerID', axis = 1)


# In[12]:


df


# In[13]:


seaborn.pairplot(df[['age','income','score']])


# In[14]:


x = df.drop(['score','gender'], axis = 1)
x


# In[15]:


y = df['score']
y


# In[16]:


import sklearn.cluster as cluster


# In[17]:


kmeans = cluster.KMeans(n_clusters = 5) # k = 5


# In[18]:


kmeans = kmeans.fit(df[['income','score']])


# In[19]:


kmeans.cluster_centers_


# In[20]:


df['clusters'] = kmeans.labels_


# In[21]:


df['clusters']


# In[22]:


df.head(15)


# In[23]:


df['clusters'].value_counts()


# In[24]:


seaborn.scatterplot(x ='income', y='score', hue='clusters', data=df)


# In[25]:


from sklearn.cluster import KMeans


# In[26]:


K_range = range(1,15)
wcss = []


# In[27]:


for k in K_range:
    km = KMeans(n_clusters=k)
    km.fit(df[['income','score']])
    wcss.append(km.inertia_)  #Inertia_ is the sum of squared error for each cluster.


# In[28]:


wcss


# In[29]:


plt.xlabel('Number of clusters (K)') 
plt.ylabel('Sum of squared error') 
plt.plot(K_range,wcss) 
plt.title('Tennis Elbow Courve') 


# In[30]:


K_range = range(1,20)
wcss2 = []


# In[31]:


for k in K_range:
    km = KMeans(n_clusters=k)
    km.fit(df[['age','score']])
    wcss2.append(km.inertia_) #Inertia_ is the sum of squared error for each cluster.


# In[32]:


wcss2


# In[33]:


plt.xlabel('Number of clusters (K)')
plt.ylabel('Sum of squared error')
plt.plot(K_range,wcss2)


# In[34]:


kmeans2 = cluster.KMeans(n_clusters = 4)


# In[35]:


kmeans2 = kmeans2.fit(df[['age','score']])


# In[36]:


kmeans2.cluster_centers_


# In[37]:


df['age_clusters'] = kmeans2.labels_


# In[38]:


df['age_clusters'].value_counts()


# In[39]:


seaborn.scatterplot(x='age', y='score',hue='age_clusters',data=df)


# In[ ]:




