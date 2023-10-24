"""
for i in range(0, 5, 2):
    a = (-1/2) ** (i + 1)
    print(i)
    print(a.as_integer_ratio())
"""
from math import sqrt, pi
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def d_factorial(n: int):
    if n <= 0:
        return 1
    else:
        return n * d_factorial(n - 2)

vals = [1/6, 1/60, 1/840]
for i in range(1, 6, 2):
    a = 2 / ( 2 ** (i + 1) * d_factorial(i + 3))
    print(a)
print()
for val in vals:
    print(val)