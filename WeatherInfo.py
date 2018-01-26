"""
Daniel Moore

Purpose of this program is to ingest a file and spit out Sea Breeze
Days detected using the DetAlg module with either the 5min data
function or the 1hr data function

YY MM DD hh mn degT relH wspd wdir GST
"""


import numpy as np
import math as m
import DetAlg
import ReadDate
import os.path

np.set_printoptions(threshold=np.inf)

Station_list=["DRHB","DIRL","DBNG","DBBB","DWAR","DSBY",\
"DSTK","DELN","DHAR","DJCR","DBRG","DLAU","DSJR"]

#year_list=np.arange(2013,2018)

#station="DRHB"
year="2013"

Sea_breeze=np.zeros((295,len(station_list)+1))


cnt=0
while(cnt<len(station_list)):
    station=station_list[cnt]

    path_name="/Users/dpmoore2927/Desktop/UD/Thesis/StationData/"
    mesonet="DEOS"
    suffix="_M.txt"
    infile=open(os.path.join\
    (path_name,year,mesonet,station+suffix),"r")
    if cnt==3:
        Sea_breeze[:,0]=ReadDate.date(infile,year)

    #which module depends on whether it's 5min or 1hr data
    #DetAlg.det1hr(infile)
    Sea_breeze[:,cnt+1]=DetAlg.det5min(infile,station,year)
    cnt+=1

#Read the first column to get date and put in first column of
#sea_breeze array

np.savetxt("/Users/dpmoore2927/Desktop/sea_breeze.csv",Sea_breeze,\
           delimiter=",")

#outfile=open("/Users/dpmoore2927/Desktop/sea_breeze.csv","w")
#print >> outfile,sea_breeze





