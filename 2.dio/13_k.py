#Trapez i Simson

#Izracunati masu stapa koji ima granice duljine i zadanu linearnu gustoću

import matplotlib.pyplot as plt
from math import cos, pi, exp

L = 2.5

def function(x):
    
    return (exp(x) + x**5)

def trapezna(f, a, b, m):
    
    h=(b-a)/m  #br čvorova
    
    #izr vrijednosti funkcije u granicama pomnožene s faktorom 1/2
    
    it=0.5*(f(a) + f(b))
    k=0
    
    while k < m:
        
        it+=f(a+k*h)
        k+=1         
        #rj je zbroj vrijednosti funkcije u zadanim čvorovima pomnožen s korakom h
    it*=h
    
    return it 

def simpsonova(f, a, b, m):
    
    h=(b-a)/m  #br čvorova
    it=f(a)+f(b)  #izr vrijednosti funkcije u granicama a i b
    k=0
    #sumirati doprinose vrijednosti funkcije u čvorovima
    
    while k < m:
        
        if (k%2==0):
            it+=2*f(a+k*h)
        else:
            it+=4*f(a+k*h)
        k+=1
    it*=h/3
    
    return it

print('m = 10:',trapezna(function, -0.5, 2, 10)*L)
print('m = 10:',simpsonova(function, -0.5, 2, 10)*L)


   