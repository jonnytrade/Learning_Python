from turtle import *
from time import sleep
pu()
bk(300)
pd()
n=5
m=11
for i in range(n):
    fd(200)
    ang=n//2*360/n
    left(ang)
pu()
fd(300)
pd()
for i in range(m):
    fd(200)
    ang=m//2*360/m
    left(ang)
sleep(3)



