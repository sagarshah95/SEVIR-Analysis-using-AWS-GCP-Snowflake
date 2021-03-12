CREATE OR REPLACE TABLE location(\n",
    "    YEARMONTH int,\n",
    "    EPISODE_ID int,\n",
    "    EVENT_ID int,\n",
    "    LOCATION_INDEX int,\n",
    "    RANGE float,\n",
    "    AZIMUTH varchar(255),\n",
    "    LOCATION varchar(255),\n",
    "    LATITUDE float,\n",
    "    LONGITUDE float,\n",
    "    LAT2 int, \n",
    "    LON2 int)