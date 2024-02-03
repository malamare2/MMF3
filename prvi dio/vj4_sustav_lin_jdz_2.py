import math
import numpy as np
import matplotlib as plt

R1 = [0, -2, -2, -2]   #definirani potrebne nizove
R2 = [4, 6, 6, 8]
R3 = [-2, -2, -2, 0]
R4 = [5, 0, 0, 0]

R3cc = [R3[0]/R2[0]]  #ovo su prvi clanovi 
R4cc = [R4[0]/R2[0]]

for i in range(1, 3): #posto vec imam definiran prvi clan krece se od drugog clana do predzadnjeg
    R3cc.append(R3[i]/(R2[i]-R1[i]*R3cc[i-1]))
    R4cc.append((R4[i]-R1[i]*R4cc[i-1])/(R2[i]-R1[i]*R3cc[i-1]))

R4cc.append((R4[3] - R1[3]*R4cc[2])/(R2[3] - R1[3]*R3cc[2]))# sad tražim cetvrti član liste(zadnji clan)
I = R4cc[3]
Ilista = []
Ilista.append(I)

for i in range(1, 4): #zadano je da moran obrnit ali to ne funkcionira pa se doda brojac
    k = 3-i  #to je brojač da bi išla unazad jer ako obrnem u for ptlji to neće funkcionirati
    Ilista.append(R4cc[k] - R3cc[k]*Ilista[i-1]) #jer je u zadatku zadano da je ovdje najveca vrijednost a kako smo mi appendali zadnju vrijednost tako da dalje treba appendat iducu ud najvece do najmanje

#provjera rezultata
Iprovjera = []
for i in range(0, 4):
    k = 3-i #vracam na pravu stranu
    Iprovjera.append(round(Ilista[k]*94))


print (Iprovjera)

#treba opcenitije definirati ako mi dode ovakav na ispitu