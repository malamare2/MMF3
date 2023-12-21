import math
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


def der(x, h):
    d = (math.exp(x+h)-2*math.exp(x)+math.exp(x-h))/h**2 #druga der
    return d
    #formula za derivaciju (numericki)

def funk(x):
    return math.exp(x) 
    #direktan izracun derivacije

x1 = [1.0, 5.0, 10.0]
h1 = [10**-1, 10**-2, 10**-3, 10**-4, 10**-5, 10**-6]

table1 = []

for x in x1:
    errors = []
    h_log = []

    for h in h1:
        d = der(x, h) #aproksimacija
        der_tocno = funk(x) #derivacija
        error = (abs(der_tocno - d)) #negativni logaritam za pogrešku (apsolutna vrijednost razlike)
        errors.append(error)
        h_log.append((h)) #svaki negativan logaritam od koraka h u listi 


        row =[f"x = {x}, h = {h}", d, der_tocno, error]   #sto ce svaki red sadrzavat po stupcima
        table1.append(row) # tablica koja ce sadrzavat sve redove


    plt.plot(h_log, errors)

vrh_tablice = ["Parametri", "aproksimacija", "tocna vrijednost", "pogreska"]
tablica = tabulate(table1, vrh_tablice)
print(tablica)

#plt.xlim(1e-7, 1e-0)
#plt.ylim(1e-11, 1e+5)
plt.xscale("log") #log-log skala
plt.yscale("log")
plt.xlabel("h")
plt.ylabel("error")



plt.show()
# sto je h manji to je tocniji rezultat





