import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.cm import ScalarMappable

def Bfield(x,y,t):
    B=y**3 * t**2
    return B


dt = 100
duration = 100
ts = np.linspace(0, duration, dt)
ys = np.linspace(0, duration, dt)
DT=duration/dt
a = 10
k = 1e-4
fluxs = np.full(dt, np.nan)
T = np.full(dt, np.nan)
emfs = np.full(dt, np.nan)
Bs = np.full((duration,dt), np.nan)
j = 0

Nx=100
x=np.linspace(0,a,Nx)
y=np.linspace(0,a,Nx)
X, Y = np.meshgrid(x,y)
dx=a/Nx
dy=a/Nx
flux_old=0.0
for t in ts:
    BXY = Bfield(X,Y,t)
    flux = np.sum(np.sum(BXY))*dx*dy

    fluxs[j]=flux
    T[j]=t
    emfs[j] = (flux-flux_old)/DT    
    flux_old=flux
    

    plt.figure()
    plotf = plt.plot(T, fluxs)
    plt.ylim(0, 1e8)
    plt.xlim(0, duration)
    plt.show()
    plt.savefig(f'7.13/figures2/magnetic_field/fluxes/{j}.png') # i don't know how to save each individual time step
    j=j+1
# plt.figure()
# #plotf = plt.plot(T, fluxs)
# plotf = plt.plot(T, emfs)
# #plt.ylim(0, 1e8)
# plt.xlim(0, duration)
# plt.show()




# for t in ts:
#     i = 0
#     flux_value = (1/4)*k*t**2*a**5
#     fluxs[j] = flux_value 

#     emf_value = -(1/2)*k*t*a**5
#     emfs[j] = emf_value

#     for y in ys:
#         B_value = k * y**3 * t**2
#         Bs[j][i] = B_value
#         i = i + 1

#     # magnetic field 
#     # plt.figure()
#     # plotb = plt.plot(ys, Bs[j])
#     # plt.ylim(0, 1e6)
#     # plt.xlim(0, duration)
#     # plt.xlabel('Time')
#     # plt.ylabel('Magnetic Field')
#     # plt.title(f'Magnetic field vs. y-position at t = {round(t, 3)}')
    
#     # flux
#     plt.figure()
#     plotf = plt.plot(ts, fluxs)
#     plt.xlim(0, duration)
#     plt.ylim(0, 25000)
#     plt.xlabel('Time')
#     plt.ylabel('Flux Value')
#     plt.title(f'Flux vs Time at t={round(t,3)}')
    
#     # emf
#     # plt.figure()
#     # plote = plt.plot(ts, emfs)
#     # plt.xlim(0, duration)
#     # plt.ylim(-700, 700)
#     # plt.xlabel('Time')
#     # plt.ylabel('EMF')
#     # plt.title(f'EMF vs. Time at t={round(t,3)}')
#     # plt.savefig(f'..//final_animation/moving/1D/{j}.png')
#     plt.show()


#     #trying to set multiple plots at once
#     '''''''''''''''
#     fig, axs = plt.subplots(3)
#     plt.setp(axs, xlim=(0,duration))
#     axs[0].plot(ys,Bs[j])
#     axs[0].set_title(f'Magnetic field vs. y-position at t = {round(t, 3)}')
#     axs[1].plot(ts,fluxs)
#     axs[1].set_title(f'Flux vs Time at t={round(t,3)}') 
#     axs[2].plot(ts,emfs)
#     axs[2].set_title(f'EMF vs. Time at t={round(t,3)}') 
#     plt.close()
#     '''''''''''
#     j = j + 1


    
