import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from polint import polint


X = []
Y = []

E = 4*math.pi
B = 4*math.pi

m = 6
Q = 3
w = (Q*B)/m

def x(t):
    return E*(w*t - math.sin(w*t))/(w*B)

def y(t):
    return E*(1-math.cos(w*t))/(w*B)

for t in np.arange(0, 1.005, 0.125):
    X.append(x(t))
    Y.append(y(t))

yN = []
dY = []
c=[]
#print(X)
for i in np.arange(0, 1.005, 0.001):# tocke na krivulji koje crtam sto blize da bi mi ispala pravilnija krivulja
    c.append(i)



#D)NEVILLEV ALGORITAM   
    yn, dy = polint(X, Y, len(X)-1, i)
    yN.append(yn) #vrijednost funkcije
    dY.append(dy) # pogreska za svaku tocku
#poprima previse nultocki te je zato nije dobar za velike range-ove i zato gledamo cubicsplkine
#ako je reda 39 dakle polinom 38 stupnjA I ZATO PROLAZI KROZ PUNO NULTOCAKA


#CUBIC SPLINE
firstder_0 = (E*w)/(w*t) - (w*math.cos(w*t))/(w*B)
firstder_1 = (w*math.sin(w*t))/(w*B) 

#bc oznacava potpuni spline koji treba derivirati
cs = CubicSpline(X, Y, bc_type="natural")  #matrica
xs = np.arange(0, 1, 0.001)

x1_interpolate = 51
y1_interpolate = cs(x1_interpolate)
print(f'položaj čestice: x={x1_interpolate} je y={y1_interpolate}')


# a = []
# def Lagrange(X, Y, x, m):  # ovo je funkcija koju crtan samo ovisi o polinomu kojeg gledam i to uvrstavan posli u liste koje plotan kako bi vidila na grafu (Lagrangian)
#     p = 0.0
#     for i in range(m+1):
#         L = 1.0  # jer u formuli ovo vrijedi
#         for j in range(m+1): # jer python krece od 0 pa da bi dosao do polinoma kojeg ja treban 
#             if (j != i):
#                 L = L*((x - X[j])/(X[i] - X[j]))
#         p = p + Y[i]*L
 
#     return(p)
# for x in np.arange(0,1, 0.001):# tocke na krivulji koje crtam sto blize da bi mi ispala pravilnija krivulja
#     a.append(Lagrange(X, Y, x, 0)) #lagrange
#     c.append(x)



plt.scatter(X, Y, s=50, facecolors='none', edgecolors='k')
plt.scatter(c, cs(xs), s=10, facecolors='none', edgecolors='yellow')
plt.errorbar(c, yN, yerr=dY, fmt = "." )
plt.legend(['(X, Y)', "CubicSpline", "Neville"])


plt.show()
