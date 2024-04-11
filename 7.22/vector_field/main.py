import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from scipy import constants

'''
Have to add the calculation of the magnetic field due to an induced emf. To calculate emf we can use (emf = -M*dI_1/dt) and give the loops some internal resistance in order to calculate
emf = I_2R_2. Solving this for I_2 we get the induced current due to the change in current of the other loop. Now that we have this current we can add it to the internal current that it may have
in order to get the total current flowing through the loop. We use this current then to find the magnetic field. 
'''
 
def dipole_magnetic_field(r, theta, R, I, shift):
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    area = np.pi*R**2
    m = I*area
    const = (constants.mu_0*m)/(4*np.pi*(np.sqrt(x**2 + (y - shift)**2))**3)
    Br = const*2*np.cos(theta)
    Btheta = const*np.sin(theta)
    
    return Br, Btheta

def loop_magnetic_field(r, theta, R, I):
    Br = 0
    Btheta = (constants.mu_0 * I * R**2 * np.cos(theta)) / (2 * np.pi * (r**2 + R**2)**(3/2))

    return Br, Btheta

# Initializing values
lim = 5 # Bounds for plot
r = np.linspace(0.001, 10, 100)  # Polar radial distance
theta = np.linspace(0, 2*np.pi, 100)  # Polar angle
dt = 60

ms = [] # Magnetic moment list for dipole
R, Theta = np.meshgrid(r, theta) # Polar coordinates meshgrid
f = 60 # Frequency of current
ts = np.linspace(0, 2*f, dt) # Time array
omega = 2*constants.pi*f # Angular frequency of current
I0 = 2 # Peak current
Is = [] # Empty current list for plotting
j = 0 # Inital index for file naming
b = 4 # Radius of loop of wire
a = 0.4e-2 # Radius of little loop of wire
z0 = (1/2)*lim # Separation between loops
resistance_a = 1
resistance_b = 10
I_old_b = I0
I_old_a = 0
I_total_a = I_old_a

for t in ts:
    I = I0*np.sin(omega*t) # Current in loop B
    z = z0 # Separation between two at time t
    M = (constants.mu_0*np.pi*a**2*b**2) / (2*(b**2 + z**2)**(3/2)) # Mutual Inductance as a function of z
    emf_a = -M*(I - I_old_b)/dt # Induced emf in Loop A and B
    I_induced_a = emf_a / resistance_a # Induced current in Loop A due to change in current in Loop B
    I_total_a = I_total_a + I_induced_a # Total current through loop A
    emf_b = -M*(I_total_a - I_old_a)/dt
    I_induced_b = emf_b / resistance_b # Induced current in loop B due to change in current in loop A
    I_total_b = I + I_induced_b # Total current through loop B

    Br_loop, Btheta_loop = loop_magnetic_field(R, Theta, R=b, I=I_total_b)
    B_mag_loop = np.sqrt(Br_loop**2 + Btheta_loop**2)

    Br_loop2, Btheta_loop2 = dipole_magnetic_field(R, Theta, R=a, I=I_total_a, shift=z)
    B_mag_loop2 = np.sqrt(Br_loop2**2 + Btheta_loop2**2)

    I_old_b = I_total_b
    I_old_a = I_total_a

    # Convert polar coordinates to Cartesian coordinates
    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)

    vmin = 0
    vmax = 1e-7

    '''
    # Plot magnetic field using contour plot
    plt.figure(figsize=(8, 6))
    loop1 = plt.contourf(X, Y, B_mag_loop, levels=200, cmap='magma', extend='both', vmax=vmax, vmin=vmin)
    plt.xlim(-lim,lim)
    plt.ylim(-lim,lim)
    plt.title(f'Loop 1 Magnetic Field with R = b')
    plt.colorbar(ScalarMappable(norm=loop1.norm, cmap=loop1.cmap))
    plt.show()

    plt.figure(figsize=(8, 6))
    loop2 = plt.contourf(X, Y, B_mag_loop2, levels=200, cmap='magma', extend='both')
    plt.xlim(-lim,lim)
    plt.ylim(-lim,lim)
    plt.title(f'Loop 2 Magnetic Field with dipole appoximation')
    plt.colorbar(ScalarMappable(norm=loop2.norm, cmap=loop2.cmap))
    plt.show()
    '''
    print(f'Total dipole magnetic field at {t}: {B_mag_loop2}')
    print(f'Total Magnetic field array at {t}: {B_mag_loop + B_mag_loop2}')

    plt.figure(figsize=(8, 6))
    loop3 = plt.contourf(X, Y, B_mag_loop2 + B_mag_loop, levels=200, cmap='magma', extend='both')
    plt.xlim(-lim,lim)
    plt.ylim(-lim,lim)
    plt.title(f'Magnetic Field Sum')
    plt.colorbar(ScalarMappable(norm=loop3.norm, cmap=loop3.cmap))
    plt.show()