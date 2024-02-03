import math
import numpy as np
import matplotlib.pyplot as plt

x1 = -0.3
x2 = 5
L = x2-x1
b = 1
a = 2

def f(x):
    return (a*math.exp(x) + b*x**3)

    
#FUNKCIJA GAULEG
def  gauleg(n):#n isto sta i N u drugim zad
    #n - stupanj polinoma
    eps = 0.00001
    x = []
    w = []
    for i in range(0, n+1):
        x.append(i)
        w.append(i)
    m = int((n+1)/2) #brojac jer trazimo samo pola jer su simetricne pa nije potrebno gledat obe strane
    #br tocaka koje koristimo pri integraciji
    xm = (x2 + x1)/2 # sredina intervala
    xl = (x2 - x1)/2 #pola duljine intervala
    #pomoću xm i xl tecke se legendrovog polinoma pozicioniraju na traženi interval[x1, x2]

    for i in np.arange(1, m+1): # petlja za odredivanje nultocaka
        z = math.cos(math.pi * ((i-0.25)/(n+0.5)))#za odabiranje pocetne vrijednosti
        #petlja koja racuna nul-tocke
        while True:
            #drugi polinom
            p1 = 1.0
            #prvi polinom
            p2 = 0.0
            #petlja koja racuna polinome n-tog stupnja
            for j in np.arange(1, n+1):
                p3 = p2
                p2 = p1
                #polinom j+1 stupnja
                p1 = ((2*j - 1)*z*p2-(j-1)*p3)/j
            #derivacija polinoma n-tog stupnja
            pp = n * (z*p1-p2)/(z*z-1)
            #stara pocetna tocka za newton-rapsonovu metodu
            z1 = z
            #nova pocetna tocka koja se racuna kao stara, vrijednost der u staroj tocki
            z = z1  - p1/pp       
            if (abs(z-z1) < eps):
                break
        # lista zadnjih z, ovdje spremamo nultocke u listu
        x[i] = xm - xl * z
        # s obzirom da su nultocke simetricne oko 0 spremamo vrijednost na odgovarajuce mjesto tako da brojimo od kraja liste
        x[n + 1 - i] = xm + xl * z
        #analogno
        w[i] = (2*xl)/((1-z*z)*pp*pp)
        w[n + 1 - i] = w[i]

        I = 0
        for i in range(1, len(x)):
            I = I + f(x[i])*w[i]

    return I

print(gauleg(10))
print(gauleg(50))
print(gauleg(100))