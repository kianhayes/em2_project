import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_0 = 4e-7 * np.pi  # Permeability of free space (T*m/A)
I = 1.0  # Current (A)
b = 1.0  # Radius of the loop (m)

# Define the magnetic field function
def magnetic_field(r, theta):
    r_vec = np.array([np.cos(theta), np.sin(theta)])  # Unit vector in radial direction
    dl = b * np.array([-np.sin(theta), np.cos(theta)])  # Element of wire in polar coordinates
    r_sq = r**2
    dB = (mu_0 / (4 * np.pi)) * (I * np.cross(dl, r_vec) / r_sq)
    return dB

# Create a grid of r and theta values
r_values = np.linspace(0.1, 3, 100)
theta_values = np.linspace(0, 2*np.pi, 100)

# Calculate magnetic field at each point in the grid
B_r, B_theta = np.meshgrid(np.zeros_like(r_values), np.zeros_like(theta_values))
for i, r in enumerate(r_values):
    for j, theta in enumerate(theta_values):
        dB = magnetic_field(r, theta)
        B_r[j, i] = dB[0]
        B_theta[j, i] = dB[1]

# Convert to Cartesian coordinates for plotting
X, Y = r_values * np.cos(theta_values), r_values * np.sin(theta_values)
U, V = B_r * np.cos(theta_values) - B_theta * np.sin(theta_values), B_r * np.sin(theta_values) + B_theta * np.cos(theta_values)

# Plot the magnetic field
plt.figure(figsize=(8, 6))
plt.streamplot(X, Y, U, V, color='b', density=2)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Magnetic Field of a Current Loop')
plt.axis('equal')
plt.grid(True)
plt.show()
