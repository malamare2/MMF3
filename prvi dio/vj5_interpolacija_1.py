import math
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt


a = []   #appendam funkciju za razlicite polinome
b = []
c = []

#m je velicina od X sto znaci da gledan br clanova ali ako je npr x od 3 krece se od 0,1, 2, 3 dakle to je 4
X = [1, 2, 3, 4, 5]
Y = [-2*t - 4*t*t + t*t*t   for t in X]  #t je svaki clan u X listi

def f(X, Y, x, m):  # ovo je funkcija koju crtan samo ovisi o polinomu kojeg gledam i to uvrstavan posli u liste koje plotan kako bi vidila na grafu (Lagrangian)
    p = 0.0
    for i in range(m+1):
        L = 1.0  # jer u formuli ovo vrijedi
        for j in range(m+1): # jer python krece od 0 pa da bi dosao do polinoma kojeg ja treban 
            if (j != i):
                L = L*((x - X[j])/(X[i] - X[j]))
        p = p + Y[i]*L
    return(p)

for x in np.arange(0, 5, 0.001):# tocke na krivulji koje crtam sto blize da bi mi ispala pravilnija krivulja
    a.append(f(X, Y, x, 2)) #m je polinom u zadatku je zadano imamo 2 i 3 i sad prvo definiramo za 2
    b.append(f(X, Y, x, 3))
    c.append(x)  #samo apendam tocke koje san gore definirala

plt.scatter(X, Y)
plt.plot(c, a)
plt.plot(c, b)
plt.xlabel("t")
plt.ylabel("x")
plt.legend(['X_4', 'P_2(t)', "P_3(t)"])
plt.show()

print()
