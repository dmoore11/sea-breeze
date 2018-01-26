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
def det5min(infile,station,year):

    #read data
    obs_list=infile.readlines()
    n=len(obs_list)

    #check year for number of days
    if year==2013 or year==2014 or year==2015 or year==2017:
        numdays=365
    else:
        numdays=366 #2016 is a leap year

    #initialize values
    k=0;i=0;yy=0;mm=0;dd=0;date=0;
    Date=np.zeros(numdays,float);Winddir=np.zeros(n)
    Temp=np.zeros(n);Sbb=np.zeros(numdays)

    #loop reading the data
    for obs in obs_list[1:]:
        yy=float(obs.split()[0])
        mm=float(obs.split()[1])
        dd=float(obs.split()[2])

        date=(yy*10000)+(mm*100)+dd #puts date into format: yyyymmdd

        if i==0: #if first pass, sets date
            Date[k]=date
            k+=1
        elif date!=Date[k-1]: #after first pass, checks to see if current date
            Date[k]=date      #is different from previous
            k+=1

        if obs.split()[5]=="": #checks for missing data
            Temp[i]=999
        else:
            Temp[i]=float(obs.split()[5])
        if obs.split()[8]=="" or obs.split()[8]=="NAN":
            Winddir[i]=999
        else:
            Winddir[i]=float(obs.split()[8])

        if Temp[i]!=999 and Winddir[i]!=999:
            if Sbb[k-1]==1 #skips calculations if date has already
                i+=1       #been flagged as a sb day
                continue


            #Testing whether the criteria are met
            #Gilchrist method:
            if i>5: #will only continue if we can refer back a half hour
                    #in data
                if Temp[i-6]==999 or Winddir[i-6]==999:

                    Sbb[k-1]=0
                    i+=1
                    continue

                if 180>=np.absolute(Winddir[i]-Winddir[i-6])>=160 or \
                180>=(360-np.absolute(Winddir[i]-Winddir[i-6]))>=160:

                    if (Temp[i]-Temp[i-6])<=-1: #if temperature has dropped
                        Sbb[k-1]=1              #more than 1 degree (assign 1)
                    else:
                        Sbb[k-1]=0

                else:
                    Sbb[k-1]=0

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
    print(station,sum(Sbb))
    return Sbb







"""

def det1hr(infile,outfile): #outdated...

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

"""
