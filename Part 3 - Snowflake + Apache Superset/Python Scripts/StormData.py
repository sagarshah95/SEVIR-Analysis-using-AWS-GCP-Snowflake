#!/usr/bin/env python
# coding: utf-8

# In[1]:


import snowflake.connector as sf
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 100)
from snowflake.connector.pandas_tools import write_pandas
from pandas import DataFrame


# In[37]:


# From the web for the d2019_c20210223 from 2019 and 2020

print('Web Scrapping Started')

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

# df_catlog = pd.read_csv(r'C:\sevir\CATALOG.csv',encoding='utf8', engine='python')

# df_catlog.columns = map(str.upper, df_catlog.columns)
print('Web Scrapping Ended')

# In[38]:


# Preprocessing Data

df_details.DAMAGE_PROPERTY = df_details.DAMAGE_PROPERTY.str.replace('[K,M,B]','').astype(float).sum()

df_details.DAMAGE_CROPS = df_details.DAMAGE_CROPS.str.replace('[K,M,B]','').astype(float)


# In[39]:


print('For Details of Min and Max Dates')
print(min(df_details.BEGIN_DATE_TIME))
print(max(df_details.BEGIN_DATE_TIME))


# In[40]:


## SnowFlake Connection


# In[41]:
print('Snowflake Started')

ctx = sf.connect(
    user = 'xxx',
    password = 'xxx',
    account = 'xxx.aws',
    warehouse = 'xxx',
    database = 'xxx',
    schema = 'xxx'
)
cs = ctx.cursor()


# In[42]:



cs.execute('''CREATE OR REPLACE TABLE location(
    YEARMONTH int,
    EPISODE_ID int,
    EVENT_ID int,
    LOCATION_INDEX int,
    RANGE float,
    AZIMUTH varchar(255),
    LOCATION varchar(255),
    LATITUDE float,
    LONGITUDE float,
    LAT2 int, 
    LON2 int)''')

write_pandas(ctx, df_location, "LOCATION")


# In[43]:


# Adding the Fatality Table to Snowflake

cs.execute('''CREATE OR REPLACE TABLE fatality(
    FAT_YEARMONTH int,
    FAT_DAY int,
    FAT_TIME int,
    FATALITY_ID int,
    EVENT_ID int,
    FATALITY_TYPE varchar(255),
    FATALITY_DATE datetime,
    FATALITY_AGE int,
    FATALITY_SEX varchar(255),
    FATALITY_LOCATION varchar(255), 
    EVENT_YEARMONTH int)''')

write_pandas(ctx, df_fatal, "FATALITY")


# In[44]:


# Adding the Details Table to Snowflake

cs.execute('''CREATE OR REPLACE TABLE details(
    BEGIN_YEARMONTH int,
    BEGIN_DAY int,
    BEGIN_TIME int,
    END_YEARMONTH int,
    END_DAY int,
    END_TIME int,
    EPISODE_ID int,
    EVENT_ID int,
    STATE varchar(255),
    STATE_FIPS int, 
    YEAR int,
    MONTH_NAME varchar(255),
    EVENT_TYPE varchar(255),
    CZ_TYPE varchar(255),
    CZ_FIPS int,
    CZ_NAME varchar(255),
    WFO varchar(255),
    BEGIN_DATE_TIME varchar(255),
    CZ_TIMEZONE varchar(255),
    END_DATE_TIME varchar(255),
    INJURIES_DIRECT int,
    INJURIES_INDIRECT int,
    DEATHS_DIRECT int,
    DEATHS_INDIRECT int,
    DAMAGE_PROPERTY float,
    DAMAGE_CROPS float,
    SOURCE varchar(255),
    MAGNITUDE float,
    MAGNITUDE_TYPE varchar(255),
    FLOOD_CAUSE varchar(255),
    CATEGORY varchar(255),
    TOR_F_SCALE varchar(255),
    TOR_LENGTH int,
    TOR_WIDTH int,
    TOR_OTHER_WFO varchar(255),
    TOR_OTHER_CZ_STATE varchar(255),
    TOR_OTHER_CZ_FIPS varchar(255),
    TOR_OTHER_CZ_NAME varchar(255),
    BEGIN_RANGE float,
    BEGIN_AZIMUTH varchar(255),
    BEGIN_LOCATION varchar(255),
    END_RANGE float,
    END_AZIMUTH varchar(255),
    END_LOCATION varchar(255),
    BEGIN_LAT float,
    BEGIN_LON float,
    END_LAT float,
    END_LON float,
    EPISODE_NARRATIVE varchar(25500),
    EVENT_NARRATIVE varchar(25500),
    DATA_SOURCE varchar(255))''')

write_pandas(ctx, df_details, "DETAILS")


print('Snowflake Ended')

# In[27]:


# Adding the Catalog Table to Snowflake

# cs.execute('''CREATE OR REPLACE TABLE catlog(
#     id varchar(255),
#     file_name varchar(2550),
#     file_index int,
#     img_type varchar(255),
#     time_utc datetime,
#     minute_offsets varchar(25500),
#     episode_id int,
#     event_id int,
#     EVENT_TYPE varchar(255),
#     llcrnrlat float,
#     llcrnrlon float, 
#     urcrnrlat float,
#     urcrnrlon float,
#     proj varchar(255),
#     size_x int,
#     size_y int,
#     height_m int,
#     width_m int,
#     data_min float,
#     data_max float,
#     pct_missing float)''')

# write_pandas(ctx, df_catlog, "CATLOG")


# In[ ]:





# In[ ]:





# In[ ]:




