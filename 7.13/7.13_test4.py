import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

k = 1e-7

def b_field(x, y, z, t, k):
    return k * y**3 * t**2

x = np.linspace(-10, 10, num=100)
y = np.linspace(-10, 10, num=100)
z = np.linspace(-10, 10, num=100)
t = 5  # Selecting a single time step for visualization

X, Y, Z = np.meshgrid(x, y, z)

# Calculate magnetic field magnitude at each point
B = b_field(X, Y, Z, t, k)

# Calculate sizes of points based on the magnitude of the magnetic field
sizes = 10 * np.abs(B)

# Flatten the arrays for plotting
X_flat = X.flatten()
Y_flat = Y.flatten()
Z_flat = Z.flatten()

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X_flat, Y_flat, Z_flat, c='b', s=sizes.flatten(), alpha=0.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Magnetic Field at Time Step t={:.2f}'.format(t))

plt.show()
