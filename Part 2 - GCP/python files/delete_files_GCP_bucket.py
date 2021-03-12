#!/usr/bin/env python
# coding: utf-8

# In[1]:


from google.cloud import storage
import os
import io
from io import BytesIO
import pandas as pd

# Provide path for service accounts keys for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\shahs\.config\keys.json"


# In[2]:


# Instantiates a client
storage_client = storage.Client()
bucket = storage_client.get_bucket('sevir_data')


# In[3]:


filename = [filename.name for filename in list(bucket.list_blobs(prefix='')) ]
filename


# In[4]:


length=len(filename)
print(length)


# In[7]:


for i in range(length):
    DELETE_FILE = filename[i]
    bucket = storage_client.get_bucket('sevir_data')
    blob = bucket.blob(DELETE_FILE)
    blob.delete()
    print("deleted file " + filename[i])


# In[ ]:




