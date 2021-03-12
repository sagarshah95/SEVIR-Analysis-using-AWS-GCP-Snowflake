//Query 1 to select total death by the states//
SELECT STATE, 
        SUM(DEATHS_DIRECT) AS TOTAL_DEATHS
FROM DETAILS
GROUP BY STATE
ORDER BY TOTAL_DEATHS DESC

//Query 2 to select total death by the states//
SELECT  d.EVENT_TYPE,  
        COUNT(d.EVENT_ID) as Number_of_Fatalites
FROM DETAILS d
INNER JOIN FATALITY f ON d.EVENT_ID = f.EVENT_ID
GROUP BY d.EVENT_TYPE
ORDER BY Number_of_Fatalites DESC


//Query 3 to show number of 
SELECT fat_yearmonth, COUNT(*) AS TOTAL_DEATHS
FROM fatality
GROUP BY fat_yearmonth
ORDER BY fat_yearmonth


// Query 4 to the see death distribution by State and Event Type

SELECT  d.STATE,  
        d.EVENT_TYPE,
        COUNT(d.EVENT_ID) as Number_of_Fatalites
FROM DETAILS d
INNER JOIN FATALITY f ON d.EVENT_ID = f.EVENT_ID
GROUP BY d.STATE, d.EVENT_TYPE
ORDER BY Number_of_Fatalites DESC


// Query 5 

SELECT  l.LOCATION,
        d.EVENT_TYPE,
        COUNT(d.EVENT_ID) as Number_of_Incidents
FROM DETAILS d
INNER JOIN LOCATION l ON d.EVENT_ID = l.EVENT_ID
GROUP BY l.LOCATION, d.EVENT_TYPE
ORDER BY Number_of_Incidents DESC


