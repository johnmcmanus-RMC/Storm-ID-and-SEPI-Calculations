# @author: John McManus
# © 2023. This work is licensed under a CC BY-NC-SA 4.0 license
# MultiStation Wave Bouy Data analysis
# Program to query the NOAA Data source to get Wave Bouy data

import requests

def main():
   
   stationID = [44027, 44098, 44097, "buzm3", 44008, 44025, 44065, 44066, 44009, 44099, 41025, 41013, 41004, 41009]
   stationStart = [2003, 2008, 2009, 1997, 1982, 1991, 2008, 2009, 1986,2008, 2003, 2003, 1994, 1988]
   stationName = ["Jonesport, ME ", "Jeffrey's Ledge, NH", "Block Island, RI", "Buzzards Bay, MA", "NANTUCKET", "LONG ISLAND", "Breezy Point, NY",
                  "Long Beach, NJ", "Cape May, NJ", "Cape Henry, VA", "Diamond Shoals, NC", "Frying Pan Shoals, NC", "Charleston, SC", "Cape Canaveral, FL"]
   
   # Create the request string
   requestStringWaves = "https://www.ndbc.noaa.gov/view_text_file.php?filename=%sh%d.txt.gz&dir=data/historical/stdmet/"
   
   
   for i in range (len(stationID)):
      # Open the output file
      fileName = stationName[i] + ".csv"
      fileOut = open(fileName, "w")
      fileOut.write("The station ID is: %s \n" % stationID[i])
      fileOut.write("MM/DD/YY hh:00, WVHT, DPD \n")
      

      for year in range (stationStart[i], 2022):
         urlWaves = (requestStringWaves % (stationID[i], year))
         
         # Send the data request and store the response
         response = requests.get(urlWaves)
         
         # Get the number of data elements in the response
         responseLength = len(response.text)
         print("The response text has %d elements" % responseLength)
         
         # Split the response into a list of data elements
         data = response.text.split("\n")
         print("The response has %d lines of data" % len(data))
         
         
         outputData = data[0].split()
         if len(data) > 4:
            if outputData[4].lower() == "mm":
               minutes = True
            else:
               minutes = False
            index = outputData.index("WVHT")
         else:
            index = 0
            
         for j in range (len(data) - 1):
            outputData = data[j].split()
            if outputData[1][0].isdigit():
               if minutes:
                  date = ("%s/%s/%s %s:%s" % (outputData[1],outputData[2], outputData[0], outputData[3], outputData[4]))
               else:
                  date = ("%s/%s/%s %s:%s" % (outputData[1],outputData[2], outputData[0], outputData[3], "00"))
               fileOut.write("%s, " % (date))   
               fileOut.write("%s, " % (outputData[index]))
               fileOut.write("%s, " % (outputData[index + 1]))
               fileOut.write("\n")

   # close the output file
   fileOut.close()
   
# call the main 
main()