import math
import numpy as np
from tabulate import tabulate

#k=0
#s0=1   #član
#sa=1
eps = 10**(-10)
lista = []
listax = []
listak = []
#x = 0
#sa = s0
#ili rucno listu od 0 do 100

for x in range(0, 110):
    k=0
    s0=1
    sa = s0

    while abs(s0)>=eps:
        #apsolutni jer kad se uvrsti u doli formulu od s0 u jednom trenutku bi dobili negativni br sto ne smije biti
        
        k = k+1
        s0 = (-1)**k *((x**k)/math.factorial(k))
        sa = sa +s0



        if x == 20:
            #poc
            for i in range(0, k+1):
                i = i
            listak.append(i)
            lista.append(sa)
            a = len(lista)

                #listax.append(x)

#print(lista)    
#id do 110 jer je korak od 10 pa se gleda 10,20,30 a mora ukljucivati 100 pa nemoze biti 101

#k i s0 su definirani unutar for petlje jer se uvjek mora gledati ta pocetna vrijednost koju smo zadali
    

        #treba vidit ako je paran onda ide + ovaj clan ako je neparan ide minus

        
#stvorit praznu listu i appendat sa u nju te printat listu
#print(lista)

# poc_element = 0
# for i in range(0, 11):
   
#    print(lista[poc_element+i])






# poc_element = 0
# for i in range(0, 100):
   
#    #tablica = tabulate(listak[poc_element+i],lista[poc_element+i])
#    print(lista[poc_element+i])











#poc_element = 0
#for i in range(0, 11):
 #  a = listcx[poc_element+i]
  # b = lista[poc_element+i]
#    print(listcx[poc_element+i], lista[poc_element+i], listb[poc_element+i], listc[poc_element+i], listak[poc_element+i])

#vidit sta jos fali




#print(tabulate(table))





#REKURZIVNA
eps = 10**(-10)
listb= [] #polinomi
listbx = []
listbk = [] #stupanj polinoma

for x in range(0, 110, 10):

    listbx.append(x)

    k=0 #STUPANJ OD KOJEG SE KRECE
    s0=1 #(polinomi) #ovo je jedan polinom mogu ih imat vise pa bi bilo s1, s2, s3... a traženi bi bia npr s4 =s0
    sb = s0
    while abs(s0)>=eps:
        #apsolutni jer kad se uvrsti u doli formulu od s0 u jednom trenutku bi dobili negativni br sto ne smije biti
        
        k = k+1 #stupanj polinoma
        s0 = -s0*(x/k)   #ode ide rekurzivna relacija s0 =...(zadana u zad)
        sb = sb +s0   # te na kraju npr s4= s4+s0

   # listbk.append(k) #broji koji je stupanj polinoma
    #listb.append(sb)
#stvorit praznu listu i appendat sa u nju te printat listu

        if x==10 and k == 10:  # ako trazim polinom tocno odredenog stupnja ovaj dio koristim
            print(sb)

#print(listb)
    
