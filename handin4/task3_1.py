import numpy as np
import matplotlib.pyplot as plt

c = 1
L = 2
t = 3
x = np.linspace(-10, 10, 1000)

def heavi(x: float):
    if x < 0:
        return 0
    return 1

def q(x):
    return (1-abs(x) / L) * heavi(1-abs(x) / L)

def expr(x):
    return 1 / 2 * (q(x + c*t) + q(x - c*t))

plt.plot(x, [expr(i) for i in x])
plt.title(r'Wave-evolution with $c = 1$, $L = 2$ and $t = 3$')
plt.ylabel(r'$u(x, t)$')
plt.xlabel(r'x')
#plt.savefig('task3_1.png')
plt.show()