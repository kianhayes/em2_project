import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

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

