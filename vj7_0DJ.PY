#runge kuta je vj 8 git-hub
#oscilacija metalne kuglice
import numpy as np
import matplotlib.pyplot as plt 
import math

m = 200
l = 0.2484902028828339
g = 9.81
pi = 3.141592653589793

#y0_r = y0*pi/180 #pocetni kut u radijanima
    
def akceleracija(t, y, v): 
    return -g/l*np.sin(y)

def analiticki(t, y):
    return y*np.cos(np.sqrt(g/l)*t)

def Euler(t0, y0, v0, N):
    T = 2*pi*np.sqrt(l/g) #period
    t1 = t0
    t2 = 20*T
    
    y = [y0]
    t = [t0]
    v = [v0]
    h = (t2 - t1)/N
    for i in range(0, N):
        t.append(t0 + i*h)
        y.append(y[i] + v[-1]*h)
        v.append(v[i] + akceleracija(0, y[i], 5)*h)
    return(y, t)

print(Euler(0, 4, 0, 1000)[0])
print(Euler(0, 4, 0, 1000)[1])


plt.plot()





        

