import math
import numpy as np
import matplotlib.pyplot as plt

eps = 10**(-8)
D = 2
M = 10
t=10

x = np.arange(-100, 1000, 0.01)

obicna = []
prva = []
druga = []

def C_0(x, t):
    C = (M/np.sqrt(4*math.pi*D*t)) * math.exp(-(x**2)/(4*D*t))
    return C





def metoda_bisection(a, b):

    while C_0(a-b) > eps:
        c = (a + b)/2
        if C_0(a)*C_0(c) < 0:
            b = c
        elif C_0(a)*C_0(c) > 0:
            a = c
        else:
            break

    return c
#print(metoda_bisection(0.0, 10))

#treba opcenitije zapisat


plt.plot(x, obicna)
plt.plot(x, prva)
plt.grid(color = "green")
#plt.plot(x, druga)
plt.show()