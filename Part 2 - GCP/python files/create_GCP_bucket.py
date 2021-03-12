#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from google.cloud import storage
import os

# Provide path for service accounts keys for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\shahs\.config\keys.json"


# In[ ]:


# Instantiates a client
storage_client = storage.Client()
my_bucket_name = "sevir" # Replace [my-bucket-name] with actual bucket name


# In[ ]:


bucket = storage_client.create_bucket(my_bucket_name)
msg = f"Bucket with name {bucket.name} has been created"
print(msg)

