import math


def H(x,n): #dakle definira funkcija za podatke koje cu unosit
    H0=1  # definiraju se polinomi prvog drugog, treceg, koliko god
    H1=2*x
    for i in range(2, n+1, 1):  #od dva jer san ode definirala prva dva polinoma
        H2 = 2*x*H1 - 2*(i-1)*H0 #zapise se rekurzivna 
        H0 = H1
        H1= H2
    return(H2)


print(H(10,10))

def der(x, n):
    H(x,n)  #samo se definira da se prijasnja funkcija veze na ovu
    h1 = 10**(-1) #zadani korak u zadatku
    print((H(x + h1, n) - H(x,n))/(h1)) #definirana derivacija
    print((H((x+h1),n) - H((x-h1), n))/2*h1)

    h1 = 10**(-3) #zadani korak u zadatku
    print((H(x + h1, n) - H(x,n))/(h1)) #definirana derivacija
    print((H((x+h1),n) - H((x-h1), n))/2*h1)

der(10,10)