import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

def magnetic_field_dipole_polar(r, theta, m):
    mu_0 = 4 * np.pi * 1e-7  # vacuum permeability constant

    # Compute the magnetic field components
    Br = (mu_0 / (4 * np.pi)) * (2 * m * np.cos(theta)) / (r ** 3)
    Btheta = (mu_0 / (4 * np.pi)) * (m * np.sin(theta)) / (r ** 3)

    return Br, Btheta

def magnetic_field_wire_loop(r, theta, I, a):
    mu_0 = 4 * np.pi * 1e-7  # vacuum permeability constant
    
    # Define the wire loop in polar coordinates
    theta_loop = np.linspace(0, 2*np.pi, 100)  # angular coordinate
    r_loop = a * np.cos(theta_loop - np.pi/2)  # radial coordinate of the wire loop
    
    # Initialize magnetic field strength
    B = 0
    
    # Compute contributions from each segment of the wire loop
    for i in range(len(theta_loop)-1):
        dl_r = r_loop[i+1] - r_loop[i]
        
        r_r = r - (r_loop[i] + dl_r/2)
        
        r_mag = np.sqrt(r_r**2)
        dl_mag = np.sqrt(dl_r**2)
        
        B += (mu_0/(4*np.pi)) * (I * dl_mag / r_mag)
        
    return B

lim = 0.01

# Define polar grid
r = np.linspace(1e-8, 1, 100)  # radial distance
theta = np.linspace(0, 2 * np.pi, 100)  # angle

ts = np.linspace(0,10,3) # Time array
ms = [] # Magnetic moment list

# Create a meshgrid in polar coordinates
R, Theta = np.meshgrid(r, theta)

# Defining the current changing in the loop
f = 50 # Frequency of current
omega = 2*constants.pi*f
I0 = 2
Is = []
j = 0
b = 10 # Radius of loop of wire
a = 1 # Radius of little loop of wire

for t in ts:
    # Indexing for file naming
    j = j + 1

    # Dipole parameters
    I_value =I0*np.sin(omega*t)

    m = I_value*np.pi*a**2 # magnetic moment
    Is.append(I_value)

    # Compute magnetic field of dipole in polar coordinates
    Br_dipole, Btheta_dipole = magnetic_field_dipole_polar(R, Theta, m)
    B_mag_dipole = np.sqrt(Br_dipole**2 + Btheta_dipole**2)

    # Compute Magnetic field strength of loop of wire
    B_loop = np.zeros_like(R)
    for i in range(len(r)):
        for j in range(len(theta)):
            B_loop[i, j] = magnetic_field_wire_loop(R[i, j], Theta[i, j], I_value, b)

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