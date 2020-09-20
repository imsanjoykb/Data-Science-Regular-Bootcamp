#!/usr/bin/env python
# coding: utf-8

# ### Author : Sanjoy Biswas
# ### Topic : Polynomial Regression : Problem Solving and Implementation
# ### Email : sanjoy.eee32@gmail.com

# #### Introduction to Polynomial Regression

# Polynomial regression is a special case of linear regression where we fit a polynomial equation on the data with a curvilinear relationship between the target variable and the independent variables.
# 
# In a curvilinear relationship, the value of the target variable changes in a non-uniform manner with respect to the predictor (s).
# 
# In Linear Regression, with a single predictor, we have the following equation:
# 
# linear regression equation
# 
# where,
# 
#          y = a + b1x + b2x^2 +....+ bnx^n
# 
#           Y is the target,
# 
#           x is the predictor,
# 
#           a is the bias,
# 
#           and b1 is the weight in the regression equation
# 
# This linear equation can be used to represent a linear relationship. But, in polynomial regression, we have a polynomial equation of degree n represented as:
# 
# polynomial regression equation
# 
# Here:
# 
#           a is the bias,
# 
#           b1, b2, …, bn are the weights in the equation of the polynomial regression,
# 
#           and n is the degree of the polynomial
# 
# The number of higher-order terms increases with the increasing value of n, and hence the equation becomes more complicated.

# #### Import Necessary Libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# #### Import Dataset

# In[2]:


df = pd.read_csv('F:\ML Algorithms By Me\Polynomial Regression\HeightWeightDataset.csv')
df.head()


# In[3]:


x = df.iloc[:, 0:1].values
y = df.iloc[:,1].values


# In[4]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state =0)


# In[5]:


from sklearn.linear_model import LinearRegression
LinReg = LinearRegression()
model = LinReg.fit(x_train,y_train)


# In[6]:


model.predict([[10]])


# In[7]:


model.score(x_train,y_train)


# #### Visualize the Linear Regression Result

# In[8]:


plt.scatter(x_train,y_train,color='green')
plt.plot(x_train,LinReg.predict(x_train),color='blue')
plt.title('Linear Regression')
plt.xlabel('Age')
plt.ylabel('Height')
plt.show()


# #### Add polynomial Term to the Equation and Model

# In[9]:


from sklearn.preprocessing import PolynomialFeatures 
  
polynom = PolynomialFeatures(degree = 2) 
x_polynom = polynom.fit_transform(x_train) 
  
x_polynom


# #### Fit the Polynomial Regression Model

# In[10]:


PolyReg = LinearRegression()
modell = PolyReg.fit(x_polynom,y_train)


# #### # Visualise the Polynomial Regression Results 

# In[11]:


plt.scatter(x_train,y_train,color = 'green')
plt.plot(x_train,PolyReg.predict(polynom.fit_transform(x_train)),color='blue')
plt.title('Polynomial Regression')
plt.xlabel('Age')
plt.ylabel('Height')
plt.show()


# #### Predicted Height from test dataset w.r.t Simple Linear Regression

# In[12]:


y_predict_slr = LinReg.predict(x_test)

#Model Evaluation using R-Square for Simple Linear Regression
from sklearn import metrics
r_square = metrics.r2_score(y_test,y_predict_slr)
print('R-Square Error associated with Simple Linear Regression:', r_square)


# #### Predicted Height from test dataset w.r.t Polynomial Regression

# In[13]:


y_predict_pr = PolyReg.predict(polynom.fit_transform(x_test))

#Model Evaluation using R-Square for Polynomial Regression
from sklearn import metrics
r_square = metrics.r2_score(y_test,y_predict_pr)
print('R-Square Error associated with Polynomial Regression is:', r_square)


# In[14]:


# Predicting Height based on Age using Linear Regression 
LinReg.predict([[54]])


# In[15]:


# Predicting Height based on Age using Polynomial Regression 
PolyReg.predict(polynom.fit_transform([[54]]))


# In[ ]:




