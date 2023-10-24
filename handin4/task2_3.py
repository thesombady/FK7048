import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


x = np.linspace(-10, 10, 500); z = np.linspace(-10, 10, 500)
XX, ZZ = np.meshgrid(x, z)

r = np.sqrt(XX**2 + ZZ**2)
theta = np.arctan2(XX, ZZ)
U = 1
R = 2

# Define the r component of the vector-field
r_ = U * np.cos(theta) - U * R**3 * np.cos(theta)/r**3

# Define the theta component of the vector-field
theta_ = - (U  * np.sin(theta) +  U * R**3 * np.sin(theta)/(2 * r**2))

fig, ax = plt.subplots(figsize=(6, 4))

#ax.quiver(XX, ZZ, r_, theta_, color='b', label='Vector field')
ax.quiver(XX, ZZ, r_, theta_,
          [pd.qcut(r_.flatten(), q= 20, labels=False)],
          headwidth=5,
          minlength=3,
          pivot='tail', 
          cmap='hsv')
plt.title(r'Vector field $\vec{u}(r, \theta)$')
plt.savefig('task2_3.png')
plt.show()
