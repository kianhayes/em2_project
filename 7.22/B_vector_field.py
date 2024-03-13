# Plots the vector field for the magnetic field of a dipole

import numpy as np
from matplotlib import pyplot as plt
from scipy import constants
from sympy import symbols, diff
import matplotlib.animation as animation
import pandas as pd

# Would like to use this as a test to eventually get to a point where we can animate the changing magnetic field as the current changes in a wire

I = 0.02
a = 10
colors_in_quiver = 100
headwidth=3
minlength=1
pivot='tail'
lim = 0.25
dx = 1000

x, y = np.meshgrid(np.linspace(-lim, lim, dx),  
                   np.linspace(-lim, lim, dx)) 

r = np.sqrt(x**2 + y**2)
theta = np.arctan(y/x)

u = ((constants.mu_0*I*a**2) / (4 * r**3))*(2*np.cos(theta))
v = ((constants.mu_0*I*a**2) / (4 * r**3))*(np.sin(theta))

plt.quiver(x, y, u, v,
          [pd.qcut(u.flatten(), q=colors_in_quiver, labels=False)],
          headwidth=headwidth,
          minlength=minlength,
          pivot=pivot,
          cmap='inferno')

plt.title('Dipole Magnetic Field') 

plt.xlim(-lim, lim) 
plt.ylim(-lim, lim) 
  
#plt.grid() 
plt.show() 

