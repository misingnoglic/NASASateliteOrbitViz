from urllib import urlretrieve
#from visual import *
from orbit import * 

DataURL = "http://www.celestrak.com/NORAD/elements/stations.txt"
urlretrieve(DataURL,"stations.txt")
#issData = []
with open("stations.txt") as stations:
    issdata=[stations.next() for x in xrange(3)]
data = "".join(issdata)
data = data.split("\n")
ISS = Orbit(data[0],data[1],data[2])
ISS.printstuff()
