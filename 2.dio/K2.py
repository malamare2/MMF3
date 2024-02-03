import numpy as np
import matplotlib.pyplot as plt

m = 0.1
v0 = 15
k = 10**(-3)
g = 9.81

def akceleracija(v): 
    return -(k/m)*v*abs(v) - g

def RK4(t0, y0, tn, N):
    h=(tn-t0)/N
    t=t0
    y=y0
    v=v0
    T=[t0]
    Y=[y0]
    V=[v0]
    i=1
    for i in range(1, N+1):
        k1v=akceleracija(v)  #je nagib na početku intervala
        k1x=v

        k2v=akceleracija(v+k1x*h/2)
        k2x=v+k1x*h/2  #e nagib na sredini intervala

        k3v=akceleracija(v+k2x*h/2)
        k3x=v+k2v*h/2  #e nagib na sredini intervala

        k4v=akceleracija(y+k3x*h)
        k4x=v+k3v*h       #je nagib na kraju intervala

        v=v+(k1v+2*k2v+2*k3v+k4v)*h/6
        y=y+(k1x+2*k2x+2*k3x+k4x)*h/6
        t=t0+i*h
        
        V.append(v)
        Y.append(y)
        T.append(t)
    return T,Y,V

T,Y,V = RK4(1, 1, 10, 200000)
plt.plot(T,Y)
plt.plot(T,V)

Q=RK4(1, 1, 4, 200000)

#plt.plot(P[0], P[1], color='green', label='Euler')
# plt.plot(Q[0], Q[1], color='red', label='Runge-Kutta')
# plt.plot(a[0], a[1], color='blue', label='analitički')
plt.legend()
plt.show()

