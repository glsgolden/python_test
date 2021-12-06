#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=10
b=20
c=a+b
c


# In[3]:


id(a)


# In[4]:


d=10


# In[5]:


id(d)


# In[12]:


import pandas as pd

df = pd.read_excel(r'G:\gshirsat\Documents\Book1.xlsx')
print (df)


# In[14]:


df.head(3)


# In[15]:


a= 11
b=11
print(id(a),id(b))


# In[16]:


a=30
b=a
print(id(a),id(b))


# In[17]:


a=50
b


# In[18]:


print(id(a),id(b))


# In[19]:


a=30
b=a
print(id(a),id(b))


# In[20]:


b=60
a


# In[21]:


cf=df
print(id(cf),id(df))


# In[ ]:




