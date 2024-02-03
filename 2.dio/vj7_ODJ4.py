import numpy as np
import matplotlib.pyplot as plt

g=9.81
l=0.2484902028828339
m=200
pi=3.141592653589793
T = (1/((1/(2*np.pi))*np.sqrt(g/l)))

def an(t0, y0, tn, N):
    h=(tn-t0)/N
    t=t0
    A=y0
    T = []
    X = []
    while t <= tn:
        x=A*np.cos(np.sqrt(g/l)*t)
        T.append(t)
        X.append(x)
        t = t+h
    return T, X

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
        t = t0+i*h
        V.append(v)
        Y.append(y)
        T.append(t)
    return Y, V

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
    return Y,V
#kao euler ali se mijenja jedan plus doprinos necega
# kad vec imas formu pa kako rj izgleda tj samo je rijesavas u zadanim tockama
#jug se siri i euler 


#na maloim intervalu dobro definiran ali kako akceleracija pa se povecava sve vse i vise
def JUG(t0, y0, tn, N): #jednoliko ubrzano gibanje  
    h=(tn-t0)/N
    y=[y0]
    t=t0
    vy0 = 0
    vy = [vy0]
    y=[y0]
    T=[t]

    i=1
    j=0
    for i in range(N+1):
        vy.append(vy[j] + akceleracija(y[j])*h)
        y.append(y[j] +vy[j]*h + (1/2)*akceleracija(y[j])*h**2)
        T.append(t0 + i*h)
        j+=1
    return vy, y #ovisnost kutne brzine o kutu

#s = (vt)/2
#v = at




P=Euler(0*T, 4*pi/180, 20*T, 20000)
Q=RK4(0*T, 4*pi/180, 20*T, 20000)
a=an(17*T, 4*pi/180, 20*T, 20000)
A=JUG(0*T, 4*pi/180, 20*T, 20000)

plt.plot(P[1], P[0], linewidth=0.3, color='green', label='Euler')
plt.plot(Q[1], Q[0], linewidth=0.3, color='red', label='Runge-Kutta')
#plt.plot(a[0], a[1], color='blue', label='analitički')
plt.plot(A[0], A[1], linewidth=0.3, color='purple', label='JUG')
plt.legend()
plt.show()
