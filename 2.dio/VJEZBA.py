import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from tabulate import tabulate


g=9.81
l=0.2484902028828339
m=20
pi=3.141592653589793
T=(1/((1/(2*np.pi))*np.sqrt(g/l)))


#prvih 5 sek onda se množi 5*T

def an(t0, y0, tn, N):
    h=(tn-t0)/N    #delta t
    t=t0
    T = [t0]
    X = [y0]
    j=0
    for i in range(N+1):
        x=y0*np.cos(np.sqrt(g/l)*T[j])
        t = t0+i*h
        T.append(t)
        X.append(x)
        j+=1
    return T, X

def akceleracija(y,v): 
    return -4*y - (1/5)*v
#od 19 do 20 vidimo da odstupaju 

#jedan korak ima 4 koraka pa daje precizniji rezultat 

def RK4(t0, y0, tn, N):
    v0 = 0
    h=(tn-t0)/N
    t=t0
    y=y0
    v=v0
    T=[t0]
    Y=[y0]
    V=[v0]
    F= [akceleracija(y0,v0)]
    i=1
    for i in range(1, N):
        k1v=akceleracija(y, v)  #je nagib na početku intervala
        k1x=v

        k2v=akceleracija(y+k1x*h/2, v+k1x*h/2)
        k2x=v+k1x*h/2  #e nagib na sredini intervala

        k3v=akceleracija(y+k2x*h/2,v+k2x*h/2)
        k3x=v+k2v*h/2  #e nagib na sredini intervala

        k4v=akceleracija(y+k3x*h,v+k3x*h)
        k4x=v+k3v*h       #je nagib na kraju intervala

        v=v+(k1v+2*k2v+2*k3v+k4v)*h/6
        y=y+(k1x+2*k2x+2*k3x+k4x)*h/6
        t=t0+i*h
        
        V.append(v)
        Y.append(y)
        T.append(t)
        
        F.append(akceleracija(y,v)*m)
    return T,Y,V,F


#za prikazat ovisnost sile o vremenu
Ti,Y,V,F = RK4(0*T, 5, 20*T, 20000)
plt.plot(Ti,Y)
plt.plot(Ti,V)
plt.plot(Ti,F)

# print(len(Ti))
# print(len(Y))
# print(len(V))
# print(len(F))

# listanal = [an(0*T, 5, 20*T, 20)]
# listnum = [RK4(0*T, 5, 20*T, 20)]
# print (listanal)
# print (listnum)


# table1 = []
# row =[T, listanal, listnum]
# table1.append(row)
# vrh_tablice = ['vrijeme', "polozaj num", "polozaj anal"]
# tablica = tabulate(table1, vrh_tablice)
# print(tablica)


print('ovisnost polozaja num o vremenu:', 
      RK4(0*T, 5, 20*T, 10))
print ('ovisnost polozaja an o vremenu:',
       an(0*T, 5, 20*T, 10))
# plt.plot(RK4(0*T, 5, 20*T, 2))
# plt.plot(an(0*T, 5, 20*T, 2))



# Q=RK4(0*T, 5, 20*T, 200)
# a=an(0*T, 5, 20*T, 200)


# plt.plot(Q[0], Q[1], color='red', label='Runge-Kutta')
# plt.plot(a[0], a[1], color='blue', label='analitički')
# plt.legend()
plt.show()












# def akceleracija(y,v,t): 
#     return y-(5/2)*v+0.25
# #od 19 do 20 vidimo da odstupaju 

# #jedan korak ima 4 koraka pa daje precizniji rezultat 

# def RK4(t0, y0, tn, N):
#     v0 = 0
#     h=(tn-t0)/N
#     t=t0
#     y=y0
#     v=v0
#     T=[t0]
#     Y=[y0]
#     V=[v0]
#     t_rk = [t0]

#     v_rk = [v0]
#     y_rk = [y0]
#     i=1
#     for k in range(1, N):
        
#         t_rk.append(t_rk[k-1]+h)
#         kv1 = akceleracija(y_rk[k-1], v_rk[k-1], t_rk[k-1])
#         ky1 = v_rk[k-1]
        
#         kv2 = (akceleracija(y_rk[k-1]+ky1*h/2, v_rk[k-1]+kv1*h/2, t_rk[k-1]+h/2))
#         ky2 = (v_rk[k-1]+kv1*h/2)
        
#         kv3 = (akceleracija(y_rk[k-1]+ky2*h/2,v_rk[k-1]+kv1*h/2, t_rk[k-1]+h/2))
#         ky3 = (v_rk[k-1]+kv2*h/2)
        
#         kv4 = (akceleracija(y_rk[k-1]+ky3*h,v_rk[k-1]+kv3*h, t_rk[k]))
#         ky4 = (v_rk[k-1]+kv3*h)
        
#         v_rk.append(v_rk[k-1]+h*(kv1+2*kv2+2*kv3+kv4)/6)
#         y_rk.append(y_rk[k-1]+h*(ky1+2*ky2+2*ky3+ky4)/6)
    
        
#         V.append(v)
#         Y.append(y)
#         T.append(t)
#     return v_rk, y_rk



