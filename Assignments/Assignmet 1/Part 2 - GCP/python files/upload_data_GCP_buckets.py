#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import os
from google.cloud import storage


# In[21]:


# Provide path for service accounts keys for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\shahs\.config\keys.json"


# In[22]:


# Instantiates a client
storage_client = storage.Client()


# In[3]:


# From the web for the d2019_c20210223 from 2019 and 2020

# 2019
df_details_2019 = pd.read_csv('https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d2019_c20210223.csv.gz', compression='gzip', 
                         header=0, sep=',', quotechar='"')
df_location_2019 = pd.read_csv('https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_locations-ftp_v1.0_d2019_c20210223.csv.gz', compression='gzip', 
                         header=0, sep=',', quotechar='"')
df_fatal_2019 = pd.read_csv('https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_fatalities-ftp_v1.0_d2019_c20210223.csv.gz', compression='gzip', 
                         header=0, sep=',', quotechar='"')

# 2020
df_details_2020 = pd.read_csv('https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d2020_c20210223.csv.gz', compression='gzip', 
                         header=0, sep=',', quotechar='"')
df_location_2020 = pd.read_csv('https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_locations-ftp_v1.0_d2020_c20210223.csv.gz', compression='gzip', 
                         header=0, sep=',', quotechar='"')
df_fatal_2020 = pd.read_csv('https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_fatalities-ftp_v1.0_d2020_c20210223.csv.gz', compression='gzip', 
                         header=0, sep=',', quotechar='"')


df_details = pd.concat([df_details_2019, df_details_2020], ignore_index=True)

df_location = pd.concat([df_location_2019, df_location_2020], ignore_index=True)

df_fatal = pd.concat([df_fatal_2019, df_fatal_2020], ignore_index=True)


# In[28]:


df_details.to_csv(r'stormDetails.csv', index = False, encoding='utf-8')


# In[29]:


df_location.to_csv(r'stormLocation.csv', index = False, encoding='utf-8')


# In[30]:


df_fatal.to_csv(r'stormFatal.csv', index = False, encoding='utf-8')


# In[36]:


filename= ['sevir.csv','stormDetails.csv','stormLocation.csv','stormFatal.csv']


# In[37]:


length=len(filename)


# In[38]:


print(length)


# In[40]:


for i in range(length):
    print(filename[i])
    UPLOADFILE = os.path.join(os.getcwd(), filename[i])
    bucket = storage_client.get_bucket('sevir_data')
    blob = bucket.blob(filename[i])
    blob.upload_from_filename(UPLOADFILE)


# In[ ]:




