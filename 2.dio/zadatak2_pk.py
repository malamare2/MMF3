import numpy as np
import matplotlib.pyplot as plt

m = 0.1
k = 10 ** (-3)
g = 9.81

def alpha(v):
    return - (k / m) * v * abs(v) - g

def JUG_metoda(h0, v0, dt = 10**(-4)):
    t = [0]
    h = [h0]
    v = [v0]
    a = [alpha(v0)]
    
    i = 0
    while h[i] >= 0:
        i += 1
        t.append(i * dt)
        v.append(v[i-1] + a[i-1] * dt)
        h.append(h[i-1] + v[i-1] * dt + a[i-1] * dt ** 2 / 2)
        a.append(alpha(v[i]))
    
    return t, h, v, a

a, b, c, d = JUG_metoda(0, 15)

print(f"\nVrijeme udara: {a[-1]} s")

plt.plot(a, b, label = "polozaj")
plt.plot(a, c, label = "brzina")
plt.legend()
plt.show()

