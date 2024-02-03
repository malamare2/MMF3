#runge kuta je vj 8 git-hub
#oscilacija metalne kuglice
import numpy as np
import matplotlib.pyplot as plt 
import math

m = 200
l = 0.2484902028828339
g = 9.81
pi = 3.141592653589793
w =np.sqrt(g/l)
    
def akceleracija(y): 
    return -(g/l)*np.sin(y)  #ovo se na papiru racuna slikano

def analiticki(t, y):
    return y*np.cos(np.sqrt(g/l)*t)  

def Euler(t0, y0, n, N):
    t = [t0]
    theta = (y0/180)*pi
    y = [theta]
    lista = [theta]
    tn = n*(1/((1/(2*pi))*np.sqrt(g/l)))
    h = (tn - t0)/N
    s = 0
    j = 0
    for i in range(1, N+1):
        y.append(y[j]+s*h)
        t.append(t0+i*h)
        s = s+h*akceleracija(y[j])
        lista.append(theta*np.cos(np.sqrt(g/l)*t[j]))
        j = j+1
    return t,y,lista

def RK4(t0, y0, n, N):
    t = [t0]
    theta = (y0/180)*pi
    y = [theta]
    lista = [theta]
    v = [0]
    tn = n*(1/((1/(2*pi))*np.sqrt(g/l)))
    h = (tn - t0)/N
    j = 0
    for i in range(1, N+1):
        ky = v[j]    #pocetna funk koju uzimamo der
        kv = akceleracija(y[j])
        sy = ky
        sv = kv
        tp = t[j]+(h/2)
        yp = y[j]+ky*(h/2)
        vp = v[j]+kv*(h/2)

        ky = vp      #funk u polovicnom koraku
        kv = akceleracija(yp)
        sy = sy+2*ky
        sv = sv+2*kv
        yp = y[j] +ky*(h/2)
        vp = v[j]+kv*(h/2)

        ky = vp
        kv = akceleracija(yp)
        sy = sy +2*ky
        sv = sv+2*kv
        t.append(t0+(i+1)*h)
        yp =y[j]+ky*h
        vp = v[j]+kv*h

        ky = vp   
        kv = akceleracija(yp)
        sy = sy+ky
        sv = sv+kv

        y.append(y[j]+(h/6)*sy)
        v.append(v[j]+(h/6)*sv)

        lista.append(theta * np.cos(np.sqrt(g/l)*t[j]))
        j = j+1

    return t,y,lista

def crtanje(t0, y0, n, N):
    e, f, g = Euler(t0, y0, n, N)
    r, p, o = RK4(t0, y0, n, N)

    plt.plot(e, f, 'g', linestyle= 'dashed', linewidth = 2, label = 'Euler')
    plt.plot(e, g, 'r', linestyle= 'dashed', linewidth = 2, label = 'analiticki')

    plt.plot(r, p, 'b', ms = 0.2, label = 'RK4')
    plt.plot(r, o, 'black', ms = 0.2, label = 'analiticki')

    plt.title('E-RK4')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.grid()
    plt.legend(loc = 'lower right')
    plt.show()

crtanje(0, 64, 1, 20000)
crtanje(0, 64, 20, 20000)






# def Euler(t0, y0, v0, N):
#     T = 2*pi*np.sqrt(l/g) #period
#     t1 = t0
#     t2 = 20*T
    
#     y = [y0]
#     t = [t0]
#     v = [v0]
#     h = (t2 - t1)/N
#     for i in range(0, N):
#         t.append(t0 + i*h)
#         y.append(y[i] + v[-1]*h)
#         v.append(v[i] + akceleracija(0, y[i], 5)*h)
#     return(y, t)

# print(Euler(0, 4, 0, 1000)[0])
# print(Euler(0, 4, 0, 1000)[1])
        

