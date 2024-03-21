# My Animation Code
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def RotZ(x):
    return np.array([[np.cos(x), -np.sin(x), 0, 0], [np.sin(x), np.cos(x), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])


def RotY(x):
    return np.array([[np.cos(x), 0, np.sin(x), 0], [0, 1, 0, 0], [-np.sin(x), 0, np.cos(x), 0], [0, 0, 0, 1]])


def RotX(x):
    return np.array([[1, 0, 0, 0], [0, np.cos(x), -np.sin(x), 0], [0, np.sin(x), np.cos(x), 0], [0, 0, 0, 1]])


def Trans(x,y,z):
    return np.array([[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]])


# Translation and Rotation Matrix in 3D space
def Matrix_Transform(x, y, z, qx, qy, qz):
    return np.matmul(np.matmul(np.matmul(Trans(x,y,z), RotX(qx)), RotY(qy)), RotZ(qz)) 

# Translate and Rotate in 3D space
def Transform(Obj, Transform_Matrix):

    transformed_vertex = np.zeros((3,len(Obj.vertex)))  # array initialization

    for i in range(0, len(Obj.vertex)):
        arr = np.append(Obj.vertex[i],0)  
        vertex_rotated = np.matmul(Transform_Matrix, arr)
        vertex_rotated_translated = vertex_rotated + Transform_Matrix[:,3]
        transformed_vertex[:,i] = vertex_rotated_translated[:3]

    return transformed_vertex


class AniObj:
    def __init__(self, r, h):
        self.vertex = np.array([[r                   , 0                   , -h/2],
                                [r*np.cos(2 *np.pi/8), r*np.sin(2 *np.pi/8), -h/2],
                                [r*np.cos(4 *np.pi/8), r*np.sin(4 *np.pi/8), -h/2],
                                [r*np.cos(6 *np.pi/8), r*np.sin(6 *np.pi/8), -h/2],
                                [r*np.cos(8 *np.pi/8), r*np.sin(8 *np.pi/8), -h/2],
                                [r*np.cos(10*np.pi/8), r*np.sin(10*np.pi/8), -h/2],
                                [r*np.cos(12*np.pi/8), r*np.sin(12*np.pi/8), -h/2],
                                [r*np.cos(14*np.pi/8), r*np.sin(14*np.pi/8), -h/2],
                                [r                   , 0                   ,  h/2],
                                [r*np.cos(2 *np.pi/8), r*np.sin(2 *np.pi/8),  h/2],
                                [r*np.cos(4 *np.pi/8), r*np.sin(4 *np.pi/8),  h/2],
                                [r*np.cos(6 *np.pi/8), r*np.sin(6 *np.pi/8),  h/2],
                                [r*np.cos(8 *np.pi/8), r*np.sin(8 *np.pi/8),  h/2],
                                [r*np.cos(10*np.pi/8), r*np.sin(10*np.pi/8),  h/2],
                                [r*np.cos(12*np.pi/8), r*np.sin(12*np.pi/8),  h/2],
                                [r*np.cos(14*np.pi/8), r*np.sin(14*np.pi/8),  h/2]])

# Position and Rotation in time
A = np.array([[0, 0, 0, 0, 0, 0],
              [0.01599998, 0, -0.0006239, 0, 0.01136968, 0],
              [0.05403919, 0, 0.00676171, 0, 0.03658598, 0],
              [0.10514987, 0, 0.03305278, 0, 0.06318129, 0],
              [0.16226590, 0, 0.08316074, 0, 0.07898396, 0],
              [0.22450262, 0, 0.15264478, 0, 0.07800290, 0],
              [0.29704876, 0, 0.22760964, 0, 0.06264864, 0],
              [0.37834865, 0, 0.29329005, 0, 0.03757572, 0],
              [0.46285620, 0, 0.33771592, 0, 0.00815532, 0],
              [0.54269669, 0, 0.35392964, 0, -0.0215355, 0]])

# Parameters
radius = 5
height = 1

# Figure Setup
fig = plt.figure()
ax = Axes3D(fig)

# Animation
for i in range(0, len(A)):

    # Pause and clear window every iteration
    plt.pause(0.001)
    plt.cla()

    # Cylinder Setup
    CylinderObj = AniObj(radius, height)
    M = Matrix_Transform(A[i,0], A[i,1], A[i,2], A[i,3], A[i,4], A[i,5])
    CylinderObj.vertex = Transform(CylinderObj, M)
    Cylinder_vertices = list(zip(*(CylinderObj.vertex.tolist())))

    # Rendering in Poly3DCollection (list of list of triples) 
    # Top & Bottom
    Cylinder_Top    = [Cylinder_vertices[8:]]
    Cylinder_Bottom = [Cylinder_vertices[:8]]
    # Sides
    Cylinder_Side1  = [list(zip(*zip(Cylinder_vertices[0 ], Cylinder_vertices[1 ], Cylinder_vertices[9 ], Cylinder_vertices[8 ])))]
    Cylinder_Side2  = [list(zip(*zip(Cylinder_vertices[1 ], Cylinder_vertices[2 ], Cylinder_vertices[10], Cylinder_vertices[9 ])))]
    Cylinder_Side3  = [list(zip(*zip(Cylinder_vertices[2 ], Cylinder_vertices[3 ], Cylinder_vertices[11], Cylinder_vertices[10])))]
    Cylinder_Side4  = [list(zip(*zip(Cylinder_vertices[3 ], Cylinder_vertices[4 ], Cylinder_vertices[12], Cylinder_vertices[11])))]
    Cylinder_Side5  = [list(zip(*zip(Cylinder_vertices[4 ], Cylinder_vertices[5 ], Cylinder_vertices[13], Cylinder_vertices[12])))]
    Cylinder_Side6  = [list(zip(*zip(Cylinder_vertices[5 ], Cylinder_vertices[6 ], Cylinder_vertices[14], Cylinder_vertices[13])))]
    Cylinder_Side7  = [list(zip(*zip(Cylinder_vertices[6 ], Cylinder_vertices[7 ], Cylinder_vertices[15], Cylinder_vertices[14])))]
    Cylinder_Side8  = [list(zip(*zip(Cylinder_vertices[7 ], Cylinder_vertices[0 ], Cylinder_vertices[8 ], Cylinder_vertices[15])))]

    # Plot Cylinder on Axis 
    ax.add_collection3d(Poly3DCollection(Cylinder_Bottom, alpha=0.5,  linewidths=1, facecolors='darkcyan'), zs='z')
    ax.add_collection3d(Poly3DCollection(Cylinder_Top   , alpha=0.5,  linewidths=1, facecolors='darkcyan'), zs='z')
    ax.add_collection3d(Poly3DCollection(Cylinder_Side1 , alpha=0.5,  linewidths=1, facecolors='teal'), zs='z')
    ax.add_collection3d(Poly3DCollection(Cylinder_Side2 , alpha=0.5,  linewidths=1, facecolors='darkcyan'), zs='z')
    ax.add_collection3d(Poly3DCollection(Cylinder_Side3 , alpha=0.5,  linewidths=1, facecolors='teal'), zs='z')
    ax.add_collection3d(Poly3DCollection(Cylinder_Side4 , alpha=0.5,  linewidths=1, facecolors='darkcyan'), zs='z')
    ax.add_collection3d(Poly3DCollection(Cylinder_Side5 , alpha=0.5,  linewidths=1, facecolors='teal'), zs='z')
    ax.add_collection3d(Poly3DCollection(Cylinder_Side6 , alpha=0.5,  linewidths=1, facecolors='darkcyan'), zs='z')
    ax.add_collection3d(Poly3DCollection(Cylinder_Side7 , alpha=0.5,  linewidths=1, facecolors='teal'), zs='z')
    ax.add_collection3d(Poly3DCollection(Cylinder_Side8 , alpha=0.5,  linewidths=1, facecolors='darkcyan'), zs='z')

    # Set Window
    ax.set_xlim((-5, 5))
    ax.set_ylim((-5, 5))
    ax.set_zlim((-5, 5))


    # Show figure
    plt.show()
