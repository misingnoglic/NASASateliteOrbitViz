from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv

from urllib import urlretrieve
from visual import *
from orbit import *
from time import sleep

DataURL = "http://www.celestrak.com/NORAD/elements/stations.txt"
urlretrieve(DataURL,"stations.txt")
#issData = []
with open("stations.txt") as stations:
    issdata=[stations.next() for x in xrange(3)]
data = "".join(issdata)
data = data.split("\n")

ISS = twoline2rv(data[1],data[2],wgs72)
year=2000
month=6
day=29
hour=12
minute=50
second=19

position, velocity = ISS.propagate(year, month, day, hour, minute, second)
position = [x/1000.0 for x in position]
ball= sphere(pos=tuple(position),radius=.1,make_trail=True)
#ball2 = sphere(pos=(0,0,0),radius=1)
#sleep(5)
#print("CHanged")
x=0
while True:
    sleep(1)
    rate(30)
    x+=.1
    position, velocity = ISS.propagate(year, month, day, hour, minute, second+x)
    
    #print(velocity)
    if position!=None:
        position = [x/1000 for x in position]
        ball.pos=tuple(position)
#ball.pos=tuple(position)

line1 = ('1 00005U 58002B   00179.78495062  ''.00000023  00000-0  28098-4 0  4753')
line2 = ('2 00005  34.2682 348.7242 1859667 ''331.7664  19.3264 10.82419157413667')
satellite = twoline2rv(line1, line2, wgs72)
