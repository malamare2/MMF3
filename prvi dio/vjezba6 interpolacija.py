import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


X = [-5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5]
Y = [1/np.sqrt(1-t) for t in X]

# for X in range((-5, 1), 10):
#     Y = 1/np.sqrt(1-X)

print(Y)

c = []
for x in range(-5, 1):
    c.append(x)

def firstder(x):
    return(-6)*(-45064)*x**(-7) ###derivirat zadanu koji imam napisanu za Y tocke

firstder_0 = (Y[1]-Y[0])/(X[1]-X[0])
# Stvaranje cubic spline interpolacije
cs = CubicSpline(X, Y, bc_type=((1, firstder_0), (1, firstder(X[-1]))))

# Procjena interpolacijske vrijednosti u nekoj točki (npr. x = 2.5)
x1_interpolate = -5
x2_interpolate = -4.7
x3_interpolate = -1.25
x4_interpolate = -0.7

y1_interpolate = cs(x1_interpolate)
y2_interpolate = cs(x2_interpolate)
y3_interpolate = cs(x3_interpolate)
y4_interpolate = cs(x4_interpolate)

# Ispis rezultata
print(f'Interpolirana vrijednost pri x={x1_interpolate} je y={y1_interpolate}')
print(f'Interpolirana vrijednost pri x={x2_interpolate} je y={y2_interpolate}')
print(f'Interpolirana vrijednost pri x={x3_interpolate} je y={y3_interpolate}')
print(f'Interpolirana vrijednost pri x={x4_interpolate} je y={y4_interpolate}')

#plt.scatter(c, cs, s=10, facecolors='none', edgecolors='yellow')

plt.scatter(X, Y)
# plt.plot(np.linspace(0, 4, 100), cs(np.linspace(0, 4, 100)), label='Cubic Spline interpolacija')
# plt.scatter(x1_interpolate, y1_interpolate, color='red', marker='o')
# plt.scatter(x2_interpolate, y2_interpolate, color='yellow', marker='o')
# plt.scatter(x3_interpolate, y3_interpolate, color='blue', marker='o')
# plt.scatter(x4_interpolate, y4_interpolate, color='green', marker='o')

plt.show()
