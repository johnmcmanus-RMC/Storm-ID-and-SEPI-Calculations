# CoastalSedsCode
Python code for STORMINESS Research
This code accesses the NOAA web services to gather data from multiple tidal stations
The collection of fifteen programs forms a pipeline that: 
1.	Gets the raw station data from NOAA (3 programs), computes the current epoch MSL for each station (1 program)
  a.	Multi Station Tide CodeV1 - MSL- Base Value.py
2.	Computes the monthly average MSL for each station (3 programs)
  a.	Multi Station Tide CodeV4 - MSL - Average.py
  b.	Multi Station Tide CodeV4 - MSL – Average – AC Start.py
  c.	Multi Station Tide CodeV4 - MSL – Average – AC End.py
3.	Computes the monthly average MHW for each station (3 programs)
  a.	Multi Station Tide CodeV4 - MHW-Average.py
  b.	Multi Station Tide CodeV4 - MHW-Average – AC Start.py
  c.	Multi Station Tide CodeV4 - MHW-Average – AC End.py
4.	Fixes the raw station data from NOAA (1 program)
  a.	Multi Station Predicted Value Correction Code V1.py
5.	Computes the annual surge values using the “fixed data” (1 program)
  a.	Multi Station Annual Surge Code V3.py
6.	Processes the final data to generate storms and SEPI (2 versions, one with surge threshold calculated over the whole data set, and one with annual surge thresholds). 
  a.	Multi Station Tides Processing Code Single Surge V2 - UI for SD.py
  b.	Multi Station Tides Processing Code Annual Surge V2.py
7.	There is a user defines abstract data type used to store the data objects and help to manage making sure the data elements are aligned correctly (the monthly or annual values are applied to the correct months or years). 
  a.	tideData.py
  
The break in the Atlantic City data in 1970 requires that we treat Atlantic City as a special case. That is why some of the programs have three variants: one for Atlantic City from 1922 to the end of 1969, one for Atlantic City starting in 1971, and one for all the other stations.
