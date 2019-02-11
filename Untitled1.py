#!/usr/bin/env python
# coding: utf-8

# In[66]:


import pandas as pd
import numpy as np


# In[ ]:


'''Data frame object : 
Read csv file
drop 
add a column
drop null values
replace null values with mean values
add two data objects
convert database to csv
'''


# In[7]:


pd.read_csv('C:\\Users\Yogesh\Desktop\Salaries.csv')


# In[6]:


pd.read_csv('.../Salaries.csv')


# In[14]:


df1=pd.DataFrame (numpy.random.randn(4,4),['a','b','c','d'],['P','Q','R','S'])


# In[15]:


df1


# In[21]:


df2=pd.DataFrame (numpy.random.randn(4,3),['a1','b1','c1','d1'],['P1','Q1','R1'])


# In[22]:


df2


# In[23]:


df1+df2


# In[36]:


df1.drop('S',axis=1,inplace=True)


# In[37]:


df1


# In[38]:


df1


# In[39]:





# In[45]:


df1['S']=df1['P']+df1['R']


# In[46]:


df1


# In[47]:


df1>0


# In[49]:


df1[df1>0]


# In[50]:


df1.drop('a',inplace=True)


# In[51]:


df1.drop('b',inplace=True)


# In[52]:


df1


# In[56]:


df1.loc['c']


# In[64]:


df1.loc[df1.index[1]]


# In[67]:


d={'A':{1,2,np.nan},'B':[5,np.nan],'C':[1,2,3]}


# In[68]:


d


# In[73]:


df = pd.DataFrame(d)


# In[ ]:




