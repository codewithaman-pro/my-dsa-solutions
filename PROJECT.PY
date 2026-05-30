import math 
from turtle import*
ht()
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
speed(0)
bgcolor("white")
for i in range(9000):
    speed(0)
    goto (hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("#f73487")
        goto(0,0)
        done()
        

