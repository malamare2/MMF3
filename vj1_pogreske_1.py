import math
import numpy as np
from tabulate import tabulate


#RED
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

for x in range(0, 110, 10):
    listax.append(x)
#id do 110 jer je korak od 10 pa se gleda 10,20,30 a mora ukljucivati 100 pa nemoze biti 101

#k i s0 su definirani unutar for petlje jer se uvjek mora gledati ta pocetna vrijednost koju smo zadali
    k=0
    s0=1
    sa = s0
    while abs(s0)>=eps:
        #apsolutni jer kad se uvrsti u doli formulu od s0 u jednom trenutku bi dobili negativni br sto ne smije biti
        
        k = k+1
        s0 = (-1)**k *((x**k)/math.factorial(k))
        sa = sa +s0

        #treba vidit ako je paran onda ide + ovaj clan ako je neparan ide minus

    listak.append(k)
    lista.append(sa)
#stvorit praznu listu i appendat sa u nju te printat listu
#print(lista)




#REKURZIVNA
eps = 10**(-10)
listb= [] #polinomi
listbx = []
listbk = [] #stupanj polinoma

for x in range(0, 110, 10):

    listbx.append(x)

    k=0
    s0=1 #(polinomi) #ovo je jedan polinom mogu ih imat vise pa bi bilo s1, s2, s3... a traženi bi bia npr s4 =s0
    sb = s0
    while abs(s0)>=eps:
        #apsolutni jer kad se uvrsti u doli formulu od s0 u jednom trenutku bi dobili negativni br sto ne smije biti
        
        k = k+1 #stupanj polinoma
        s0 = -s0*(x/k)   #ode ide rekurzivna relacija s0 =...(zadana u zad)
        sb = sb +s0   # te na kraju npr s4= s4+s0

    listbk.append(k) #broji koji je stupanj polinoma
    listb.append(sb)


        #if x==10 and k == 10:  # ako trazim polinom tocno odredenog stupnja ovaj dio koristim
            #print(sb)

print(listb)









listc = []
listcx = []
listck = []

for x in range(0, 110, 10):
    listcx.append(x)

    e = math.exp(x)
    invert = 1/e
    listc.append(invert)

    #uvrstit u red i onda samo rezultat stavit na minus prvu

#table1 = []
#row =[x, sa, sb, invert, k]
#table1.append(row)

#vrh_tablice = ['x', 'e^(-x)_a', 'e^(-x)_b', 'e^(-x)_c', 'br. članova']
#tablica = tabulate(table1, vrh_tablice)
#print(tablica)






eps = 10**(-10)
listd = []
listdx = []
listdk = []


for x in range(0, 110, 10):
    listdx.append(x)

    k=0
    s0=1
    sd = s0
    while abs(s0)>=eps:
        
        k = k+1
        s0 = ((x**k)/math.factorial(k))
        sd = sd +s0


    listdk.append(k)
    listd.append(1/sd)










#print(lista, listb, listc)



#fali mi jos zadnji dio
#br članova
#gornja granica
#spremiti sve u tekstualnu datoteku(ono sta smo radili sa kalinicem)




#prvi nacin


table = [['x', 'e^(-x)_a', 'e^(-x)_b', 'e^(-x)_c', 'br. članova'],
        [], 
        [listcx[0], lista[0], listb[0], listc[0], listak[0]], 
        [listcx[1], lista[1], listb[1], listc[1], listak[1]], 
        [listcx[2], lista[2], listb[2], listc[2], listak[2]], 
        [listcx[3], lista[3], listb[3], listc[3], listak[3]], 
        [listcx[4], lista[4], listb[4], listc[4], listak[4]], 
        [listcx[5], lista[5], listb[5], listc[5], listak[5]],
        [listcx[6], lista[6], listb[6], listc[6], listak[6]],
        [listcx[7], lista[7], listb[7], listc[7], listak[7]],
        [listcx[8], lista[8], listb[8], listc[8], listak[8]],
        [listcx[9], lista[9], listb[9], listc[9], listak[9]],
        [listcx[10], lista[10], listb[10], listc[10], listak[10]]]
#TREBALO BI OVO POPRAVIT DA MI SAM IZVLACI ELEMENTE TABLICE DOK NE DODE DO 10- OG ELEMENTA 

#print(tabulate(table))






#2.nacin

table1 = []

poc_element = 0
for i in range(0, 11):
   row =[listcx[poc_element+i], lista[poc_element+i], listb[poc_element+i], listc[poc_element+i], listd[poc_element+i], listak[poc_element+i]]
   table1.append(row)

#    print(listcx[poc_element+i], lista[poc_element+i], listb[poc_element+i], listc[poc_element+i], listak[poc_element+i])

#vidit sta jos fali

vrh_tablice = ['x', 'e^(-x)_a', 'e^(-x)_b', 'e^(-x)_c', 'e^(-x)_d', 'br. članova']
tablica = tabulate(table1, vrh_tablice)
#print(tablica)












# poc_element = 0
# for i in range(0, 11):
#    a = listcx[poc_element+i]
#    b = lista[poc_element+i]
# #    print(listcx[poc_element+i], lista[poc_element+i], listb[poc_element+i], listc[poc_element+i], listak[poc_element+i])

# #vidit sta jos fali


# #print(tabulate(table))



# items = [a,b]
# file = open('items.txt','w')
# for ite in items:
#     file.write(ite+"\n")
# file.close()
