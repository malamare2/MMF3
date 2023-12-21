import math
import numpy as np
import matplotlib as plt

eps = 10**(-8)
D = 2
M = 10
# obicna = []
# prva = []
t = 10
# def C_0(x):
#     C = ((M/np.sqrt(4*math.pi*D*t)) * math.exp(-(x**2)/(4*D*t))-0.4)
#     return C

# # for i in x:
# #     obicna.append(9*(i**4) - 8*(i**2) - i- 6 + 10*math.cos(2*i))

# # for l in x:
# #     prva.append(-(36*(l**3) - 16*(l) - 1 -20*math.sin(2*l)))

# x = 0
# a = 8
# b = 10
# if (C_0(a)*C_0(b)<=0):
#     c=a
#     while ((b-a)>=eps):
#         c =(a+b)/2
        
#         #provjera jeli c nul-tocka
#         if (C_0(c) ==0.0):
#             break

#         #bira se strana
#         if (C_0(c)*C_0(a) <0):
#             b=c
#         else:
#             a=c
#         x = x+1

# print(C_0(c))


# def C_1(x):
#     C1 = (M*(4*math.pi*D*t)**(-1/2))*(-(2*x)/4*D*t)*math.exp(-(x**2)/4*D*t)
#     return C1

# x0 =1
# while abs(C_0(x0)/C_1(x0)) >= eps:
#     x0 = x0 - C_0(x0)/C_1(x0)
#     t = t+1
# print ("t={}; x = {}; y_0 = {}".format(t,"%4f"%x0,C_0(x0)))


# eps =1e-6
# t = 0

def y_0(x):
    y = ((M/np.sqrt(4*math.pi*D*t)) * math.exp(-(x**2)/(4*D*t))-0.4)
    return y
print(y_0(5))

a = 0
b = 0.1

while ((b-a)>=eps):
    c =(a+b)/2
        
        #provjera jeli c nul-tocka
    if (y_0(c) ==0.0):
        break

        #bira se strana
    if (y_0(c)*y_0(a) <0):
        b=c
    else:
        a=c
    t = t+1




print(y_0(c))

def y_1(x):
    y1 = (M*(4*math.pi*D*t)**(-1/2))*(-(2*x)/(4*D*t))*math.exp(-(x**2)/(4*D*t))
    return y1

x0 =1
while abs(y_0(x0)/y_1(x0)) <= eps:
    x0 = x0 - y_0(x0)/y_1(x0)
    t = t+1
print ("t={}; x = {}; y_0 = {}".format(t,"%4f"%x0,y_0(x0)))
print(len(x0))

