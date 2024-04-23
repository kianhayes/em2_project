import numpy as np
import matplotlib.pyplot as plt
k = 1e-7

def b_field(y,t,z,k):
    return k*y**3*t**2



def dot(vec0, vec1):
    return vec0 @ vec1

def da(z,dz):
    return np.array([z*dx*dy])

# Define bounds of integration for x, y, and z
xmin = 0
xmax = 1
ymin = 0
ymax = 1
zmin = 0
zmax = 0

# Define number of steps for x, y, and z
xstepmax = 101
ystepmax = 101
zstepmax = 101

# Define step size for x, y, and z
dx = (xmax-xmin)/xstepmax
dy = (ymax-ymin)/ystepmax
dz = (zmax-zmin)/zstepmax

# Initial value of flux
flux = 0

for xsteps in range(0,xstepmax):
    x =  xmin + (dx * xsteps) # Current x value, starting at xmin and increasing by dx with each iteration

    for ysteps in range(0,ystepmax):   
        y = ymin + (dy * ysteps) # Current y value, starting at ymin and increasing by dy with each iteration          
        flux += dot(b_field(x,y,1), da(x,y,1,dx,dy,0)) * dx * dy # dot(E,da) * dx * dy 

print(flux)
