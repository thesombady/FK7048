import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(-5, 5, 100)

@np.vectorize
def transform(w):
    return 4/w * np.sin(w) + 2/(w ** 2) * (np.cos(w) - 1)

def ft(x):
    if x < 0 and x > - 1:
        return 1 + x
    elif x >= 0 and x < 1:
        return 1 - x
    else:
        return 0


plt.plot(xlist, transform(xlist), 'r', '.', markersize = 0.5, label = r'$\tilde{f}(\omega)$')
plt.plot(xlist, [ft(x) for x in xlist], 'b', '.', markersize = 0.5, label = r'$f(t)$')
plt.title(r'Transform of $f(t)$ and f(t)')
plt.grid()
plt.legend()
#plt.show()
plt.savefig('transform.png')
