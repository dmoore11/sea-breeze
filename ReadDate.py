"""
Daniel Moore

The purpose of this module will be to ingest daily data from DEOS
with 5 minute temporal scale and simply print out dates in a
decimal format.

"""

import numpy as np
import math as m


#needs input file sent to module in format:
#infile = open ("/Users/dpmoore2927/Desktop/Test.txt", "r")
#OR .csv
def date(infile,year):

    #read data
    obs_list=infile.readlines()

    #check year for number of days
    if year==2013 or year==2014 or year==2015 or year==2017:
        numdays=365
    else:
        numdays=366 #2016 is a leap year

    #initialize values
    k=0;yy=0;dd=0;mm=0;date=0
    Date=np.zeros(numdays)

    #loop reading the data
    for obs in obs_list[1:]:
        yy=float(obs.split()[0])
        mm=float(obs.split()[1])
        dd=float(obs.split()[2])

        date=(yy*10000)+(mm*100)+dd #puts date into format: yyyymmdd

        if k==0:
            Date[k]=date
            k+=1
        elif date!=Date[k-1]:
            Date[k]=date
            k+=1

    infile.seek(0)
    return Date
