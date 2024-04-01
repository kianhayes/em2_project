import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

def loop_magnetic_field(r, theta, I, b):
    # Define the observation grid
    

    # Calculate the magnetic field components
    B_r = np.zeros_like(r)
    B_theta = np.zeros_like(theta)

    for i in range(len(r_vals)):
        for j in range(len(theta_vals)):
            r = r_vals[i]
            theta = theta_vals[j]

            B_r[i, j] = 0  # No radial component since we're considering a circular loop
            B_theta[i, j] = (constants.mu_0 / (4*np.pi)) * (1 / r) * b**2 * np.sin(theta) / (r**2 + b**2 - 2*r*b*np.cos(theta))

    # Calculate the total magnetic field magnitude
    B_mag = np.sqrt(B_r**2 + B_theta**2)

    return B_mag

'''
r = np.linspace(1e-8, 1, 100)
theta = np.linspace(0, 2 * np.pi, 100)
R, Theta = np.meshgrid(r, theta)
'''
b = 10
r_vals = np.linspace(0.01, 3*b, 100)  # r from slightly above 0 to 3 times the loop radius
theta_vals = np.linspace(0, 2*np.pi, 200)  # theta from 0 to 2*pi
R, Theta = np.meshgrid(r_vals, theta_vals)
I = 2

B_mag = loop_magnetic_field(R, Theta, I, b)

X = R * np.cos(Theta)
Y = R * np.sin(Theta)

# Plot magnetic field using contour plot
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, B_mag, levels=200, cmap='magma')

# Set color bar limits
plt.colorbar(label='Magnetic Field Strength')
plt.title(f'Magnetic Field')
plt.show()
