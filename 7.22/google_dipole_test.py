import numpy as np
import matplotlib.pyplot as plt

# Define the dipole moment
m = np.array([0, 0, 1])

# Create a grid of points
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Calculate the magnetic field at each point
B = (3*m*(X*m) - np.linalg.norm(m)**2*X)/np.linalg.norm(X)**5

# Plot the contour plot
plt.contourf(X, Y, B, levels=20)
plt.colorbar()
plt.show()