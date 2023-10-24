import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


x = np.linspace(-2, 2, 20); z = np.linspace(-np.pi, np.pi, 20)
XX, ZZ = np.meshgrid(x, z)

r = np.sqrt(XX**2 + ZZ**2)
theta = np.arctan2(XX, ZZ)
Gamma = 1
lambd = 1



# Define the r component of the vector-field
r1 =  Gamma / (2 * np.pi) * theta
r2 = lambd/(2 * np.pi) * np.log(r)
# Define the theta component of the vector-field
theta1 = -Gamma * np.log(r) / (2 * np.pi)
theta2 =0 #lambd / (2 * np.pi) * theta 

fig, ax = plt.subplots(figsize=(6, 4))

#ax.quiver(XX, ZZ, r_, theta_, color='b', label='Vector field')
"""
ax.quiver(XX, ZZ, r1, theta1,
          [pd.qcut(theta1.flatten(), q= 10, labels=False)],
          headwidth=7,
          minlength=3,
          pivot='tail', 
          cmap='viridis')
"""
ax.quiver(XX, ZZ, r2, theta2, cmap = 'viridis')
plt.title(r'Vector field $\vec{u}_2(r, \theta)$')
plt.xlabel(r'$r$')
plt.ylabel(r'$\theta$')
#plt.savefig('task3_f2_cir.png')
plt.show()
