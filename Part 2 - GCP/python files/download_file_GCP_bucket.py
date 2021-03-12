#!/usr/bin/env python
# coding: utf-8

# In[4]:


from google.cloud import storage
import os

# Provide path for service accounts keys for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\shahs\.config\keys.json"


# In[18]:


# Instantiates a client
storage_client = storage.Client()
bucket = storage_client.get_bucket('sevir_data')


# In[19]:


filename= ['sevir.csv','stormDetails.csv','stormLocation.csv','stormFatal.csv']


# In[20]:


length=len(filename)


# In[21]:


print(length)


# In[23]:


for i in range(length):
    blop = bucket.blob(blob_name = filename[i]).download_as_string()
    with open (filename[i], "wb") as f:
        f.write(blop)


# In[13]:





# In[ ]:




