#!/usr/bin/env python
# coding: utf-8

# In[1]:


try:
    from google.cloud import storage
    import google.cloud.storage
    import json
    import os
    import sys
except Exception as e:
    print("Error : {} ".format(e))


# In[2]:


PATH = os.path.join(os.getcwd() , r'C:\Users\shahs\.config\keys.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = PATH


# In[3]:


storage_client = storage.Client(PATH)


# In[4]:


bucket = storage_client.get_bucket('sevir')


# In[6]:


filename = [filename.name for filename in list(bucket.list_blobs(prefix='')) ]
print(filename)


# In[ ]:




