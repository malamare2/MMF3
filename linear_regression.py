# linearna regresiaj



import matplotlib.pyplot as plt
from scipy import stats

x = [0, 0.176, 0.3010299957]
y = [1.447,1.88, 2.146]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.xlabel("log(L)")
plt.ylabel("log(m)")
plt.legend(['mjerenje', 'aproksimacija'])
plt.show()




#plotanje ovisnoti y i x 


# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15])
# ypoints = np.array([0.8346, 0.7266, 0.6261, 0.55587, 0.482265, 0.43317, 0.382187, 0.34835, 0.3109, 0.2844272, 0.2660573, 0.24858, 0.224859, 0.211955576, 0.195])

# plt.scatter(xpoints, ypoints, label ="mjerenja")
# plt.xlabel("alpha[°]")
# plt.ylabel("zeta")
# plt.legend()
# plt.show()