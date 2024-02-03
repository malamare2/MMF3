#INTEGRACIJA (6.vj)

#isti zadatak kao 6.4, ali nas trazi samo Gauss-L. rezultat

from math import cos, pi, exp
import math

m = 3.37e-26
T = 300
a = 549.4 - 50
b = 549.4 + 50
k = 1.38064852e-23
A = m/(2*k*T)
pi=3.141592654

def function(v):
    
    return ((A/pi)**(3/2)) * (4*pi*v**2) * (exp(-A*(v**2)))

def Gauss(f, x1, x2, n):
    
    x = [0 for i in range(n+1)]  
    w = [0 for i in range(n+1)]
    epsilon=1e-14
    m=(n+1)/2   	
    xm=0.5*(x2+x1)
    xl=0.5*(x2-x1)

    for i in range(1, int(m+1)): 
        
        z=cos(pi*(i-0.25)/(n+0.5))
        
        while True:
            p1=1.0
            p2=0.0
            
            for j in range(1,n+1):
                
                p3=p2
                p2=p1
                p1=((2.0*j-1.0)*z*p2-(j-1.0)*p3)/j  
            
            pp=n*(z*p1-p2)/(z*z-1.0)
            z1=z
            z=z1-p1/pp
            
            if abs(z-z1) > epsilon:
                break
        
        x[i-1]=xm-xl*z
        x[n-i]=xm+xl*z
        w[i-1]=2.0*xl/((1.0-z*z)*pp*pp)
        w[n-i]=w[i-1]
    
    suma = 0

    for i in range(len(x)):
       
        suma += w[i]*f(x[i])
    
    return suma

for m in [10, 50, 100]:
    
    print(f"Gauss-Legendreova formula za m={m} daje: {Gauss(function,a,b,m-1)*100} %")
   