#!/usr/bin/env python
# coding: utf-8

# ## Author : Sanjoy Biswas
# ## Topic : NumPy Tutorial: Data Analysis with NumPY
# ## Email : sanjoy.eee32@gmail.com

# # Numpy and Array Basics

# ### The numpy library is one of the core packages in Python's data science software stack. Many other Python data analysis libraries require numpy as a prerequisite, because they use its array data structure as a building block. The Kaggle Python environment has numpy available by default; if you are running Python locally, the Anaconda Python distribution comes with numpy as well.
# 
# ### Numpy implements a data structure called the N-dimensional array or ndarray. ndarrays are similar to lists in that they contain a collection of items that can be accessed via indexes. On the other hand, ndarrays are homogeneous, meaning they can only contain objects of the same type and they can be multi-dimensional, making it easy to store 2-dimensional tables or matrices.

# # Import NumPY Library

# In[1]:


import numpy as np


# # Creating a NumPy Array

# ## Basic ndarray

# In[2]:


a = [10,20,30,40]


# In[3]:


type(a)


# In[4]:


x = np.array(a)


# In[5]:


print(x)


# In[6]:


type(x)


# In[7]:


a = [1,2,3,4]
b = [10,20,30,40]
x = np.array([a,b])


# In[8]:


print(x)


# In[9]:


a = [1,2,3,4]
b = [10,20,30]
x = np.array([a,b])


# In[10]:


print(x)


# In[11]:


x = np.array([1,2,3,4], dtype = np.float32)
print(x)


# In[12]:


x = np.zeros((2,3))
print(x)


# ## Array of zeros

# In[13]:


x = np.zeros((4,4))
print(x)


# ## Array of ones

# In[14]:


np.ones((3,3))


# In[15]:


np.ones(5, dtype = np.int32)


# ## Random numbers in ndarrays

# In[16]:


x = np.random.rand(2,5)


# In[17]:


print(x)


# In[18]:


get_ipython().run_line_magic('pinfo2', 'np.random.rand')


# In[19]:


np.random.randint(1,20, size = (3,3))


# In[20]:


get_ipython().run_line_magic('pinfo2', 'np.random.randint')


# In[21]:


np.random.randn(2,5)


# In[22]:


get_ipython().run_line_magic('pinfo2', 'np.random.randn')


# In[23]:


np.random.choice([2,3,4,7,8,10])


# ## An array of your choice

# In[24]:


np.full((3,4),10)


# In[25]:


np.ones((3,3))*10


# ## Identity matrix

# In[26]:


x = np.eye(4, k = -1)
print(x)


# In[27]:


get_ipython().run_line_magic('pinfo2', 'np.eye')


# ## Evenly spaced ndarray

# In[28]:


np.arange(5,11)


# In[29]:


np.arange(0,11,2)


# In[30]:


np.linspace(0,1,5)


# # $\frac{end-start}{n-1}$

# # Shape and Reshaping of NumPy Array

# ## Dimension of nparray

# In[31]:


a = [10,20,30,40,50]
x = np.array(a)
print(x)


# In[32]:


x.ndim


# In[33]:


b = [1,2,3,4,5]
y = np.array([a,b])
print(y)


# In[34]:


y.ndim


# ## Shape of NumPy array

# In[35]:


y.shape


# In[36]:


y.size


# ## Reshaping a NumPy array

# In[37]:


a = np.array([3,6,9,12])
print(a)


# In[38]:


np.reshape(a, (2,2))


# In[39]:


a.reshape(2,2)


# In[40]:


x = np.arange(1,16)
x


# In[41]:


x.size


# In[42]:


x.reshape(5,3)


# ## Transpose of a NumPy array

# In[43]:


x = np.arange(1,16)
print(x)


# In[44]:


y = x.reshape(3,5)
print(y)


# In[45]:


z = np.transpose(y)
print(z)


# In[46]:


y.transpose()


# # Indexing and Slicing of NumPy Array

# ## 1D NumPy arrays

# In[47]:


a = np.arange(1,10)


# In[48]:


print(a)


# In[49]:


a[2:6]


# ## 2-D NumPy arrays

# In[50]:


x = np.arange(1,10).reshape(3,3)
print(x)


# In[51]:


x[1,2]


# In[52]:


x[1][2]


# In[53]:


x[1:3,1:3]


# # Stacking and Concatenating NumPy Arrays

# ## Stacking

# In[54]:


a = np.arange(1,6)
b = np.arange(6,11)


# In[55]:


print(a)


# In[56]:


print(b)


# In[57]:


x = np.vstack((a,b))


# In[58]:


print(x)


# In[59]:


x = np.hstack((a,b))


# In[60]:


print(x)


# ## Concatenating

# In[61]:


a = np.arange(1,10).reshape(3,3)


# In[62]:


b = np.arange(10,19).reshape(3,3)


# In[63]:


print(a)


# In[64]:


print(b)


# In[65]:


np.concatenate((a,b))


# In[66]:


np.concatenate((a,b), axis = 1)


# # Broadcasting in NumPy arrays

# In[67]:


a = np.arange(10,21,2)


# In[68]:


b = np.array([[2],[2]])


# In[69]:


print(a)


# In[70]:


print(b)


# In[71]:


z = a+b
print(z)


# In[72]:


a = np.arange(10,21,2)


# In[73]:


a+2


# In[74]:


a - b


# In[75]:


a*b


# In[76]:


a = np.ones((3,3))
b = np.array([2])
print(a)


# In[77]:


print(b)


# In[78]:


a+b


# In[79]:


a-b


# # Arithmetic Operations on NumPy Array

# In[80]:


a = np.eye(4)
print(a)


# In[81]:


print(a+5)


# In[82]:


a - 1


# In[83]:


a*2


# In[84]:


a/0.5


# In[85]:


np.sin(a)


# In[86]:


np.cos(a)


# In[87]:


np.sqrt(a)


# # Aggregate Function

# ## Mean, Median and Standard deviation

# In[88]:


a = np.arange(5,15,2)


# In[89]:


print(a)


# In[90]:


np.mean(a)


# In[91]:


np.median(a)


# In[92]:


np.std(a)


# ## Min-Max values

# In[93]:


a = np.array([[1,6],[4,3]])
print(a)


# In[94]:


print(np.min(a, axis = 0))


# In[95]:


print(np.min(a, axis = 1))


# In[96]:


print(np.max(a, axis = 1))


# In[97]:


print(np.max(a, axis = 0))


# # Sorting

# In[98]:


a = np.array([1,4,3,10,20])


# In[99]:


x = np.sort(a, kind = 'mergesort')


# In[100]:


print(x)


# # Matrix Multiplication

# In[101]:


A = np.arange(0,9).reshape(3,3)
B = np.ones((3,3))


# In[102]:


print(A)


# In[103]:


print(B)


# In[104]:


np.dot(A,B)


# In[105]:


A.dot(B)


# In[ ]:




