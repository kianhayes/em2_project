import numpy as np
from matplotlib import pyplot as plt
from scipy import constants
from sympy import symbols, diff
import matplotlib.animation as animation

'''
This models the interaction between two loops of wire of different radii separated by a distance z with one of the loops having
a changing current in it. Specifically, current is flowing through loop B and the change in flux through loop a is calculated. The interaction is
animated over time to show how the flux through the loop is changing with time. In addition, the separation between the two loops changes as a 
function of time. Does this affect the magnetic field due to Faraday's Law?
'''

# Constants
a = 1 # Radius of small loop
b = 4 # Radius of big loop
f = 50 # Frequency of current
omega = 2*constants.pi*f
I0 = 2 # Peak Current
ts = np.linspace(0,100,1000)

# Intializing lists to store values
z0 = 100 # Initial separation between loops
Is = []
fluxs = []
zs = [] 
emfs = []
old_flux = 0

# For loop that does all calculations for each time step
for t in ts:
    z_value = (2*t)+z0
    I_value = I0*np.sin(omega*t)
    flux_value = (constants.mu_0 * I_value * constants.pi * a**2 * b**2) / (2*(b**2 + z_value**2)**(3/2))
    fluxs.append(flux_value)
    emfs.append((flux_value-old_flux)/0.1)
    old_flux = flux_value
    Is.append(I_value)
    zs.append(z_value)

# Defining different the various lines to be graphed
fig, axs = plt.subplots(3)
line1 = axs[0].plot(ts[0], Is[0])[0]
line2 = axs[1].plot(ts[0], fluxs[0])[0]
line3 = axs[2].plot(ts[0], emfs[0])[0]
axs[0].set(xlim=[0, 100], ylim=[-3, 3], xlabel='Time [s]', ylabel='Current through Loop B')
axs[1].set(xlim=[0, 100], ylim=[-10e-11, 10e-11], xlabel='Time [s]', ylabel='Flux through Loop A')
axs[2].set(xlim=[0, 100], ylim=[-5e-11, 5e-11], xlabel='Time [s]', ylabel='EMF')

# Animation Function that updates the graph
def update(frame):
    line1.set_xdata(ts[:frame])
    line1.set_ydata(Is[:frame])
    line2.set_xdata(ts[:frame])
    line2.set_ydata(fluxs[:frame])
    line3.set_xdata(ts[:frame])
    line3.set_ydata(emfs[:frame])
    return (line1, line2)

# Animation and plotting
ani = animation.FuncAnimation(fig=fig, func=update, interval=1e-6, cache_frame_data=False)
fig.tight_layout()
plt.show()