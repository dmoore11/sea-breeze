"""
Daniel Moore

The purpose of this module will be to ingest daily data from DEOS
with 5 minute temporal scale and simply print out dates.

"""

import numpy as np
import math as m


#needs input file sent to module in format:
#infile = open ("/Users/dpmoore2927/Desktop/Test.csv", "r")
def date(infile):

    #read data
    obs_list=infile.readlines()

    #initialize values
    k=0;day=0
    date=np.zeros(365)

    #loop reading the data
    for obs in obs_list[1:]:
        day=float(obs.split(",")[0])

        if k==0:
            date[k]=day
            k+=1
        elif day!=date[k-1]:
            date[k]=day
            k+=1

    infile.seek(0)
    return date
