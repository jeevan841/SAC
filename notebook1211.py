#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy


# In[2]:


array_shape = numpy.array([[10,20,30],[40,50,60]])


# In[3]:


array_shape.shape


# In[4]:


array_shape.ndim


# In[5]:


array_shape.size


# In[6]:


array_shape.dtype


# In[7]:


array_shape.itemsize


# In[8]:


array_shape.data


# In[9]:


numpy.zeros((2,3))


# In[10]:


numpy.ones((15,12))


# In[11]:


numpy.empty((2,3))


# In[12]:


numpy.full((3,3),2)


# In[13]:


numpy.eye(3,3)


# In[14]:


numpy.random.random((24,24))


# In[15]:


numpy.arange(10,30,2)


# In[16]:


numpy.arange(0,2.2,0.3)


# In[17]:


numpy.linspace(0,2,10)


# stop is inclusive in linspace but not in arange

# In[18]:


a = numpy.arange(6)


# In[19]:


a


# In[20]:


a[4]


# In[21]:


a[2:5]


# In[22]:


a[:4:2] = -999


# In[23]:


a


# In[24]:


a[::-1]


# In[25]:


for j in a:
    print(j)


# In[26]:


a = numpy.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]
])


# In[27]:


a[2,3]


# In[28]:


a[:2, 1:3]


# In[29]:


lower_axes=a[1:2, :]


# In[30]:


lower_axes


# In[31]:


lower_axes.ndim


# In[32]:


same_axes=a[1:2,:]


# In[33]:


same_axes


# In[34]:


a[:,1]


# In[35]:


a[:,1:2]


# In[36]:


a[:,1:3]


# In[37]:


for row in a:
    print(row)


# In[38]:


for r in a.flat:
    print(r)


# #.flat function helps to make multidimentional array behave like 1-dimentional array for iteration

# In[ ]:





# In[ ]:




