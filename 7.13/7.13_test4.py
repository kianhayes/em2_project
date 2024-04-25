import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.cm import ScalarMappable

k = 1e-7

def b_field(y, t, k):
    B = k * y**3 * t**2
    return B

x = np.linspace(0, 10, num=100)
y = np.linspace(0, 10, num=100)
z = np.linspace(0, 10, num=100)
t = np.linspace(0, 100, 10)  # Selecting a single time step for visualization

X, Y = np.meshgrid(x, y)

for t in t:
    # Calculate magnetic field magnitude at each point
    B = b_field(Y, t, k)
    contour = plt.contourf(X, Y, B, levels = 200, cmap = 'magma', vmin=0, vmax=0.2)
    plt.title(f'Magnetic Field at Time Step t={t}')
    plt.colorbar(ScalarMappable(norm=contour.norm, cmap=contour.cmap))

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
