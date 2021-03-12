#!/usr/bin/env python
# coding: utf-8

# In[25]:


from google.cloud import storage
import os
import io
from io import BytesIO
import pandas as pd

# Provide path for service accounts keys for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\shahs\.config\keys.json"


# In[26]:


# Instantiates a client
storage_client = storage.Client()
bucket = storage_client.get_bucket('sevir')


# In[27]:


filename = [filename.name for filename in list(bucket.list_blobs(prefix='')) ]
filename


# In[28]:


length=len(filename)


# In[29]:


print(length)


# In[31]:


for i in range(length):
    df = pd.read_csv(
    io.BytesIO(
                 bucket.blob(blob_name = filename[i]).download_as_string() 
              ) ,
                 encoding='UTF-8',
                 sep=',')
    print("==================================================")
    print(filename[i])
    print(df.head(5))


# In[ ]:




