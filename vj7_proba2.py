def Euler(t0, x0, v0, function, N, tN):
    '''
    Eulerova metoda za numericko rjesavanje obicnih diferencijalnih jednadzbi prvog reda.
    \nt0 --- pocetni trenutak
    \nx0 --- pocetni polozaj
    \nv0 --- pocetna brzina
    \nN  --- broj iteracija
    \ntN --- krajnji trenutak
    '''
    h = (tN-t0)/N #vremenski korak
    T = [t0] #pocetni trenutak
    X = [x0] #pocetni polozaj
    V = [v0] #pocetna brzina
    A = [function(t0, x0, v0)] #pocetna akceleracija
    while T[-1] <= tN:
        T.append(T[-1]+h)
        X.append(X[-1]+V[-1]*h)
        V.append(V[-1]+A[-1]*h)
        A.append(function(T[-1], X[-1], V[-1]))
    return T, X, V, A

def pred_kor(t0, x0, v0, function, N, tN):
    '''
    Prediktor-korektor metoda za numericko rjesavanje obicnih diferencijalnih jednadzbi prvog reda.
    \nt0 --- pocetni trenutak
    \nx0 --- pocetni polozaj
    \nv0 --- pocetna brzina
    \nN  --- broj iteracija
    \ntN --- krajnji trenutak
    '''
    h = (tN-t0)/N #vremenski korak
    T = [t0] #pocetni trenutak
    X = [x0] #pocetni polozaj
    V = [v0] #pocetna brzina
    A = [function(t0, x0, v0)] #pocetna akceleracija
    while T[-1] <= tN:
        t = T[-1]
        x = X[-1]
        v = V[-1]
        k1v = function(t, x, v)
        k1x = v
        k2v = function(t+h, x+h*k1x, v+h*k1v)
        k2x = v+h*k1v
        T.append(T[-1]+h)
        X.append(x+(k1x+k2x)*h/2)
        V.append(v+(k1v+k2v)*h/2)
        A.append(function(T[-1], X[-1], V[-1]))
    return T, X, V, A

def RK4(t0, x0, v0, function, N, tN):
    '''
    Runge-Kutta 4 metoda za numericko rjesavanje obicnih diferencijalnih jednadzbi prvog reda.
    \nt0 --- pocetni trenutak
    \nx0 --- pocetni polozaj
    \nv0 --- pocetna brzina
    \nN  --- broj iteracija
    \ntN --- krajnji trenutak
    '''
    h = (tN-t0)/N #vremenski korak
    T = [t0] #pocetni trenutak
    X = [x0] #pocetni polozaj
    V = [v0] #pocetna brzina
    A = [function(t0, x0, v0)] #pocetna akceleracija
    while T[-1] <= tN:
        t = T[-1]
        x = X[-1]
        v = V[-1]
        k1v = function(t, x, v)
        k1x = v
        k2v = function(t+h/2, x+h/2*k1x, v+h/2*k1v)
        k2x = v+h/2*k1v
        k3v = function(t+h/2, x+h/2*k2x, v+h/2*k2v)
        k3x = v+h/2*k2v
        k4v = function(t+h, x+h*k3x, v+h*k3v)
        k4x = v+h*k3v
        T.append(t+h)
        X.append(x+(k1x+2*k2x+2*k3x+k4x)*h/6)
        V.append(v+(k1v+2*k2v+2*k3v+k4v)*h/6)
        A.append(function(T[-1], X[-1], V[-1]))
    return T, X, V, A