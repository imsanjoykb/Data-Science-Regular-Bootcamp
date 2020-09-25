#!/usr/bin/env python
# coding: utf-8

# ### Author : Sanjoy Biswas
# ### Topic : K Nearest Neighbors Algorithm For Machine Learning
# ### Email : snajoy.eee32@gmail.com

# #### K-Nearest Neighbor(KNN) Algorithm for Machine Learning
# .K-Nearest Neighbour is one of the simplest Machine Learning algorithms based on Supervised Learning technique.
# 
# .K-NN algorithm assumes the similarity between the new case/data and available cases and put the new case into the category that is most similar to the available categories.
# 
# .K-NN algorithm stores all the available data and classifies a new data point based on the similarity. This means when new data appears then it can be easily classified into a well suite category by using K- NN algorithm.
# 
# .K-NN algorithm can be used for Regression as well as for Classification but mostly it is used for the Classification problems.
# 
# .K-NN is a non-parametric algorithm, which means it does not make any assumption on underlying data.
# 
# .It is also called a lazy learner algorithm because it does not learn from the training set immediately instead it stores the dataset and at the time of classification, it performs an action on the dataset.
# 
# .KNN algorithm at the training phase just stores the dataset and when it gets new data, then it classifies that data into a category that is much similar to the new data.
# 
# .Example: Suppose, we have an image of a creature that looks similar to cat and dog, but we want to know either it is a cat or dog. So for this identification, we can use the KNN algorithm, as it works on a similarity measure. Our KNN model will find the similar features of the new data set to the cats and dogs images and based on the most similar features it will put it in either cat or dog category.

# #### How does K-NN work?
# The K-NN working can be explained on the basis of the below algorithm:
# 
# Step-1: Select the number K of the neighbors
# 
# Step-2: Calculate the Euclidean distance of K number of neighbors
# 
# Step-3: Take the K nearest neighbors as per the calculated Euclidean distance.
# 
# Step-4: Among these k neighbors, count the number of the data points in each category.
# 
# Step-5: Assign thenew data points to that category for which the number of the neighbor is maximum.
# 
# Step-6: Our model is ready.

# ### Import Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ### Import Dataset

# In[2]:


df = pd.read_csv("F:\ML Algorithms By Me\K Nearest Neighbors\Classified Data",index_col=0)


# In[3]:


df.head()


# ### Standardize the Variables

# In[4]:


from sklearn.preprocessing import StandardScaler


# In[5]:


scaler = StandardScaler()


# In[6]:


scaler.fit(df.drop('TARGET CLASS',axis=1))


# In[7]:


scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))


# In[8]:


df_feat = pd.DataFrame(scaled_features,columns=df.columns[:-1])
df_feat.head()


# ### Pair Plot

# In[9]:


sns.pairplot(df,hue='TARGET CLASS')


# ### Train Test Split

# In[10]:


from sklearn.model_selection import train_test_split


# In[11]:


x_train,x_test,y_train,y_test = train_test_split(scaled_features,df['TARGET CLASS'],test_size=0.30)


# ### Apply KNN Algorithm

# In[12]:


from sklearn.neighbors import KNeighborsClassifier


# In[13]:


knn = KNeighborsClassifier(n_neighbors = 1)


# In[14]:


knn.fit(x_train,y_train)


# In[15]:


pred = knn.predict(x_test)


# ### Predictions and Evaluations

# Lets Evaluate KNN Model

# In[16]:


from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import cross_val_score


# In[17]:


print(confusion_matrix(y_test,pred))


# In[18]:


print(classification_report(y_test,pred))


# ### Choosing a K Value

# Use Elbow Method to pick a good K value

# In[19]:


accuracy_rate = []

for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors = i)
    score = cross_val_score(knn,df_feat,df['TARGET CLASS'],cv=10)
    accuracy_rate.append(score.mean())


# In[20]:


error_rate = []

for i in range(1,40):
    
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(x_train,y_train)
    pred_i = knn.predict(x_test)
    error_rate.append(np.mean(pred_i !=y_test))


# In[21]:


error_rate = []

# Will take some time
for i in range(1,40):
    
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train,y_train)
    pred_i = knn.predict(x_test)
    error_rate.append(np.mean(pred_i != y_test))


# In[22]:



plt.figure(figsize=(10,6))
#plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o',
  #       markerfacecolor='red', markersize=10)
plt.plot(range(1,40),accuracy_rate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')


# In[24]:



# FIRST A QUICK COMPARISON TO OUR ORIGINAL K=1
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(x_train,y_train)
pred = knn.predict(x_test)

print('WITH K=1')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))


# In[25]:


# NOW WITH K=23
knn = KNeighborsClassifier(n_neighbors=23)

knn.fit(x_train,y_train)
pred = knn.predict(x_test)

print('WITH K=23')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))


# ### References :
# 
# 1.Krish Naik [Youtube Channel]
# 
# 2.javatpoint.com
# 
# 3.https://medium.com/capital-one-tech/k-nearest-neighbors-knn-algorithm-for-machine-learning-e883219c8f26
# 
# 4.https://www.analyticsvidhya.com/blog/2018/03/introduction-k-neighbours-algorithm-clustering/

# In[ ]:




