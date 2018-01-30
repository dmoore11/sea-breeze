"""
Test document to test filters out one by one utilizing the same input files for the actual document.
"""


import numpy as np
import math as m
import pandas as pd
import os.path

import DetAlg


#changes when more/less data is introduced
Station_list=["DRHB","DBLK","DSMY"]

#set years of interest
Year_list=[2013,2014,2015,2016,2017]


yrcnt=0 #initialize year count
while(yrcnt<len(Year_list)): #loop through years of interest
    year=Year_list[yrcnt]
    if year==2013 or year==2014 or year==2015 or year==2017:
        numdays=365
    else:
        numdays=366 #2016 is a leap year

    #initialize
    #Sea_breeze=np.zeros((numdays,len(Station_list)))
    #Filter12=np.zeros((numdays,len(Station_list)))
    Filter3=np.zeros(numdays)
    #Date=np.zeros(numdays)

    stcnt=0 #initialize station count every time year changes
    while(stcnt<len(Station_list)): #loop thru stations
        station=Station_list[stcnt]

        path_name="/Volumes/LaCie/SeaBreeze/OriginalData/StationData/"
        suffix=".dat"
        infile=open(os.path.join\
        (path_name,str(year),station+str(year)+suffix),"r")

        #if stcnt==0: #first pass, fill Date array
            #Date=ReadDate.date(infile,numdays)

        #we send data to filt12 to test for sea breeze based on
        #winddir and temp drop over 30 min intervals - sea sub
        #Filter12[:,stcnt]=DetAlg.filt12(infile,station,numdays)

        #Tests for precipitation at any station for each day
        #replaces each 0 with 1 if there is a precip at each
        #individual station.
        Filter3=DetAlg.filt3(infile,Filter3,numdays)

        stcnt+=1
    yrcnt+=1

