import math
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

X = [0, 50, 100, 150, 200, 250, 300]
Y = [0.00, 0.20, 0.75, 1.20, 1.40, 1.48, 1.50]

a = []   #appendam funkciju za razlicite polinome
b = []
c = []
d = []

def Lagrange(X, Y, x, m):  # ovo je funkcija koju crtan samo ovisi o polinomu kojeg gledam i to uvrstavan posli u liste koje plotan kako bi vidila na grafu (Lagrangian)
    p = 0.0
    for i in range(m+1):
        L = 1.0  # jer u formuli ovo vrijedi
        for j in range(m+1): # jer python krece od 0 pa da bi dosao do polinoma kojeg ja treban 
            if (j != i):
                L = L*((x - X[j])/(X[i] - X[j]))
        p = p + Y[i]*L
 
    return(p)
#od 0 do 7 jer u tim tockama poznajemo vrijednost funkcije
for x in np.arange(0, 300, 0.1):# tocke na krivulji koje crtam sto blize da bi mi ispala pravilnija krivulja
    a.append(Lagrange(X, Y, x, 6)) #lagrange
    c.append(x)




#OVO ISPOD IDE ZAJEDNO SVE STA UJE U KOMENT

# firstder_0 = (Y[1]-Y[0])/(X[1]-X[0])
# firstder_1 = (Y[0]-Y[1])/(X[0]-X[1])

# #bc oznacava potpuni spline koji treba derivirati
# cs = CubicSpline(X, Y, bc_type=((1, firstder_0), (1, firstder_1)))  #matrica
# xs = np.arange(0, 300, 0.1)

#clamped moze jos biti
cs = CubicSpline(X, Y, bc_type="natural")  #matrica
xs = np.arange(0, 300, 0.1)


plt.xlim([-50,350])
plt.ylim([-0.20,1.6])
plt.scatter(X, Y, s=50, facecolors='none', edgecolors='k')
plt.scatter(c, a, s=2 ,marker='o', color="red")
plt.scatter(c, cs(xs), s=2, facecolors='none', edgecolors='yellow')

plt.show()
