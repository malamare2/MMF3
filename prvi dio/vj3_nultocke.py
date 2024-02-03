import math
import numpy as np
import matplotlib as plt


#iman interval(sama zadajen) koji cijepan na pola i onda kad odredim jeli veci ili manji od nula tada taj opet dio cijepan pa opet pa opet sve manje i manje
#ta funkcija je zapravo razlika dvije zadane funkcije
eps =1e-6

A = 1
B = 3
C = 2
D = 0.5
y01 = 5.0
y02 = 0.325
t = 0

def y_0(t):

    y = y01 + A *math.cos(B*t) - (y02 + C * math.exp(D*t))
    return y

def metoda_bisection(a, b):

    while y_0(a-b) > eps:
        c = (a + b)/2
        if y_0(a)*y_0(c) < 0:
            b = c
        elif y_0(a)*y_0(c) > 0:
            a = c
        else:
            break

    return c
print(metoda_bisection(0.0, 10))

#treba opcenitije zapisat




def y_1(t):   #derivacija gornje jdž
    d = -A*B*math.sin(B*t) - (C*D*math.exp(D*t))
    return d

def metoda_RN():
    x0 = 1.3
    while abs(y_0(x0)/y_1(x0)) > eps:
        x0 = x0 - y_0(x0)/y_1(x0)
    return x0

print(metoda_RN())

#problem je kad upadne na minimum tad se gleda tangenta i sobziron da je minimum di presjeca vraća stari presjek a metoda za naći tocnu tocku mogu plotat tj nacrtati graf te preko njega vidjeti di sam i sta sam































# x = [i for i in np.arange(0.0, 5.0, 0.01)]
# y = [y_0(i, y01, A, B, y02, C, D) for i in x]

# plt.plot(x, y)
# plt.grid(True)
# plt.show()



        
