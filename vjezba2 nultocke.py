import math
import numpy as np
import matplotlib.pyplot as plt

eps =1**(-5) #rubni uvjet, totalna vrijednost
x = np.arange(-5, 91, 0.01)

obicna = []
prva = []
druga = []

#za min i max nacrtat
for i in x:
    obicna.append(9*(i**4) - 8*(i**2) - i- 6 + 10*math.cos(2*i))

for l in x:
    prva.append(-(36*(l**3) - 16*(l) - 1 -20*math.sin(2*l)))

for k in x:
    druga.append(-(108*(k**2) - 16 - 40*math.cos(2*i)))
#ovo je samo za pronac intervale koje posli uvrstavan u metodu bisekcije



#ode se dalje samo koristim tom metodom vise mi ne treba ono gore
def U(x):   #stabilna i nestabilna ravnoteza svakako trazin der od ovog
    return(9*(x**4) - 8*(x**2) - x- 6 + 10*math.cos(2*x))  #zadana pot funkcija

def der_U(x):
    return(-(36*(x**3) - 16*(x) - 1 -20*math.sin(2*x))) 
#crtanjem ove derivacije funkcije dobivam di se nalaze nul tocke


def der2_U(x):
    return(-(108*(x**2) - 16 - 40*math.cos(2*x)))

# Bisection method to find roots of a function
def bisection_method(a, b):  #u funk kad posli pozivam samo dodajem vec prethodno odredene funkcije
    n = 0
    c=(a + b) / 2
    while U(a - b) / 2 > eps:
        n = n+1
        
        if U(a) * U(c) < 0:
            b = c
        elif U(b) * U(c) > 0:
            a = c
        elif (n==100):
            break
    return c

interval = bisection_method(-0.6, 0.6) #minimum i maksimum
#sama odredujem interval a ako imam vise nul tocki onda za svaku nul-tocku moran odredit min i maks

if der2_U(interval) <0:
    print("min")
elif der2_U(interval) >0:
    print("max")
else:
    print("nije dobro")

plt.xlim(-2,2)
plt.ylim(-30,50)
plt.plot(x, obicna)
plt.plot(x, prva)
plt.grid(color = "green")
#plt.plot(x, druga)
plt.show()
