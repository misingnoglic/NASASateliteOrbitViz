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
for i in range(20):
    with open("stations.txt") as stations:
        issdata=[stations.next() for x in xrange(i*3,(i*3)+3)]
    data = "".join(issdata)
    data = data.split("\n")
    ISS = twoline2rv(data[1],data[2],wgs72)
    SatData+=[ISS]
#print SatData    
year=2000
month=6
day=29
hour=12
minute=50
second=19
earth = sphere(pos=(0,0,0),radius=6000,color=color.blue)
orbits = [None for x in SatData]
for i in range(len(SatData)):
    position, velocity = SatData[i].propagate(year, month, day, hour, minute, second)
    #position = [x/1000.0 for x in position]
    #print position
    orbits[i]= sphere(pos=tuple(position),radius=1000,make_trail=True,color=(rn.random(), rn.random(), rn.random()))
    
    #sleep(5)
    #print("CHanged")
#New=zip(SatData,orbits)
#print(New)
print(orbits)
x=0
while True:
    sleep(.01)
    rate(30)
    x+=1
    #p=0
    for i in range(len(SatData)):
        position, velocity = SatData[i].propagate(year, month, day, hour, minute, second+x)
        
        #print(position)
        if position!=None:
            #position = [x/1000 for x in position]
            orbits[i].pos=tuple(position)
        #p+=1
        #print(p)
line1 = ('1 00005U 58002B   00179.78495062  ''.00000023  00000-0  28098-4 0  4753')
line2 = ('2 00005  34.2682 348.7242 1859667 ''331.7664  19.3264 10.82419157413667')
satellite = twoline2rv(line1, line2, wgs72)
