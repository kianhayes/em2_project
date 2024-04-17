import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the constant k
k = 1  # You can change this value as needed

# Define the range for y and t
y_values = np.linspace(-5, 5, 100)
t_values = np.linspace(0, 5, 100)

# Create a meshgrid for y and t
y, t = np.meshgrid(y_values, t_values)

# Calculate the magnetic field components
B_y = 0  # In this case, B_y is zero
B_x = 0  # In this case, B_x is zero
B_z = k * y**3 * t**2

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the magnetic field
ax.plot_surface(y, t, B_z, cmap='viridis', edgecolor='none')
ax.set_title('Magnetic Field B(y,t) in z-direction')
ax.set_xlabel('y')
ax.set_ylabel('t')
ax.set_zlabel('B(y,t)')
ax.grid(True)

plt.show()
