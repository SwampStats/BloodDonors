
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import matplotlib as plt


# In[17]:


datapath = "../data/raw/"


# In[18]:


df = pd.read_csv(datapath+"transfusion.data")


# In[19]:


df=df.rename({'Recency (months)': 'MonthsSinceLast', 'Frequency (times)': 'DonationCount', 'Monetary (c.c. blood)': 'VolumeDonated', 'Time (months)'
             : 'MonthsSinceFirst', 'whether he/she donated blood in March 2007': 'March2007_YorN'}, axis=1)


# In[20]:


### names={'MonthsSinceLast', 'Frequency', 'Volume', 'MonthsSinceFirst', 'March2007_YesNo'}


# In[21]:


df.head()


# In[22]:


donor_train = df[:500]


# In[23]:


donor_test = df[500:]


# In[24]:


donor_train.describe()


# In[25]:


donor_test.head()


# In[26]:


donor_X_train = donor_train.loc['MonthsSinceLast':'MonthsSinceFirst',:]


# In[27]:


donor_y_train = donor_train['March2007_YorN']


# In[28]:


donor_y_train.describe()


# In[29]:


donor_X_test = donor_test.loc['MonthsSinceLast':'MonthsSinceFirst',:]


# In[30]:


donor_y_test = donor_test['March2007_YorN']


# In[36]:


get_ipython().run_line_magic('pinfo', 'pd')


# In[39]:





# In[ ]:




