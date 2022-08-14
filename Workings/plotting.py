
import matplotlib.pyplot as plt 
from pitch import draw_3d_pitch
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.patches as patches
import numpy as np
from scipy import interpolate
import math


def get_curve_coords(p1, p2,flip_coords = False):
    if flip_coords:
        p1[0],p1[1] = p1[1],p1[0]
        p2[0],p2[1] = p2[1],p2[0]
    
    #https://stackoverflow.com/questions/16525814/python-how-to-draw-a-curve-between-two-3d-points

    y=np.array([0,.5,.75,.75,.5,0]) #describe your shape in 1d like this
    d = math.sqrt((p1[0] - p2[0]) **2 + (p1[1] - p2[1]) **2)

    if d < 10: 
        amp = 0
    elif d > 65:
        amp = 20
    else:
        amp = d - 40
    #get the adder. This will be used to raise the z coords
    x=np.arange(y.size)
    xnew = np.linspace(x[0],x[-1] , 100) #sample the x coord
    tck = interpolate.splrep(x,y,s=0) 
    adder = interpolate.splev(xnew,tck,der=0)*amp
    adder[0]=adder[-1]=0
    adder=adder.reshape((-1,1))

    #get a line between points
    shape3=np.vstack([np.linspace(p1[dim],p2[dim],100) for dim in range(3)]).T

    #raise the z coordinate
    shape3[:,-1]=shape3[:,-1]+adder[:,-1]

    x,y,z=(shape3[:,dim] for dim in range(3))
    return x,y,z

def plot_trajectory(startx,starty,endx,endy,ax,flip_coords = False,*args,**kwargs):
    for i in range(len(startx)):
        x,y,z = get_curve_coords([startx[i],starty[i],0],[endx[i],endy[i],0],flip_coords)
        ax.plot(x,y,z,*args,**kwargs)
    return ax

def plot_scatter_2d(x,y,ax,flip_coords=False,*args, **kwargs):
    '''
    Takes in 2d points X and Y and loops through them creating a Ellipse Patch using the ARGS and KWARGS
    Pass in flip_coords = TRUE if needed since 3d plot x and y are swapped 
    '''
    if flip_coords:
        x,y = y,x

    for x_i,y_i in zip(x,y):
        c = patches.Ellipse((x_i,y_i),0.68,1.05,*args,**kwargs)
        ax.add_patch(c)
        art3d.pathpatch_2d_to_3d(c, z=0, zdir="z")
    return ax

