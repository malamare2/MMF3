import numpy as np
import matplotlib.pyplot as plt

g=9.81
l=0.2484902028828339
m=200
pi=3.141592653589793
T=2*np.pi/np.sqrt(g/l)


def analiticki(t):
    return pi*np.cos(np.sqrt(g/l)*t)

def akceleracija(y): 
    return -(g/l)*np.sin(y)

def Euler(t0, y0, tn, N):
    v0 = 0
    h=(tn-t0)/N
    y=y0
    t=t0
    v=v0
    Y=[y]
    T=[t]
    V=[v]
    i=1
    for i in range(1, N+1):
        v = v + akceleracija(y)*h
        y = y + v*h
        t=t0+i*h
        V.append(v)
        Y.append(y)
        T.append(t)
        i+=1
    return T, Y, V

def RK4(t0, y0, tn, N):
    v0 = 0
    h=(tn-t0)/N
    t=t0
    y=y0
    v=v0
    T=[t0]
    Y=[y0]
    V=[v0]
    i=1
    for i in range(1, N+1):
        k1v=akceleracija(y)
        k1x=v

        k2v=akceleracija(y+k1x*h/2)
        k2x=v+k1x*h/2

        k3v=akceleracija(y+k2x*h/2)
        k3x=v+k2v*h/2

        k4v=akceleracija(y+k3x*h)
        k4x=v+k3v*h

        v=v+(k1v+2*k2v+2*k3v+k4v)*h/6
        y=y+(k1x+2*k2x+2*k3x+k4x)*h/6
        t=t0+i*h
        
        V.append(v)
        Y.append(y)
        T.append(t)
        i+=1
    return T,Y,V

def an(t0, y0, tn, N):
    h=(tn-t0)/N
    t=t0
    T=[]
    X=[]
    A=y0
    while t <= tn:
        x=A*np.cos(np.sqrt(g/l)*t)
        T.append(t)
        X.append(x)
        t+=h

    return T, X

def JUG(t0, y0, tn, N):
    v0 = 0
    h=(tn-t0)/N
    y=y0
    t=t0
    v=v0
    Y=[y]
    T=[t]
    V=[v]
    i=1
    while i <= N:
        v+=akceleracija(y)*h
        y+=v*h
        t=t0+i*h
        V.append(v)
        Y.append(y)
        T.append(t)
        i+=1
    return T, Y, V


Q=RK4(0*T, 4*pi/180, 7*T, 20000)
P=RK4(0*T, 8*pi/180, 7*T, 20000)
L=RK4(0*T, 16*pi/180, 7*T, 20000)
C=RK4(0*T, 32*pi/180, 7*T, 20000)
D=RK4(0*T, 64*pi/180, 7*T, 20000)

plt.plot(Q[0], Q[1], color='purple', label='Runge-Kutta')
plt.plot(P[0], P[1], color='yellow', label='Runge-Kutta')
plt.plot(L[0], L[1], color='red', label='Runge-Kutta')
plt.plot(C[0], C[1], color='blue', label='Runge-Kutta')
plt.plot(D[0], D[1], color='green', label='Runge-Kutta')

plt.legend()
plt.show()