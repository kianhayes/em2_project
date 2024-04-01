import numpy as np
from matplotlib import pyplot as plt
from scipy import constants
from sympy import symbols, diff
import matplotlib.animation as animation

a = 1e10 # Radius of small loop
b = 4 # Radius of big loop
f = 50 # Frequency of current
omega = 2*constants.pi*f
I0 = 2 # Peak Current
ts = np.linspace(0,100,1000)

Is = []
fluxs = []
z0 = 100 # Loops initial separation
zs = []
emfs = []

for t in ts:
    z_value = (t/10)**2 + z0
    I_value = I0*np.sin(omega*t)
    flux_value = (constants.mu_0 * I_value * constants.pi * a**2 * b**2) / (2*(b**2 + z_value**2)**(3/2))
    fluxs.append(flux_value)
    Is.append(I_value)
    zs.append(z_value)

fig, axs = plt.subplots(3)
axs[0].plot(ts, Is)
axs[0].set_title("Current Through Loop A (A)")
axs[1].plot(ts, fluxs)
axs[1].set_title("Flux Through Loop B (Wb)")
axs[2].plot(ts, zs)
axs[2].set_title("Separation Between Loop A and B")
fig.tight_layout()

plt.show()