import numpy as np
from matplotlib import pyplot as plt

def test1():
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    radii = np.linspace(0.01, 5, 10)
    thetas = np.linspace(0, 2 * np.pi, 40)
    theta, r = np.meshgrid(thetas, radii)

    f = plt.figure()

    ax = f.add_subplot(polar=True)
    ax.quiver(theta, r, 4 / (2 * np.pi) * theta, 4 * np.log(r) / (2* np.pi))
    #plt.savefig('task3_f1.png')
    plt.show()
    plt.close()

    f = plt.figure()
    ax = f.add_subplot(polar=True)
    ax.quiver(theta, r, 4 / (2 * np.pi) * np.log(r), 4 * theta / (2 * np.pi))
    plt.savefig('task3_f2.png')
    plt.show()


# Define the grid of polar coordinates
r = np.linspace(0.1, 5, 20)  # Radial coordinate
theta = np.linspace(0, 2*np.pi, 40)  # Angular coordinate
R, Theta = np.meshgrid(r, theta)

# Define parameters
Gamma = 1.0  # Replace with your desired value
lambda1 = 1.0
# Calculate the components of u1
u1_theta = Gamma / (2 * np.pi * R)

# Convert polar coordinates to Cartesian coordinates
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

# Plot the vector field
#plt.figure(figsize=(8, 6))
plt.quiver(X, Y, lambda1/(2 * np.pi * R), Theta * 0, scale=10, scale_units='xy')
plt.xlabel('X')
plt.ylabel('Y')
plt.title(r'Vector Field $\mathbf{u}_2$')
plt.axis('equal')
plt.savefig('task3_f2_cir.png')
plt.show()
