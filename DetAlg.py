"""
Daniel Moore

The purpose of this module will be to ingest daily data from DEOS
with 5 minute temporal scale.

"""

import numpy as np
import math as m
import csv


#needs input file sent to module in format:
#infile = open ("/Users/dpmoore2927/Desktop/Test.csv", "r")
def det5min(infile,station):

    #read data
    obs_list=infile.readlines()
    n=len(obs_list)

    #initialize values
    k=0;i=0;day=0
    date=np.zeros(365,float);winddir=np.zeros(n)
    temp=np.zeros(n);sbb=np.zeros(365)

    #loop reading the data
    for obs in obs_list[1:]:
        day=float(obs.split(",")[0])

        if i==0:
            date[k]=day
            k+=1
        elif day!=date[k-1]:
            date[k]=day
            k+=1

        if obs.split(",")[2]=="" and obs.split(",")[5]==""\
         or obs.split(",")[5]=="NAN":
            temp[i]=999
            winddir[i]=999
        elif obs.split(",")[2]=="":
            temp[i]=999
            winddir[i]=float(obs.split(",")[5])
        elif  obs.split(",")[5]=="" or obs.split(",")[5]=="NAN":
            winddir[i]=999
            temp[i]=float(obs.split(",")[2])
        else:
            temp[i]=float(obs.split(",")[2])
            winddir[i]=float(obs.split(",")[5])

            if sbb[k-1]==1:
                i+=1
                continue


            #Testing whether the criteria are met
            #Gilchrist method:
            if i>5:

                if temp[i]==999 or temp[i-6]==999 or \
                winddir[i]==999 or winddir[i-6]==999:

                    sbb[k-1]=0
                    i+=1
                    continue

                if np.absolute(winddir[i-6]-winddir[i])<=180 and \
                np.absolute(winddir[i-6]-winddir[i])>=160:

                    if (temp[i-6]-temp[i])<=-1:
                        sbb[k-1]=1
                        #print(date[k-1])
                    else:
                        sbb[k-1]=0

                elif np.absolute(winddir[i-6]-winddir[i])>180 and \
                (360-np.absolute(winddir[i-6]-winddir[i]))>=160:

                    if (temp[i-6]-temp[i])<=-1:
                        sbb[k-1]=1

                    else:
                        sbb[k-1]=0

                else:
                    sbb[k-1]=0

        i+=1


#Print
    """
    count=0
    sbbcount=0
    while (count<365):
        if sbb[count]==1:
            sbbcount+=1
        count+=1
    print('The total number of sea breeze days at\
    detected in 2015 is',sbbcount)
    """
    print(station,sum(sbb))
    return sbb









def det1hr(infile,outfile):

    #read data
    obs_list=infile.readlines()
    n=len(obs_list)

    #initialize values
    k=0;i=0;day=0
    date=np.zeros(365,float);winddir=np.zeros(n)
    temp=np.zeros(n);sbb=np.zeros(365)

    #loop reading the data
    for obs in obs_list[1:]:
        day=float(obs.split(",")[0])

        if i==0:
            date[k]=day
            k+=1
        elif day!=date[k-1]:
            date[k]=day
            k+=1

        if obs.split(",")[2]=="":
            temp[i]=999
            winddir[i]=float(obs.split(",")[5])
        elif  obs.split(",")[5]=="" or obs.split(",")[5]=="NAN":
            winddir[i]=999
            temp[i]=float(obs.split(",")[2])
        else:
            temp[i]=float(obs.split(",")[2])
            winddir[i]=float(obs.split(",")[5])

            if sbb[k-1]==1:
                i+=1
                continue


            #Testing whether the criteria are met
            #Gilchrist method:
            if i>5:

                if temp[i]==999 or temp[i-1]==999 or \
                winddir[i]==999 or winddir[i-1]==999:

                    sbb[k-1]=0
                    i+=1
                    continue

                if np.absolute(winddir[i-1]-winddir[i])<=180 and \
                np.absolute(winddir[i-1]-winddir[i])>=160:

                    if (temp[i-1]-temp[i])<=-1:
                        sbb[k-1]=1
                        #print(date[k-1])
                    else:
                        sbb[k-1]=0

                elif np.absolute(winddir[i-1]-winddir[i])>180 and \
                (360-np.absolute(winddir[i-1]-winddir[i]))>=160:

                    if (temp[i-1]-temp[i])<=-1:
                        sbb[k-1]=1

                    else:
                        sbb[k-1]=0

                else:
                    sbb[k-1]=0

        i+=1

#Print

    count=0
    sbbcount=0
    while (count<365):
        if sbb[count]==1:
            sbbcount+=1
        count+=1
    print('The total number of sea breeze days at',str(station),\
    'detected is',sbbcount)
