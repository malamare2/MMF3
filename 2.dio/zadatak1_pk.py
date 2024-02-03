from math import cos, pi, exp
import math

a = 0
b = 5

def PodInt_I(x):
    return 2 * pi * x ** 3 * ((2) / (1 + x ** 3))

def PodInt_M(x):
    return 2 * pi * x * ((2) / (1 + x ** 3))

def Trapezna(func, a, b, m):
    h = (b - a) / m
    rj = 0.5 * (func(a) + func(b))
    k = 1
    while k < m:
        rj += func(a + k * h)
        k += 1
    rj *= h
    return rj 

def Simpsonova(func, a, b, m):
    h = (b - a) / m  
    rj = func(a) + func(b)  
    k = 1
    while k < m:
        if (k % 2 == 0):
            rj += 2 * func(a + k * h)
        else:
            rj += 4 * func(a + k * h)
        k += 1
    rj *= h / 3
    return rj

def GauLeg(func, x1, x2, n, ispis=False):
    x = [0 for i in range(n)]  
    w = [0 for i in range(n)]
    epsilon = 1e-17   
    # jedna  nultocka  za  neparan n je 0, ostale su nultocke i  pripadne  tezine simetricne s obzirom na 0 pa je dovoljno da ih tražimo pola
    m = (n + 1) / 2
    # ove vrijednosti se koriste da se nultocke Legendreovog polinoma pozicioniraju na trazeni interval[x1,x2]
    xm = 0.5 * (x2 + x1) 
    xl = 0.5 * (x2 - x1)
    # petlja u koju spremamo nultocke u listu i pripadne tezine
    for i in range(1, int(m+1)): 
        # pocetna tocka za odredivannje nultocke s Newton-Raphsonovom metodom
        z = cos(pi * (i - 0.25) / (n + 0.5))
        # petlja koja racuna nultocke
        while True:
            # drugi Legendrovog polinom
            p1 = 1.0
            # prvi Legendrovog polinom
            p2 = 0.0
            # petlja koja racuna polinome, j ide od 1 do n jer zelimo dobiti polinom n-tog stupnja
            for j in range(1, n+1):
                p3 = p2
                p2 = p1
                # polinom j+1 stupnja
                p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j  
            # derivacija Legendrovog polinoma n-tog stupnja
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            # stara pocetna tocka za Newton-Raphsonovu metodu
            z1 = z
            # nova pocetna tocka, racunamo je kao i staru, vrijednost derivacije u staroj tocki
            z = z1 - p1 / pp
            # kad nam uvjet vise nije ispunjen znaci da je z
            if abs(z - z1) > epsilon:
                break

        # lista zadnjih z, ovdje spremamo nultocke u listu
        x[i-1] = xm - xl * z
        # s obzirom da su nultocke simetricne oko 0 spremamo vrijednost na odgovarajuce mjesto tako da brojimo od kraja liste
        x[n-i] = xm + xl * z
        # analogno
        w[i-1] = 2.0 * xl / ((1.0 - z * z) * pp * pp)
        w[n-i] = w[i-1]
    suma = 0
    for i in range(len(x)):
        suma += w[i] * func(x[i])
    if ispis:
        print("nultočke:")
        print(x)
        print("težine:")
        print(w)
        return
    return suma

print("\n\nMOMENT INERCIJE")
print('--------------------------------------------------------------')
for m in [10, 50, 100]:
    print(f"Trapezna formula za m = {m} daje: {Trapezna(PodInt_I, a, b, m)}")
    print(f"Simpsonova formula za m = {m} daje: {Simpsonova(PodInt_I, a, b, m)}")
    print(f"Gauss-Legendreova formula za m = {m} daje: {GauLeg(PodInt_I, a, b, m - 1)}")
    print('--------------------------------------------------------------')

print('\n\n\nMASA\n--------------------------------------------------------------')
for m in [10, 50, 100]:
    print(f"Trapezna formula za m = {m} daje: {Trapezna(PodInt_M, a, b, m)}")
    print(f"Simpsonova formula za m = {m} daje: {Simpsonova(PodInt_M, a, b, m)}")
    print(f"Gauss-Legendreova formula za m = {m} daje: {GauLeg(PodInt_M, a, b, m - 1)}")
    print('--------------------------------------------------------------')

print('\n\n\nTEŽINE\n--------------------------------------------------------------')
print("\nza masu:\n")
GauLeg(PodInt_M, a, b, 6, True)
print("\nza moment inercije:\n")
GauLeg(PodInt_I, a, b, 6, True)
print("\n")


