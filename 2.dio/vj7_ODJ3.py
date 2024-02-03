import numpy as np
import matplotlib.pyplot as plt

g=9.81
l=0.2484902028828339
m=200
pi=3.141592653589793
T=(1/((1/(2*np.pi))*np.sqrt(g/l)))
#T = 1/((1/(2*np.pi)) * w

#prvih 5 sek onda se množi 5*T
# delta = b/2m
#wo = k/m
#w = wo**2-delta**2) korjen
#priguseno

def an(t0, y0, tn, N):
    h=(tn-t0)/N
    t=t0
    T = [t0]
    X = [y0]
    j=0
    for i in range(N+1):
        x=y0*np.cos(np.sqrt(g/l)*T[j])   # ode se pise
        t = t0+i*h
        T.append(t)
        X.append(x)
        j+=1
    return T, X

def akceleracija(y): 
    return -(g/l)*np.sin(y)
#od 19 do 20 vidimo da odstupaju 
#euler - prema dijelu 
#imamo der funkcije 
#trazimo funk u tocki 
#preko tang se gleda se najmanji br koraka

#uzeli taylorov razvoj i tocku uzeli te prvi clan ove der eulerova metoda odgovara taylorovom razvoju do prvog stupnja

#racun za nagib tangente na krivulji u bilo kojoj tocki   bitno je da je velicina koraka dovoljno mala
def Euler(t0, y0, tn, N):   #najjednostavnija RK metoda za rjesasvanje odj
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
        y = y + v*h
        v = v + akceleracija(y)*h
        t = t0+i*h
        V.append(v)
        Y.append(y)
        T.append(t)
    return T, Y, V

#jedan korak ima 4 koraka pa daje precizniji rezultat 

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
        k1v=akceleracija(y)  #je nagib na početku intervala
        k1x=v

        k2v=akceleracija(y+k1x*h/2)
        k2x=v+k1x*h/2  #e nagib na sredini intervala

        k3v=akceleracija(y+k2x*h/2)
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
print(RK4(19*T, 32*pi/180, 5*T, 2))


P=Euler(19*T, 32*pi/180, 5*T, 20000)
Q=RK4(19*T, 32*pi/180, 5*T, 20000)
a=an(19*T, 32*pi/180, 5*T, 20000)

#plt.plot(P[0], P[1], color='green', label='Euler')
plt.plot(Q[0], Q[1], color='red', label='Runge-Kutta')
plt.plot(a[0], a[1], color='blue', label='analitički')
plt.legend()
plt.show()


















#odj se racuna kao y'' = |F|/m      y'' =f(y, y', t)      F = ma

