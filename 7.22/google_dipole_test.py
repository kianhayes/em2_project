import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

'''
# Create a grid of x and y values
X = np.linspace(-10, 10, 1000)
Y = np.linspace(-10, 10, 1000)
a = 1
I = 2

# Calculate the B field at each point in the grid
B = np.zeros((len(X), len(Y)))
for i in range(len(X)):
    for j in range(len(Y)):
        B[i,j] = np.sqrt(((constants.mu_0*I*a**2*X[i])/(2*(X[i]**2+Y[j]**2)**2))**2 / ((constants.mu_0*I*a**2*Y[j])/(4*(X[i]**2+Y[j]**2)**2))**2)
        #B[i, j] = (I*constants.mu_0*a**2*np.sqrt(4*(X[i]**2)+(Y[j]**2)))/(4*((X[i]**2)+(Y[j]**2))**2)

# Plot the contour field
plt.contourf(X, Y, B, 200, cmap='magma')
plt.colorbar()
plt.show()
'''

def magnetic_field_dipole_polar(r, theta, m):
    mu_0 = 4 * np.pi * 1e-7  # vacuum permeability constant

    # Compute the magnetic field components
    Br = (mu_0 / (4 * np.pi)) * (2 * m * np.cos(theta)) / (r ** 3)
    Btheta = (mu_0 / (4 * np.pi)) * (m * np.sin(theta)) / (r ** 3)

    return Br, Btheta

lim = 0.01

# Define polar grid
r = np.linspace(1e-8, 1, 100)  # radial distance
theta = np.linspace(0, 2 * np.pi, 100)  # angle
ts = np.linspace(0,10,20)
ms = []

# Create a meshgrid in polar coordinates
R, Theta = np.meshgrid(r, theta)

f = 50 # Frequency of current
omega = 2*constants.pi*f
I0 = 2
Is = []

for t in ts:
# Dipole parameters
    I_value =I0*np.sin(omega*t)
    a = 1
    m = I_value*np.pi*a**2 # magnetic moment
    Is.append(I_value)

    # Compute magnetic field components in polar coordinates
    Br, Btheta = magnetic_field_dipole_polar(R, Theta, m)

    B_mag = np.sqrt(Br**2 + Btheta**2)

    # Normalize the magnetic field strength
    B_normalized = B_mag / np.max(B_mag)

    # Convert polar coordinates to Cartesian coordinates
    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)

    print(f'B_mag at t={t}: {B_mag}')

    # Plot magnetic field using contour plot

    fig1=plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, B_mag, levels=200, cmap='magma', extend='both', vmax=1e18)

    # Set color bar limits
    plt.xlim(-lim,lim)
    plt.ylim(-lim,lim)
    plt.colorbar(label='Magnetic Field Strength')
    plt.title(f'Magnetic Field of a Dipole at t = {round(t, 2)}')
    #plt.show()
    plt.savefig(f"7.22/figures/contour_animation/{round(t, 2)}.png")
