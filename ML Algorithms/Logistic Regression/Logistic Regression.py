#!/usr/bin/env python
# coding: utf-8

# ### Author : Sanjoy Biswas
# ### Topic : Logistic Regression : Maritial Status Prediction
# ### Email : sanjoy.eee32@gmail.com

# Logistic regression is one of the most popular Machine Learning algorithms, which comes under the Supervised Learning technique. It is used for predicting the categorical dependent variable using a given set of independent variables.
# 
# Logistic regression predicts the output of a categorical dependent variable. Therefore the outcome must be a categorical or discrete value. It can be either Yes or No, 0 or 1, true or False, etc. but instead of giving the exact value as 0 and 1, it gives the probabilistic values which lie between 0 and 1.

# #### Type of Logistic Regression:
# On the basis of the categories, Logistic Regression can be classified into three types:
# 
# Binomial: In binomial Logistic regression, there can be only two possible types of the dependent variables, such as 0 or 1, Pass or Fail, etc.
# Multinomial: In multinomial Logistic regression, there can be 3 or more possible unordered types of the dependent variable, such as "cat", "dogs", or "sheep"
# Ordinal: In ordinal Logistic regression, there can be 3 or more possible ordered types of dependent variables, such as "low", "Medium", or "High".

# #### Steps in Logistic Regression: 
# To implement the Logistic Regression using Python, we will use the same steps as we have done in previous topics of Regression. Below are the steps:
# 
# Data Pre-processing step
# 
# Fitting Logistic Regression to the Training set
# 
# Predicting the test result
# 
# Test accuracy of the result(Creation of Confusion matrix)
# 
# Visualizing the test set result.

# #### Equation of Logistic Regression
# 
# In Logistic Regression y can be between 0 and 1 only, so for this let's divide the above equation by (1-y):
# 
# y/1-y       0 for y=1, infinity for y=o
# 
# But we need range between -[infinity] to +[infinity], then take logarithm of the equation it will become:
# 
# log(y/1-y)= b0+b1x1+b2x2+.....+bnxn

# ### Import Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# #### Import Dataset

# In[2]:


df = pd.read_csv('F:\ML Algorithms By Me\Logistic Regression\marital status.csv')
df


# #### Check Null Value

# In[3]:


df.isnull().sum()


# #### Handle Null Value

# In[4]:


handle = df['status'].median()


# In[5]:


handle


# In[6]:


df.status = df.status.fillna(handle)


# In[7]:


df


# In[8]:


df['status'].value_counts()


# #### Split Dependent and independent variable

# In[9]:


x = df[['age']]
x


# In[10]:


y = df[['status']]
y


# #### Split Train and Test dataset

# In[11]:


from sklearn.model_selection import train_test_split


# In[12]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


# In[13]:


x_train


# In[14]:


x_test


# #### Apply Logistic Regression ALgorithm

# In[15]:


from sklearn.linear_model import LogisticRegression


# In[16]:


model = LogisticRegression()


# In[17]:


model.fit(x_train,y_train)


# In[18]:


model.predict(x_test)


# In[19]:


model.score(x_train,y_train)


# In[20]:


model.score(x_test,y_test)


# In[ ]:




