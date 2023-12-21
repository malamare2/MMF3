import math
import numpy as np
import matplotlib as plt

eps =1e-6
t = 0

def y_0(t):
    y = math.sin(2*t)-2*math.cos(t)
    return y

a = 1
b = 2
if (y_0(a)*y_0(b)<=0):
    c=a
    while ((b-a)>=eps):
        c =(a+b)/2
        
        #provjera jeli c nul-tocka
        if (y_0(c) ==0.0):
            break

        #bira se strana
        if (y_0(c)*y_0(a) <0):
            b=c
        else:
            a=c
        t = t+1

print(y_0(c))




def y_1(t):
    y1 = 2*math.cos(2*t)+2*math.sin(t)
    return y1

x0 =1
while abs(y_0(x0)/y_1(x0)) >= eps:
    x0 = x0 - y_0(x0)/y_1(x0)
    t = t+1
print ("t={}; x = {}; y_0 = {}".format(t,"%4f"%x0,y_0(x0)))