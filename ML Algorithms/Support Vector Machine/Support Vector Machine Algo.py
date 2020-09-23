#!/usr/bin/env python
# coding: utf-8

# ### Author : Sanjoy Biswas
# ### Topics : Support Vector Machine Algorithm :
# ### Email : sanjoy.eee32@gmail.com

# ###  What is Support Vector Machine?
# “Support Vector Machine” (SVM) is a supervised machine learning algorithm which can be used for both classification or regression challenges. However,  it is mostly used in classification problems. In the SVM algorithm, we plot each data item as a point in n-dimensional space (where n is number of features you have) with the value of each feature being the value of a particular coordinate. Then, we perform classification by finding the hyper-plane that differentiates the two classes very well (look at the below snapshot).

# ### Why SVMs
# Solve the data points are not linearly separable
# 
# Effective in a higher dimension.
# 
# Suitable for small data set: effective when the number of features is more than training examples.
# 
# Overfitting problem: The hyperplane is affected by only the support vectors, so SVMs are not robust to the outliner.

# #### Import Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# #### Import Dataset

# In[2]:


df = pd.read_csv('F:\Data Science\ML Algorithms\Support Vector Machine\credit card taiwan svm algorithm.csv')
df.head()


# #### Check Null Value

# In[3]:


df.isnull().sum()


# #### Nan Value Handeling

# In[4]:


missing = df.AGE.mean()
missing


# In[5]:


df.AGE = df.AGE.fillna(missing)


# In[6]:


df.isnull().sum()


# In[7]:


df


# In[8]:


df.head()


# #### Split Predictors & Prediction Row

# In[9]:


x = df.drop(['default.payment.next.month'],axis=1)
x


# In[11]:


y = df['default.payment.next.month']
y


# #### Split Train and Test datasets

# In[15]:


from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


# In[16]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25,random_state=42)


# In[17]:


x_train


# In[18]:


x_test


# #### Apply SVM Algorithm

# In[21]:


svmAlgo = SVC()


# In[22]:


model = svmAlgo.fit(x_train,y_train)


# In[24]:


model.score(x_train,y_train)


# In[25]:


model.score(x_test,y_test)


# In[ ]:




