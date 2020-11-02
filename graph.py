# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 10:24:17 2020

@author: jmcos
"""


from matplotlib import*




#ARGUMENTS: 
#Un axe ax
#Une config c sous la forme d'une matrice Nx2
#Le temps t correspondant à la config pour la placer sur l'axe des y

def afficher_config(ax,c,t,dalto=False):
    if(dalto):
        couleur=["white","blue","red"]
    else:
        couleur=["white","orange","darkred"]
    X=c.shape[0]
    
    if(X>19):
        for i in range(X):
            v=c[i]
            if(int(v[0]) != 0):
                ax.add_patch(patches.Rectangle((i,t+0.2),0.375,0.5,facecolor=couleur[int(v[0])]))
            if(int(v[1])!=0):
                 ax.add_patch(patches.Rectangle((i+0.375,t+0.2),0.375,0.5,facecolor=couleur[int(v[1])]))

    else:
        for i in range(X):
            v=c[i]
            ax.add_patch(patches.Rectangle((i,t+0.2),0.375,0.5,facecolor=couleur[int(v[0])],edgecolor="black"))
            ax.add_patch(patches.Rectangle((i+0.375,t+0.2),0.375,0.5,facecolor=couleur[int(v[1])],edgecolor="black"))

    return
    
    
    
    

def afficher_liste_config(l,daltonisme=False):
    figure,ax = pyplot.subplots()


    #suppression des marges
    pyplot.gcf().subplots_adjust(0,0,1,1)

    #suppression des axes
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    #pas de cadre
    ax.set_frame_on(False)
    
    ax.set_xlim(0,l[0].shape[0])
    ax.set_ylim(0,len(l))
    
    for i in range(len(l)):
        afficher_config(ax, l[i], i,dalto=daltonisme)
    
    return
    
    
    
    
    
    
"""

ax.add_artist(patches.Rectangle((0.2,0.2),0.75,1,facecolor="green",edgecolor="black"))
ax.add_artist(patches.Rectangle((0,5.2),0.75,1,facecolor="green",edgecolor="black"))
ax.set_xlim(0,10)
ax.set_ylim(0,10)

"""