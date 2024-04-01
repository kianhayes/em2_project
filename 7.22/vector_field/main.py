import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from dipole_field import dipole_magnetic_field
from loop_field import loop_magnetic_field

# Initializing values
lim = 0.01 # Bounds for plot
r = np.linspace(1e-8, 1, 100)  # Polar radial distance
theta = np.linspace(0, 2 * np.pi, 100)  # Polar angle
ts = np.linspace(0,10,3) # Time array
ms = [] # Magnetic moment list for dipole
R, Theta = np.meshgrid(r, theta) # Polar coordinates meshgrid
f = 50 # Frequency of current
omega = 2*constants.pi*f # Angular frequency of current
I0 = 2 # Peak current
Is = [] # Empty current list for plotting
j = 0 # Inital index for file naming
b = 10 # Radius of loop of wire
a = 1 # Radius of little loop of wire

# Main loop
for t in ts:
    j = j + 1 # Indexing for file naming

    # Dipole parameters
    I_value =I0*np.sin(omega*t) # Current calculation
    m = I_value*np.pi*a**2 # Magnetic moment calculation
    Is.append(I_value) # Puts current calculation in current list

    # Compute magnetic field of dipole
    Br_dipole, Btheta_dipole = dipole_magnetic_field(R, Theta, m)
    B_mag_dipole = np.sqrt(Br_dipole**2 + Btheta_dipole**2)

    # Compute Magnetic field of loop of wire
    B_loop = np.zeros_like(R)
    for i in range(len(r)):
        for j in range(len(theta)):
            B_loop[i, j] = loop_magnetic_field(R[i, j], Theta[i, j], I_value, b)

    print(B_mag_dipole[1])
    print(B_loop[1])

    # Convert polar coordinates to Cartesian coordinates
    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)
    Y_shift = Y + (1/2)*lim # Shifts the dipole up on the y-axis

    '''
    # Plot magnetic field using contour plot
    plt.figure(figsize=(8, 6))
    dipole = plt.contourf(X, Y_shift, B_mag_dipole, levels=200, cmap='magma', extend='both', vmax=1e5)
    
    # Set color bar limits
    plt.xlim(-lim,lim)
    plt.ylim(-lim,lim)
    plt.colorbar(label='Magnetic Field Strength')
    plt.title(f'Magnetic Field of a Dipole at t = {round(t, 2)}')
    plt.show()

    plt.figure(figsize=(8, 6))
    loop = plt.contourf(X, Y, B_loop, levels=200, cmap='magma', extend='both', vmax=1e5)
    plt.xlim(-lim,lim)
    plt.ylim(-lim,lim)
    plt.colorbar(label='Magnetic Field Strength')
    plt.title(f'Magnetic Field of Loop at t = {round(t, 2)}')
    plt.show()
    #plt.savefig(f"7.22/figures/contour_animation/{j}.png")
'''