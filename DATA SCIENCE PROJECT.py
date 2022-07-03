#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv("C:\\Users\\ACER\\Downloads\\country_wise_latest.csv")
data.head()


# In[3]:


data.columns


# In[4]:


data.tail()


# In[5]:


data.describe()


# In[6]:


sns.relplot(x="Confirmed",y="Recovered",data=data)


# In[7]:


sns.relplot(x="Confirmed",y="Active",data=data)


# In[8]:


sns.relplot(x="New cases",y="New recovered",data=data)


# In[9]:


sns.relplot(x="Confirmed",y="Active",hue="Recovered",data=data)


# In[10]:


sns.pairplot(data)


# In[13]:


sns.relplot(x="Confirmed",y="Active",kind='line',data=data)


# In[14]:


sns.relplot(x="New cases",y="New recovered",kind='line',data=data)


# In[15]:


data.columns


# In[17]:


sns.catplot(x='Confirmed',y='Recovered',data=data)


# In[ ]:




