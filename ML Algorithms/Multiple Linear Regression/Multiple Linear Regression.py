#!/usr/bin/env python
# coding: utf-8

# #### Author : Sanjoy Biswas
# #### Topic : Multiple Linear Regression : Car Price Prediction
# #### Email : sanjoy.eee32@gmail.com

# It is the extension of simple linear regression that predicts a response using two or more features. Mathematically we can explain it as follows −
# 
# Consider a dataset having n observations, p features i.e. independent variables and y as one response i.e. dependent variable the regression line for p features can be calculated as follows −
# 
# h(xi)=b0+b1xi1+b2xi2+⋯+bpxip
# Here, h(xi) is the predicted response value and b0,b1,b2,⋯bp are the regression coefficients.
# 
# Multiple Linear Regression models always includes the errors in the data known as residual error which changes the calculation as follows −
# 
# h(xi)=b0+b1xi1+b2xi2+⋯+bpxip+ei
# We can also write the above equation as follows −
# 
# yi=h(xi)+eiorei=yi−h(xi)

# #### Import Libraries

# In[ ]:


import numpy as np
import pandas as pd


# #### Import Datasets

# In[ ]:


df = pd.read_csv('datasets_794035_1363047_carprices.csv')
df


# In[ ]:


### Dummy Variables
dummies = pd.get_dummies(df['Car Model'])
dummies


# In[ ]:


### Merge Datasets
merge = pd.concat([df,dummies],axis='columns')
merge


# In[ ]:


final = merge.drop(['Car Model'],axis='columns')
final


# In[ ]:


### Column Name
final.columns


# #### Features Selection

# In[ ]:


predictors = ['Mileage','Age','Audi','BMW X5','Mercedez Benz ','Toyota']
x = final[predictors]
y = final['Sell Price']


# In[ ]:


x.shape,y.shape


# In[ ]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# #### Split Train and Test Datasets

# In[ ]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2 , random_state =43)


# In[ ]:


x_train.shape,x_test.shape


# In[ ]:


y_train.shape,y_test.shape


# #### Apply Linear Regression

# In[ ]:


reg = LinearRegression()


# In[ ]:


model = reg.fit(x_train,y_train)


# #### Predict Model

# In[ ]:


model.predict([[69000,6,0,1,0,0]])


# #### Accuracy Score

# In[ ]:


model.score(x_test,y_test)


# In[ ]:


model.score(x_train,y_train)


# In[ ]:




