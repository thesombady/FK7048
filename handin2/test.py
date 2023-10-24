import numpy as np
import matplotlib.pyplot as plt


def func(x):
    beta = 1
    return -101.3*np.exp(9.82 / (-beta * 1)) * (293 - beta * x) / 293

xlist = np.linspace(0, 100000, 1000)
ylist = func(xlist)

plt.plot(xlist, ylist)

plt.show()