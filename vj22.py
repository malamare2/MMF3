import numpy as np
from math import *
xx = [] #list of x values
frw = [] #list of forw. differencies of x
def derForward(f, I, h):
    x = np.arange(I[0], I[1], h)
    f = np.vectorize(f)
    for x_ in x[:-1]:
        dxdy = (f(x_+h)-f(x_))/ h
        xx.append(x_)
        frw.append(dxdy)
    x = np.array(xx)
    dy = np.array(frw)
    return x, dy