from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv

from urllib import urlretrieve
from visual import *
from orbit import *
from time import sleep
import random as rn

DataURL = "http://www.celestrak.com/NORAD/elements/stations.txt"
urlretrieve(DataURL,"stations.txt")
SatData = []
stations = open("stations.txt").read()
TwoLineData = stations.split("\n")

for i in range(0,len(TwoLineData)-1,3):
    
    name = TwoLineData[i]
    ISSline1 = TwoLineData[i+1]
    ISSline2 = TwoLineData[i+2]

    ISS = twoline2rv(ISSline1, ISSline2,wgs72)
    SatData.append(ISS)
   
year=2013
month=9
day=8
hour=12
minute=50
second=19
earth = sphere(pos=(0,0,0),radius=6000,color=color.blue)
orbits = [None for x in SatData]
for i in range(len(SatData)):
    #if i!=4:
        try:
            t = SatData[i].propagate(year, month, day, hour, minute, second)
            print t
            position, velocity = t
            print(i)
            #print position
            orbits[i]=(sphere(pos=tuple(position),radius=100,make_trail=True, retain=250, color=(rn.random(), rn.random(), rn.random())))
        except TypeError:
            print "sorry"

print(orbits)
x=0
while True:
    sleep(.01)
    rate(30)
    x+=1
    for i in range(len(SatData)):
        try:
            position, velocity = SatData[i].propagate(year, month, day, hour, minute+x, second)
            
            if position!=None:
                orbits[i].pos=tuple(position)
        except:
            pass
            #print "skip"
