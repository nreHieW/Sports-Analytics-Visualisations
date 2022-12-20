import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.patches as patches
import matplotlib.path as path


def draw_3d_pitch(fig,ax,amount,view ='20,160',line_color ='grey',pitch_color='white',linewidth=1,grid=False,**kwargs):
    min_h = 0 
    amount = int(amount[:-1])/100

    if view == 'sideline':
        ax.view_init(elev=8, azim=90)

    elif view == 'back':
        ax.view_init(elev=8, azim=-180)

    elif view == 'top':
        ax.view_init(elev=90, azim=90)
    else:
        view = view.split(',')
        ax.view_init(elev=int((view[0])), azim=int(view[1]))

    #plot outline and centre line
    ax.plot([100*(1-amount),100],[0,0],min_h,c=line_color,lw=linewidth,**kwargs)
    ax.plot([100*(1-amount),100],[100,100],min_h, c=line_color,lw=linewidth,**kwargs)
    ax.plot([100,100],[0,100],min_h,c=line_color,lw=linewidth,**kwargs)


    if amount == 1:
        ax.plot([100,100],[0,100],min_h,c=line_color,lw=linewidth,**kwargs)
        ax.plot([0,100*amount],[0,0],min_h,c=line_color,lw=linewidth,**kwargs)
        ax.plot([0,0],[0,100],min_h,c=line_color,lw=linewidth,**kwargs)
    if amount >= 0.5:
        ax.plot([50,50],[0,100],min_h,c=line_color,lw=linewidth,**kwargs)

    #Prepare Arcs

    Path = path.Path
    if amount > 0.77:
        pp1 = patches.PathPatch(
            Path([(17,38.5), (23,50), (17,61.5)],
                [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
            fc="none", transform=ax.transData,color=line_color)
        ax.add_patch(pp1)
        art3d.pathpatch_2d_to_3d(pp1, z=0, zdir="z")

    pp1 = patches.PathPatch(
    Path([(83,38.5), (77,50), (83,61.5)],
        [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,color=line_color)
    ax.add_patch(pp1)
    art3d.pathpatch_2d_to_3d(pp1, z=0, zdir="z")

    if amount > 0.83:
    #left penalty 
        ax.plot([17,17],[21.1,78.9],min_h,c=line_color,lw=linewidth,**kwargs)
        ax.plot([0,17],[78.9,78.9],min_h,c=line_color,lw=linewidth,**kwargs)
        ax.plot([0,17],[21.1,21.1],min_h,c=line_color,lw=linewidth,**kwargs)

    if amount > 0.94:
    #six yard 
        ax.plot([5.8,5.8],[36.8,63.2],min_h,c=line_color,lw=linewidth,zorder=2,**kwargs)
        ax.plot([0,5.8],[63.2,63.2],min_h,c=line_color,lw=linewidth,zorder=2,**kwargs)
        ax.plot([0,5.8],[36.8,36.8],min_h,c=line_color,lw=linewidth,zorder=2,**kwargs)

    #right penalty 
    ax.plot([83,83],[21.1,78.9],min_h,c=line_color,lw=linewidth,**kwargs)
    ax.plot([83,100],[78.9,78.9],min_h,c=line_color,lw=linewidth,**kwargs)
    ax.plot([83,100],[21.1,21.1],min_h,c=line_color,lw=linewidth,**kwargs)

    #six yard 
    ax.plot([94.2,94.2],[36.8,63.2],min_h,c=line_color,lw=linewidth,**kwargs)
    ax.plot([94.2,100],[63.2,63.2],min_h,c=line_color,lw=linewidth,**kwargs)
    ax.plot([94.2,100],[36.8,36.8],min_h,c=line_color,lw=linewidth,**kwargs)

    #center circle
    radius = 17.68
    width = radius * 0.68
    height = radius * 1.05
    if amount > 0.50:
        c_circle = patches.Ellipse((50,50),width,height,fill=False,edgecolor=line_color,lw=linewidth,zorder=-1)
        ax.add_patch(c_circle)
        art3d.pathpatch_2d_to_3d(c_circle, z=0, zdir="z")
    else:
        pp1 = patches.PathPatch(
        Path([(50,50-height/2), (50-(width*0.6),50), (50,50+height/2)],
            [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
        fc="none", transform=ax.transData)
        ax.add_patch(pp1)
        art3d.pathpatch_2d_to_3d(pp1, z=0, zdir="z")
    
    if amount >= 0.5:
        c_circle = patches.Ellipse((50,50),0.5,0.5,fill=False,edgecolor=line_color,lw=linewidth,zorder=-1)
        ax.add_patch(c_circle)
        art3d.pathpatch_2d_to_3d(c_circle, z=0, zdir="z")
    

    pen = patches.Ellipse((88.5,50),0.5,0.5,fill=False,edgecolor=line_color,lw=linewidth,zorder=-1)
    ax.add_patch(pen)
    art3d.pathpatch_2d_to_3d(pen, z=0, zdir="z")

    #pen spots

    if amount > 0.885:
        pen = patches.Ellipse((11.5,50),0.5,0.5,fill=False,edgecolor=line_color,lw=linewidth,zorder=-1)
        ax.add_patch(pen)
        art3d.pathpatch_2d_to_3d(pen, z=0, zdir="z")

    #goals
    scale = 68/100
    width = 7.32/scale
    height = 2.44/scale
    start = 50 - width/2
    end = 50 + width/2

    ax.plot([100,100],[start,start],[0,height],c=line_color,lw=linewidth)
    ax.plot([100,100],[end,end],[0,height],c=line_color,lw=linewidth)
    ax.plot([100,100],[start,end],[height,height],c=line_color,lw=linewidth)
    ax.plot([100,102],[start,start],[height,height],c=line_color,lw=linewidth)
    ax.plot([100,102],[end,end],[height,height],c=line_color,lw=linewidth)
    ax.plot([102,102],[start,start],[0,height],c=line_color,lw=linewidth)
    ax.plot([102,102],[end,end],[0,height],c=line_color,lw=linewidth)
    ax.plot([102,102],[start,end],[height,height],c=line_color,lw=linewidth)

    if amount == 1: #plot other side 
        ax.plot([0,0],[start,start],[0,height],c=line_color,lw=linewidth)
        ax.plot([0,0],[end,end],[0,height],c=line_color,lw=linewidth)
        ax.plot([0,0],[start,end],[height,height],c=line_color,lw=linewidth)
        ax.plot([0,-2],[start,start],[height,height],c=line_color,lw=linewidth)
        ax.plot([0,-2],[end,end],[height,height],c=line_color,lw=linewidth)
        ax.plot([-2,-2],[start,start],[0,height],c=line_color,lw=linewidth)
        ax.plot([-2,-2],[end,end],[0,height],c=line_color,lw=linewidth)
        ax.plot([-2,-2],[start,end],[height,height],c=line_color,lw=linewidth)

    if grid:
        for i in range(int(round((1-amount)*100)),100,5):
            ax.plot([i,i],[0,100],c=line_color,alpha=0.15,lw=0.5,zorder=-1)
        for i in range(0,100,5):
            ax.plot([100,100*(1-amount)],[i,i],c=line_color,alpha=0.15,lw=0.5,zorder=-1)

    ax.set_zlim(-50,50)
    ax.set_xlim(100*(1-0.7),100)
    ax.set_ylim(0,100)
    ax.set_box_aspect((105,68,50))
    ax.invert_yaxis()
    ax.invert_xaxis()
    ax.axis('off')
    fig.patch.set_facecolor(pitch_color)
    ax.set_facecolor(pitch_color)
    return ax

# import matplotlib.pyplot as plt
# fig = plt.figure(figsize=(10,6))
# ax = fig.add_subplot(111,projection = '3d')
# line_color ='black'
# linewidth = 1
# pitchcolor = 'white'

# ax = draw_3d_pitch(fig,ax,'70%','20,160',line_color,pitchcolor, linewidth,grid=True)


# ax.axis('on')
# ax.set_xlabel('X', fontsize=20)
# ax.set_ylabel('Y')
# plt.show()