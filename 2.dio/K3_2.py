import matplotlib.pyplot as plt

#cili graf je jedna velika matrica(uxt) i slazemo u stupce(t) i retke(x)

#difuzijska jednadžba
def explicit(ut0, t0, M, x0, X, N, a):   #-direktna metoda
    #N -  br tocaka u kojima se racuna vrijednost funkcije (proizvoljno npr 100)
    #tj na koliko sjelova dt - vremenski koraci
    #M - ukupan broj koraka
    
    dx=0.1  #(ode su dx i dt)
    dt=0.005
    alpha=a*dt/(dx**2) #-parametar uvik ovako

    #a je difuzijska konst  10**-2
    #x0, x su zadani u funkciji  rho(0,t)= rho(20,t) = 0

    time=[t0]
    space=[]
    uxt=[[]]


    i=0
    while i < N:   #ispunjava se prvi red matrice
        uxt[0].append(ut0(x0+i*dx))  #ut0 je rubni uvjet
        space.append(x0+i*dx)
        i+=1

    i=1
    j=1  #kako smo definirali prvi red matrice indeks ide od 1
    while j < M:
        u=[0]
        i=1
        while i < N-1:
            u.append(alpha*uxt[-1][i+1] + (1-2*alpha)*uxt[-1][i] + alpha*uxt[-1][i-1])
            i+=1
        u.append(0)
        uxt.append(u)
        time.append(t0+j*dt) #ispunimo sljedece stupce i retke do neke granice koju zadamo
        j+=1



    return time, space, uxt

def rhox0(x):
    if x>=0 and x<=1/5:
        rho=-x
    elif x>1/5 and x<=6/10:
        rho=x-2/5
    elif x>6/10 and x<=1:
        rho=1-x
    else:
        rho = 0
    return rho

# def rhox0(x1): # definiramo rubni uvjet kojeg koristimo u kodu
# #uvjet rho(x,0) ={5,5   xE(2,5)


E=explicit(rhox0, 0, 10, 0, 1, 10, 1)
#(uvjet, pocetno vrijeme, Dt - kad je najstabilniji, br koraka = M, pocetno polozaj rho(x,t) na papiru, krajnji rho(x,t) na papiru, N, a)

T=E[0]
X=E[1]
U=E[2]
i=0




plt.plot(X, U[6], label='t=6dt')   #U[int(0.4)]
plt.plot(X, U[8], label='t=8dt')
plt.plot(X, U[0], label='t=0dt')
# plt.plot(X, U[200], label='t=200dt')
# plt.plot(X, U[300], label='t=300dt')
# plt.plot(X, U[400], label='t=400dt')

# plt.xlabel('x (m)')
# plt.ylabel('rho(x, t) (kg/m)')
plt.title('Eksplicitna metoda')
plt.legend()
plt.show()



# def gx(x):
#     if x>=0 and x<=1/5:
#         rho=-x
#     elif x>1/5 and x<=6/10:
#         rho=x-2/5
#     elif x>6/10 and x<=1:
#         rho=1-x
#     else:
#         rho = 0
#     return rho