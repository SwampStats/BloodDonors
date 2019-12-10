
# coding: utf-8

# In[26]:


import pandas as pd
import numpy as np
import matplotlib as plt


# In[27]:


datapath = "../data/raw/"


# In[28]:


df = pd.read_csv(datapath+"transfusion.data")


# In[29]:


df=df.rename({'Recency (months)': 'MonthsSinceLast', 'Frequency (times)': 'DonationCount', 'Monetary (c.c. blood)': 'VolumeDonated', 'Time (months)'
             : 'MonthsSinceFirst', 'whether he/she donated blood in March 2007': 'March2007_YorN'}, axis=1)


# In[30]:


### names={'MonthsSinceLast', 'Frequency', 'Volume', 'MonthsSinceFirst', 'March2007_YesNo'}


# In[31]:


df.head()


# In[43]:


donor_train = df[:500]


# In[44]:


donor_test = df[500:]


# In[45]:


donor_train.describe()


# In[46]:


donor_test.head()


# In[50]:


donor_X_train = donor_train.loc['MonthsSinceLast':'MonthsSinceFirst',:]


# In[57]:


donor_y_train = donor_train['March2007_YorN']


# In[58]:


donor_y_train.describe()


# In[59]:


donor_X_test = donor_test.loc['MonthsSinceLast':'MonthsSinceFirst',:]


# In[60]:


donor_y_test = donor_test['March2007_YorN']


# In[61]:




