import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
k = 1e-7

def b_field(x,y,z,t,k):
    return k*y**3*t**2

x = np.linspace(-10,10, num=100)
y = np.linspace(-10,10, num=100)
z = np.linspace(-10,10, num=100)
t_values = np.linspace(0,10, num=10) # 10 time-steps

fig=plt.figure(figsize=(12,10))

for i, t in enumerate(t_values):
    B=b_field(x,y,z,t,k)

    ax = fig.add_subplot(3,4,i+1,projection='3d')
    ax.set_title('Time Step = {:.2f}'.format(t))

    for xi in x:
        for yi in y:
            for zi in z:
                size = 10*np.abs(b_field(xi,yi,zi,t,k))
                ax.scatter(xi,yi,zi,c='b',s=size, alpha=0.5)




    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

plt.tight_layout()
plt.show()

