import math
import numpy as np
import matplotlib as plt

a = [0, 1, 2, 3, 4, 5, 6]
b = [2, 4, 6, 8, 6, 4, 2]
c = [6, 5, 4, 3, 2, 1, 0]
d = [0, 1, 2, 3, 2, 1, 0]

ccc = [c[0]/b[0]] #prvi clan (nulti)
dcc = [d[0]/b[0]]

for i in range(1, 6): 
    ccc.append(c[i]/(b[i]-a[i]*ccc[i-1]))
    dcc.append((d[i]-a[i]*dcc[i-1])/(b[i]-a[i]*ccc[i-1]))

dcc.append((d[6] - a[6]*dcc[5])/(b[6] - a[6]*ccc[5]))# sad tražim sedmi član liste
x = dcc[6]
xlista = []
xlista.append(x)
for i in range(1, 7):
    k = 6-i  #to je brojač da bi išla unazad jer ako obrnem u for ptlji to neće funkcionirati
    xlista.append(dcc[k] - ccc[k]*xlista[i-1]) #zasto je i-1???

#provjera rezultata
xprovjera = []
for i in range(0, 7):
    k = 6-i
    xprovjera.append(round(xlista[k]*14))
    
print (xprovjera)