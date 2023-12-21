import math
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from polint import polint


#u terminalu stavim cd .. ako zelin promijenit put ucitavanja
a = 0.52917721092
K = 315775.04

X = []
Y = []

#A)PRETVARANJE DATOTEKE

f = open("V(H-H)_AK.txt", "w")
with open("V(H-H).txt") as file:
    for line in file:
        if line.startswith("#"): #naredba da samo nastavi bez te linije di se nalazi
            continue
        else:
            sline = line.split(' ')  # separates line into a list of items.  ' ' tells it to split the lines at the commas
            prvi_stupac = round(float(sline[0])*a, 6)  #each line is now a list, a 6 je nakon kolikjo decimala da zaokruzi
            drugi_stupac = round(float(sline[3])*K, 9)

            X.append(prvi_stupac)
            Y.append(drugi_stupac)

            c = [str(prvi_stupac), str(drugi_stupac)] 
            f.write("{0}\t{1}\n".format(*c))  #stavlja stupce u novi text file
f.close()


#LAGRANGEOV OBLIK
#ovaj dio je iz proslog interpol.1
a = []   #appendam funkciju za razlicite polinome
b = []
c = []
d = []
#m je velicina od X sto znaci da gledan br clanova ali ako je npr x od 3 krece se od 0,1, 2, 3 dakle to je 

def Lagrange(X, Y, x, m):  # ovo je funkcija koju crtan samo ovisi o polinomu kojeg gledam i to uvrstavan posli u liste koje plotan kako bi vidila na grafu (Lagrangian)
    p = 0.0
    for i in range(m+1):
        L = 1.0  # jer u formuli ovo vrijedi
        for j in range(m+1): # jer python krece od 0 pa da bi dosao do polinoma kojeg ja treban 
            if (j != i):
                L = L*((x - X[j])/(X[i] - X[j]))
        p = p + Y[i]*L
 
    return(p)



yN = []
dY = []

for x in np.arange(2.81, 9.82, 0.1):# tocke na krivulji koje crtam sto blize da bi mi ispala pravilnija krivulja
    a.append(Lagrange(X, Y, x, 38)) #lagrange
    c.append(x)

#D)NEVILLEV ALGORITAM   
    yn, dy = polint(X, Y, len(X)-1, x)
    yN.append(yn) #vrijednost funkcije
    dY.append(dy) # pogreska za svaku tocku
#poprima previse nultocki te je zato nije dobar za velike range-ove i zato gledamo cubicsplkine
#ako je reda 39 dakle polinom 38 stupnjA I ZATO PROLAZI KROZ PUNO NULTOCAKA


#3.dio (CubicSpline)
def firstder(x):
    return(-6)*(-45064)*x**(-7)

firstder_0 = (Y[1]-Y[0])/(X[1]-X[0])

#bc oznacava potpuni spline koji treba derivirati
cs = CubicSpline(X, Y, bc_type=((1, firstder_0), (1, firstder(X[-1]))))  #matrica
xs = np.arange(2.81, 9.82, 0.1)




plt.xlim([1,10])
plt.ylim([-10,10])
plt.scatter(X, Y, s=50, facecolors='none', edgecolors='k')
plt.scatter(c, a, s=20 ,marker='o', color="red")
plt.scatter(c, cs(xs), s=10, facecolors='none', edgecolors='yellow')
plt.errorbar(c, yN, yerr=dY, fmt = "." )
plt.xlabel("r/A")
plt.ylabel("V/K")
plt.legend(['(ri, Vi)', 'Lagrange', "CubicSpline", "Neville"])

plt.show()



f = open("V(H-H)_inter.txt", "a")
f.truncate(0)
cols = ("r", "Lagrange", "Neville", "greska", "Spline", "Neville-Spline")
f.write("\t".join(cols) + "\n")

ys = []
for j in cs(xs):
    ys.append(j)

for i in range(0,71):
    cols1 = (str("{:.6f}".format(c[i],6)), str("{:.6f}".format(a[i],6)), str("{:.6f}".format(yN[i],6)), str("{:.6f}".format(dY[i],6)), str("{:.6f}".format(ys[i],6)), str("{:.6f}".format(yN[i]-ys[i],6)))
    f.write("\t".join(cols1)+"\n")