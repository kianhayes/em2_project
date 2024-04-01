import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

def dipole_magnetic_field(r, theta, m):
    Br = (constants.mu_0 / (4 * np.pi)) * (2 * m * np.cos(theta)) / (r ** 3)
    Btheta = (constants.mu_0 / (4 * np.pi)) * (m * np.sin(theta)) / (r ** 3)

    return Br, Btheta

