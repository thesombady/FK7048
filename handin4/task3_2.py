import numpy as np
import matplotlib.pyplot as plt

c = 1
L = 2
t = 5 
x = np.linspace(-10, 10, 1000)

def heavi(x: float):
    if x < 0:
        return 0
    return 1

def P(x):
    return 1 / (c *2) * ( (x + L ) * heavi(x + L) * heavi(L-x)  + 2 * L * heavi(x-L))


def expr(x):
    return P(x + c * t) - P(x - c * t)
    

plt.plot(x, [expr(i) for i in x])
plt.title(r'Wave-evolution with $c = 1$, $L = 2$ and $t = 5$')
plt.ylabel(r'$u(x, t)$')
plt.xlabel(r'x')
plt.savefig('task3_2_2.png')
plt.show()
