#RK4 METODA (7.vj)

#Tijelo mase m miruje u ishodištu u t = 0 i na njega djeluje sila F.
#RK4 METODA

import numpy
import matplotlib.pyplot as plt

def analitička_metoda(y0, N=2000, l=0.2484902028828339, g=9.81):    #ovako rijesavamo svaku analitivcku funkciju (jedan od nacina, nije nuzno)
    
    w0 = numpy.sqrt(g/l)
    T = 2*numpy.pi/w0
    x = []
    y = []
    
    for i in range(1,N):
        x.append(i*0.01)
        y.append(y0*numpy.cos(w0*x[i-1]))
    return x,y

def analiticki_period(l=0.2484902028828339, g=9.81):
    
    T = 2*numpy.pi*numpy.sqrt(l/g)
    return T


def RK4(y0, v0, t0=0, tN=5, N=2000, l=0.2484902028828339, g=9.81, fi_0=0):
    
    def funkcija(f,y,v,t):
        return f(y,v,t)
    
    def f(y,v,t):
        return -y-5/2*v + 0.25
    
    w0 = numpy.sqrt(g/l)
    h = (tN-t0)/N
    v_rk = [v0]
    y_rk = [y0]
    t_rk = [t0]
    
    for k in range(1, N):
        
        t_rk.append(t_rk[k-1]+h)
        kv1 = f(y_rk[k-1], v_rk[k-1], t_rk[k-1])
        ky1 = v_rk[k-1]
        
        kv2 = (f(y_rk[k-1]+ky1*h/2, v_rk[k-1]+kv1*h/2, t_rk[k-1]+h/2))
        ky2 = (v_rk[k-1]+kv1*h/2)
        
        kv3 = (f(y_rk[k-1]+ky2*h/2,v_rk[k-1]+kv1*h/2, t_rk[k-1]+h/2))
        ky3 = (v_rk[k-1]+kv2*h/2)
        
        kv4 = (f(y_rk[k-1]+ky3*h,v_rk[k-1]+kv3*h, t_rk[k]))
        ky4 = (v_rk[k-1]+kv3*h)
        
        v_rk.append(v_rk[k-1]+h*(kv1+2*kv2+2*kv3+kv4)/6)
        y_rk.append(y_rk[k-1]+h*(ky1+2*ky2+2*ky3+ky4)/6)
    
    return t_rk, y_rk 


a,b = analitička_metoda(4)
T = analiticki_period()


a3, b3 = RK4(4, 1, 0, 5*T, 20)
a_3, b_3  = RK4(4, 1, 0, 5*T)

plt.subplot(1,2,1)
plt.plot(a, b, c="r")
plt.plot(a3, b3, c="b")
plt.legend(["Analitički","RK4"],loc="upper right")
plt.title("Usporedba za N = 20000")
# plt.subplot(1,2,2)

# plt.plot(a, b, c="r")
# plt.plot(a_3, b_3, c="b")
# plt.legend(["Analitički","RK4"],loc="upper right")
# plt.title("Usporedba za N = 2000")
plt.show()