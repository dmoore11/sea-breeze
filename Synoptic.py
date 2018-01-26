"""
Daniel Moore

The purpose of this module will be to ingest radiosonde data
to determine synoptic conditions related to sea breeze

"""

import numpy as np
import math as m

#needs input file

def rsonde(infile,date) #infile and requested date needed
                        #date is the date found to meet
                        #other requirements

    #read data
    obs_list=infile.readlines()
    n=len(obs_list)

    #intialize values
    synSBB=0;


    #find specified date
        #loops through obs in obs_list and finds date that
        #is input and previous date for WDdiff calc.


    #loop finding 700hPa height and then reading that data
    for obs in obs_list:
        """
        As per Lairde (1998), WDdiff in previous 24 hours
        must be less than 90 degrees. WSdiff in previous 12
        hours must be less than 6m/s and WS at time of SB
        must be less than 11m/s
        """


    return SynSBB
