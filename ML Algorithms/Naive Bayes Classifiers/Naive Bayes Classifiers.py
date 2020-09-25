#!/usr/bin/env python
# coding: utf-8

# ### Naive Bayes Classifiers 

# #### Author : Sanjoy Biswas 
# #### Topic : NaiveNaive Bayes Classifiers : Spam Ham Email Datection 
# #### Email : sanjoy.eee32@gmail.com 

# It is a classification technique based on Bayes’ Theorem with an assumption of independence among predictors. In simple terms, a Naive Bayes classifier assumes that the presence of a particular feature in a class is unrelated to the presence of any other feature.
# 
# For example, a fruit may be considered to be an apple if it is red, round, and about 3 inches in diameter. Even if these features depend on each other or upon the existence of the other features, all of these properties independently contribute to the probability that this fruit is an apple and that is why it is known as ‘Naive’.
# 
# Naive Bayes model is easy to build and particularly useful for very large data sets. Along with simplicity, Naive Bayes is known to outperform even highly sophisticated classification methods.
# 
# Bayes theorem provides a way of calculating posterior probability P(c|x) from P(c), P(x) and P(x|c). Look at the equation below:

# ![alt text](Bayes_rule.webp "Title")

# Above,
# 
# P(c|x) is the posterior probability of class (c, target) given predictor (x, attributes).<br>
# !P(c) is the prior probability of class.<br>
# P(x|c) is the likelihood which is the probability of predictor given class.<br>
# P(x) is the prior probability of predictor.
# 

# ### Import Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ### Import Dataset

# In[3]:


df = pd.read_csv(r'F:\ML Algorithms By Me\Naive Bayes Classifiers\emails.csv')


# In[4]:


df.head()


# In[5]:


df.isnull().sum()


# ### Separate Dependent & Independent Value

# In[14]:


x = df.text.values
y = df.spam.values


# ### Split Train and Test Dataset

# In[17]:


from sklearn.model_selection import train_test_split


# In[19]:


xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.3)


# ### Data Preprocessing

# In[21]:


from sklearn.feature_extraction.text import CountVectorizer


# In[26]:


cv = CountVectorizer()


# In[33]:


x_train = cv.fit_transform(xtrain)


# In[34]:


x_train.toarray()


# ### Apply Naive Bayes Classifiers Algorithm

# In[29]:


from sklearn.naive_bayes import MultinomialNB


# In[30]:


model = MultinomialNB()


# In[32]:


model.fit(x_train,ytrain)


# In[35]:


x_test = cv.fit_transform(xtest)


# In[36]:


x_test.toarray()


# In[39]:


model.score(x_train,ytrain)


# In[ ]:




