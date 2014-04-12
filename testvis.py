from visual import *
from time import sleep
import random as rn

shapes=[x for x in range(20)]
for x in range(20):
    shapes[x] = sphere(pos=(x,0,0),radius=1,color=(rn.random(), rn.random(), rn.random()))
n=0
while True:
    rate(30)
    sleep(1)
    n+=1
    for x in range(len(shapes)):
        shapes[x].pos=(shapes[x].pos[0]+n,0,0)
    
