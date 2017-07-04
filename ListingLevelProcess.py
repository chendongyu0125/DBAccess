
# coding: utf-8

# In[2]:

import pandas as pd
import pymysql
from sqlalchemy import create_engine
e=create_engine("mysql+pymysql://chendongyu:1234@localhost/prosper?charset=utf8")
listings = pd.read_sql("r_listing",e,parse_dates=True)
listings.info()


# In[9]:

listings['CreationDate']=pd.to_datetime(listings['CreationDate'])
list_sorted=listings.sort_values(['MemberKey', 'CreationDate'], ascending=[1, 1])
list_sorted[['MemberKey', 'CreationDate','AmountRequested','Status']].head(100)


# In[4]:




# In[8]:




# In[ ]:



