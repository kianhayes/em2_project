from sympy import symbols, diff
from scipy import constants
import numpy as np

a = 1
b = 4
f = 50
omega = 2*constants.pi*f
I0 = 2
ts = np.linspace(0,100,1000)
Is = []
fluxs = []
z0 = 100
zs = []
emfs = []
z_value = 2*t+z0
I_value = I0*np.sin(omega*t)
flux_value = (constants.mu_0 * I_value * constants.pi * a**2 * b**2) / (2*(b**2 + z_value**2)**(3/2))
emf_value = diff(flux_value, t)