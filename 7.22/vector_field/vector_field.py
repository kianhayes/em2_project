# Plots the vector field for the magnetic field of a dipole

import numpy as np
from matplotlib import pyplot as plt
from scipy import constants
from sympy import symbols, diff
import matplotlib.animation as animation
import pandas as pd

# Would like to use this as a test to eventually get to a point where we can animate the changing magnetic field as the current changes in a wire

I = 0.02 # Initial Current
a = 1000 # Radius of loop
colors_in_quiver = 100
headwidth=3 # Head of line size
minlength=1 # Minimum length of line
pivot='tail' # Location on field line where the vector is pivoted 
lim = 0.25 
dx = 1000 # Spacing between vector field points

x, y = np.meshgrid(np.linspace(-lim, lim, dx),  
                   np.linspace(-lim, lim, dx)) 

r = np.sqrt(x**2 + y**2)
theta = np.arctan(y/x)

u = ((constants.mu_0*I*a**2) / (4 * r**3))*(2*np.cos(theta))
v = ((constants.mu_0*I*a**2) / (4 * r**3))*(np.sin(theta))

print(u)
'''
fig,ax=plt.subplots(1,1)
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
data = np.random.rand(4, 4)
ax=plt.imshow(r, extent=[-1, 1, -1, 1])
#ax.contourf(u,v)
ax.set_xlim(-3e-5, 3e-5)
ax.set_ylim(-3e-5, 3e-5)
'''

fig = plt.quiver(x, y, u, v,
          headwidth=headwidth,
          minlength=minlength,
          pivot=pivot,
          cmap='inferno')
          #clim= [0,100])

plt.xlim(-lim, lim) 
plt.ylim(-lim, lim) 
plt.colorbar()
plt.title('Dipole Magnetic Field') 
plt.show()

