import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

def e_field(r, theta, phi):
    k = 1 / 4*np.pi*constants.epsilon_0
    const = k / r

    Er = const*3
    Etheta = const*2*np.sin(theta)*np.cos(theta)*np.sin(phi)
    Ephi = const*np.sin(theta)*np.cos(phi)
    
    E_mag = np.sqrt(Er**2 + Etheta**2 + Ephi**2)

    return E_mag

r = np.linspace(0.01, 1, 100)
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)

R, Theta, Phi = np.meshgrid(r, theta, phi)

E_field = e_field(R, Theta, Phi)
E_field = E_field[:, :, 0]

X = R * np.sin(Theta) * np.cos(Phi)
Y = R * np.sin(Theta) * np.sin(Phi)
Z = R * np.cos(Theta)

lim = 0.1
plt.contourf(X[:, :, 0], Z[:, :, 0], E_field, levels = 1000, cmap = 'magma')
plt.xlim(0, 2.5*lim)
plt.ylim(-lim,lim)
plt.show()