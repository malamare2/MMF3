import math
import numpy as np
import matplotlib.pyplot as plt

m = 3.37*10**(-26)
T = 300
a = 50
kb = 1.38064852*10**(-23)

def v_srednja():
    vs = math.sqrt((8*kb*T)/(math.pi*m))
    return vs

def f(v):
    fm = ((m/(2*math.pi*kb*T))**(3/2))*4*math.pi*(v**2)*math.exp(-(m*(v**2))/(2*kb*T))
    return fm

a = v_srednja()-50 # jer je zadanona intervalu 50 m/s**2 
b = v_srednja()+50 #granice integrala


#TRAPEZNA FORMULA   POVRSINA TRAPEZA
def trapez(N):#zadana jednadzba dakle integral je suma gornje vrijednosti + sredina l + donje vrijednosti pomnozene s (1/2)*h
    h = (b-a)/N
    l=((1/2)*(f(b)+f(a)))*h
    for k in np.arange(1, N): #zasto je od a do b kad je definirano drugacije u formuli
        l += h*f(a+k*h) #na ovaj nacin sumira sve odma
    #zbroj = (1/2)*h*((f(a))+l+(f(b))) 
    return(l)

print(trapez(10), trapez(50), trapez(100))


#SIMPSONOVA FORMULA
def simpson(N):#zadana jednadzba dakle integral je suma gornje vrijednosti + sredina l + donje vrijednosti pomnozene s (1/2)*h
    h = (b-a)/N
    l=((f(b)+f(a)))
    for k in np.arange(1, N): #zasto je od a do b kad je definirano drugacije u formuli
        if k%2 == 0:
            l += 2*f(a+k*h) #na ovaj nacin sumira sve odma
        elif k%2 != 0:
            l += 4*f(a+k*h)
    #zbroj = (1/2)*h*((f(a))+l+(f(b))) 
    return(l*(h/3))
print(simpson(10), simpson(50), simpson(100))

    
#FUNKCIJA GAUGLEG
def  gauleg(x1, x2, n):#n isto sta i N u drugim zad
    #n - stupanj polinoma
    eps = 0.000001
    x = []
    w = []
    for i in range(0, n+1):
        x.append(i)
        w.append(i)
    m = int((n+1)/2) #brojac jer trazimo samo pola jer su simetricne pa nije potrebno gledat obe strane
    xm = (x2 + x1)/2 # sredina intervala
    xl = (x2 - x1)/2 #pola duljine intervala
    #pomoću xm i xl tecke se legendrovog polinoma pozicioniraju na traženi interval[x1, x2]

    for i in np.arange(1, m+1): # petlja za odredivanje nultocaka
        z = math.cos(math.pi * ((i-0.25)/(n+0.5)))#za odabiranje pocetne vrijednosti
        while True:
            p1 = 1.0
            p2 = 0.0
            for j in np.arange(1, n+1):
                p3 = p2
                p2 = p1
                p1 = ((2*j - 1)*z*p2-(j-1)*p3)/j
            pp = n * (z*p1-p2)/(z*z-1)
            z1 = z
            z = z1  - p1/pp       
            if (abs(z-z1) < eps):
                break
        x[i] = xm - xl * z
        x[n + 1 - i] = xm + xl * z
        w[i] = (2*xl)/((1-z*z)*pp*pp)
        w[n + 1 - i] = w[i]

        I = 0
        for i in range(1, len(x)):
            I = I + f(x[i])*w[i]

    return I

print(gauleg(a, b, 10), gauleg(a, b, 50), gauleg(a, b, 100))




