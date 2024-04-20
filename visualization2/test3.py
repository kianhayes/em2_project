import numpy as np
import matplotlib.pyplot as plt

# Define the constant k
k = 1  # You can change this value as needed

# Define the range for y and t
y_values = np.linspace(-5, 5, 100)
t_values = np.linspace(0, 5, 100)

# Create a meshgrid for y and t
y, t = np.meshgrid(y_values, t_values)

# Calculate the magnetic field B(y, t)
B_z = k * y**3 * t**2

# Plot the magnetic field
plt.figure(figsize=(8, 6))
plt.contourf(y, t, B_z, cmap='viridis')
plt.colorbar(label='B(y,t)')
plt.title('Magnetic Field B(y,t) in z-direction')
plt.xlabel('y')
plt.ylabel('t')
plt.grid(True)
plt.show()
